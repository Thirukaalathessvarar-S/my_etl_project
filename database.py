import pandas as pd
from sqlalchemy import create_engine

def load_to_staging(df, db_file='staging.db', table_name='staging_table'):
    """
    Loads the DataFrame to a SQLite staging table, appending new rows.
    """
    print(f"\nAppending data to SQLite staging table '{table_name}' in '{db_file}'...")
    engine = create_engine(f'sqlite:///{db_file}')
    df.to_sql(table_name, engine, if_exists='append', index=False)
    print("Data successfully appended to staging table.")

def get_staging_data(db_file='staging.db', table_name='staging_table'):
    """
    Reads and returns the content of the staging table as a DataFrame.
    """
    print(f"\nReading content of staging table '{table_name}':")
    engine = create_engine(f'sqlite:///{db_file}')
    try:
        with engine.connect() as connection:
            df = pd.read_sql_table(table_name, connection)
            return df
    except Exception as e:
        print(f"Could not read table '{table_name}'. It may not exist yet. Error: {e}")
        return pd.DataFrame() # Return empty DataFrame on error
