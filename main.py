import pandas as pd

def standardize_column_names(df):
    """
    Standardizes column names by converting to lowercase and replacing spaces with underscores.
    """
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    return df

def clean_data(df):
    """
    Cleans the data by handling missing values and duplicates.
    """
    print("Dropping duplicate rows...")
    df.drop_duplicates(inplace=True)

    # Convert 'value' to numeric, coercing errors to NaN
    df['value'] = pd.to_numeric(df['value'], errors='coerce')

    print("Handling missing values...")
    df['value'].fillna(0, inplace=True)
    return df

def transform_data(df):
    """
    Applies transformations to the data.
    """
    print("Applying a basic transformation (value * 2)...")
    df['value'] = df['value'] * 2
    return df

def main():
    """
    Main function to run the ETL process.
    """
    # Extract
    input_file = 'input.csv'
    print(f"Reading data from {input_file}...")
    df = pd.read_csv(input_file)
    print("\nOriginal Data:")
    print(df)
    print("\nOriginal Data Types:")
    print(df.dtypes)

    # Standardize column names
    print("\nStandardizing column names...")
    df = standardize_column_names(df.copy())
    print("Data with Standardized Columns:")
    print(df)

    # Transform (Clean)
    print("\nCleaning data...")
    cleaned_df = clean_data(df.copy())
    print("Cleaned Data:")
    print(cleaned_df)

    # Transform (Apply transformations)
    print("\nTransforming data...")
    transformed_df = transform_data(cleaned_df.copy())
    print("Transformed Data:")
    print(transformed_df)

    # Inspect final types
    print("\nFinal Data Types:")
    print(transformed_df.dtypes)


    # Load
    output_file = 'output.csv'
    print(f"\nWriting cleaned and transformed data to {output_file}...")
    transformed_df.to_csv(output_file, index=False)
    print("Done.")

if __name__ == "__main__":
    main()