import pandas as pd
from database import load_to_staging, get_staging_data

def standardize_column_names(df):
    """
    Standardizes column names by converting to lowercase and replacing spaces with underscores.
    """
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    return df

def clean_data(df, stats, initial_records_count):
    """
    Cleans the data by handling missing values and duplicates.
    Updates the stats dictionary.
    """
    # Duplicates
    initial_rows_before_dedupe = len(df)
    df.drop_duplicates(inplace=True)
    stats['duplicates_dropped'] = initial_rows_before_dedupe - len(df)
    
    # Calculate Data Quality based on rows remaining after deduplication
    records_after_deduplication = len(df)
    stats['data_quality'] = (records_after_deduplication / initial_records_count) * 100 if initial_records_count > 0 else 0

    # Missing values - cast to python int
    stats['nans_filled'] = int(df['value'].isna().sum())
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df['value'].fillna(0, inplace=True)
    
    return df

def transform_data(df):
    """
    Applies transformations to the data.
    """
    df['value'] = df['value'] * 2
    return df

def run_etl(input_file='input.csv'):
    """
    Main function to run the ETL process.
    Returns the original dataframe, transformed dataframe, and summary statistics.
    """
    # --- Extraction and Initial Stats ---
    original_df = pd.read_csv(input_file)
    initial_records_count = len(original_df)
    stats = {
        'records_processed': initial_records_count,
        'duplicates_dropped': 0,
        'nans_filled': 0,
        'data_quality': 0 # Will be updated in clean_data
    }

    # --- Transformation ---
    df = original_df.copy()
    df = standardize_column_names(df)
    df = clean_data(df, stats, initial_records_count) # Pass initial_records_count
    transformed_df = transform_data(df.copy())

    # cast to python int
    stats['transformations'] = int(stats['duplicates_dropped'] + stats['nans_filled'])

    # --- Loading ---
    transformed_df.to_csv('output.csv', index=False)
    load_to_staging(transformed_df)

    print("\nETL process completed successfully.")
    
    return original_df, transformed_df, stats


if __name__ == "__main__":
    print("Running ETL process from command line...")
    original_df, transformed_df, stats = run_etl()
    print("\n--- Summary ---")
    print(stats)
    print("\n--- Final Staging Table ---")
    print(get_staging_data())