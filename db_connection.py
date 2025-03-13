# db_connection.py
import pyodbc
import urllib.parse
import pandas as pd
from sqlalchemy import create_engine

def fetch_data_from_sqlserver():
    try:
        # SQLserver Database Configuration
        server = "DESKTOP-HF8BC08"
        database = "Claims"
        driver = "ODBC Driver 17 for SQL Server"

        # Constructing connection parameters for the SQL Server database
        params = urllib.parse.quote_plus(
        f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};Trusted_Connection=yes"
)
        # Create a connection string
        conn_str = f"mssql+pyodbc:///?odbc_connect={params}"

        # Initialize the database engine
        engine = create_engine(conn_str)

        # Query to fetch data
        query = "SELECT [Date], [close] FROM [fiveYearStockPrice] ORDER BY Date" 


    # Fetch data into a DataFrame
        df = pd.read_sql(query, engine)
        
        if df.empty:
            print("Warning: The DataFrame is empty. No data fetched from the database.")
        return df

    except Exception as e:
        print(f"Error fetching data from SQL Server: {e}")
        return None