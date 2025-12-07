import os
import random
import time
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from main import run_etl
from database import get_staging_data

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'csv'}
app.secret_key = 'super_secret_key'  # Needed for session management

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def style_transformed_df(df, original_df):
    nan_mask = original_df.isna()
    
    def highlight_nan_changes(col):
        styles = pd.Series('', index=col.index)
        if col.name == 'value':
            original_nans = nan_mask.get('value', pd.Series())
            if not original_nans.empty:
                new_zeros = (col == 0)
                styles[original_nans & new_zeros] = 'background-color: #fdebd0' # Subtle orange for NaN -> 0
        return styles

    def badge_formatter(val):
        # Add a badge to the value column
        return f'{val} <span class="badge">x2</span>'

    # Chain the styling operations
    styled_df = df.style.apply(highlight_nan_changes, axis=0) \
                        .format({'value': badge_formatter})
    
    return styled_df.to_html(classes='data', header="true", escape=False)


@app.route('/')
def index():
    try:
        df = pd.read_csv('input.csv')
        default_csv_html = df.to_html(classes='data', header="true")
    except FileNotFoundError:
        default_csv_html = "<p>Default input.csv not found.</p>"
    return render_template('index.html', default_csv_html=default_csv_html)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        original_df, transformed_df, summary_stats = run_etl(filepath)
        
        styled_html = style_transformed_df(transformed_df, original_df)

        session['original_data'] = original_df.to_html(classes='data', header="true")
        session['transformed_data'] = styled_html
        session['summary_stats'] = summary_stats
        
        return redirect(url_for('loader'))
    return redirect(request.url)

@app.route('/run_default_etl', methods=['POST'])
def run_default_etl():
    original_df, transformed_df, summary_stats = run_etl()
    
    styled_html = style_transformed_df(transformed_df, original_df)

    session['original_data'] = original_df.to_html(classes='data', header="true")
    session['transformed_data'] = styled_html
    session['summary_stats'] = summary_stats
    
    return redirect(url_for('loader'))

@app.route('/loader')
def loader():
    return render_template('loader.html')

@app.route('/results')
def results():
    original_data = session.get('original_data', '<h3>No original data found.</h3>')
    transformed_data = session.get('transformed_data', '<h3>No transformed data found.</h3>')
    staging_data = get_staging_data()
    summary_stats = session.get('summary_stats', {})
    return render_template('results.html', 
                           original_data=original_data, 
                           transformed_data=transformed_data,
                           staging_data=staging_data.to_html(classes='data', header="true"),
                           summary_stats=summary_stats)

if __name__ == '__main__':
    app.run(debug=True)