# ETL Workbench - Simple Data Pipeline project

A modern, elegant ETL (Extract, Transform, Load) application built with Flask that enables users to upload CSV files, perform data transformations, and visualize the entire data pipeline process.

<img width="1910" height="898" alt="image" src="https://github.com/user-attachments/assets/844c13c9-2ae1-4d60-a23a-ed23191c93c6" />

<img width="682" height="847" alt="image" src="https://github.com/user-attachments/assets/5e6c705f-ebd6-460c-a570-3070307397d7" />

## ✨ Features

- **📊 Interactive Data Upload** - Drag & drop or browse to upload CSV files
- **🔄 Automated ETL Pipeline** - Extract, Transform, and Load data seamlessly
- **🎯 Data Cleansing** - Intelligent handling of missing values and data quality issues
- **📈 Visual Pipeline Flow** - Clear visualization of each ETL stage
- **📋 Multi-Stage Display** - View original, transformed, and staged data side-by-side
- **📊 Quality Metrics** - Real-time statistics on data processing
- **🎨 Modern UI** - Clean, professional interface with Rosewood & Misty Rose theme
- **📱 Responsive Design** - Works beautifully on desktop, tablet, and mobile

## 🛠️ Technology Stack

- **Backend:** Python 3.8+, Flask
- **Data Processing:** Pandas
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Database:** SQLite (or your preferred database)

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.8 or higher
- pip (Python package installer)
- Git (optional, for cloning)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Thirukaalathessvarar-S/my_etl_project.git
cd my_etl_project
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
flask run
```

The application will start at `http://localhost:5000`

## 📁 Project Structure

```
etl-workbench/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── input.csv              # Default sample dataset
│
├── templates/
│   ├── index.html         # Landing page with upload interface
│   └── results.html       # Results page showing ETL output
│
├── static/
│   └── (optional assets)
│
└── README.md              # Project documentation
```

## 💻 Usage

### Running Default ETL

1. Navigate to `http://localhost:5000`
2. Click "Run Demo ETL" to process the default `input.csv`
3. View the results showing all three stages of the pipeline

### Uploading Custom CSV

1. Click "Choose CSV File" or drag & drop your file
2. Click "Process Data" to run the ETL pipeline
3. Review the transformed data and staging results

### Expected CSV Format

Your CSV should have the following structure:

```csv
id,Full Name,value
1,first,100.0
2,second,NaN
3,third,300.0
```

## 🔧 ETL Pipeline Stages

### 1️⃣ Extract
- Reads CSV file
- Validates data structure
- Displays original data

### 2️⃣ Transform
- Cleans column names (lowercase, underscores)
- Handles missing values (NaN → 0)
- Applies business logic transformations
- Doubles numeric values (example transformation)

### 3️⃣ Load
- Appends transformed data to staging table
- Maintains data history
- Displays full staging table

## 📊 Data Transformations

Current transformations include:

- **Column Renaming:** `Full Name` → `full_name`
- **Null Handling:** `NaN` → `0.0`
- **Value Multiplication:** All values × 2
- **Data Type Validation:** Ensures consistent types

## 🎨 Customization

### Changing Theme Colors

Edit the CSS variables in `templates/index.html` and `templates/results.html`:

```css
/* Current theme: Rosewood & Misty Rose */
--primary-color: #70020F;
--secondary-color: #FFDEE2;
--accent-color: #8B0000;
```

### Adding New Transformations

Edit the transformation logic in `app.py`:

```python
def transform_data(df):
    # Add your custom transformations here
    df = df.fillna(0)
    df['value'] = df['value'] * 2
    return df
```

## 📈 Future Enhancements

- [ ] Export results to CSV/Excel
- [ ] Advanced filtering options
- [ ] Multiple file format support (JSON, XML)
- [ ] Database integration options
- [ ] Scheduled ETL jobs
- [ ] Data validation rules
- [ ] Error logging dashboard
- [ ] API endpoints for programmatic access

## 🐛 Troubleshooting

### Common Issues

**Issue:** `ModuleNotFoundError: No module named 'flask'`
```bash
pip install flask pandas SQLAlchemy gunicorn
```

**Issue:** Port 5000 already in use
```bash
# Change port in app.py
app.run(debug=True, port=5001)
```

**Issue:** CSV encoding errors
- Ensure CSV is UTF-8 encoded
- Check for special characters

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Thirukaalathessvarar S**
- GitHub: [@yourusername](https://github.com/Thirukaalathessvarar-S/)
- Email: eswar2005s@gmail.com

## 🙏 Acknowledgments

- Thanks to the Flask community for excellent documentation
- Pandas library for powerful data manipulation
- Inspiration from modern data engineering practices
