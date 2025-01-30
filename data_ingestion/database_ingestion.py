import psycopg2
import pandas as pd
from config import DB_CONFIG

def fetch_from_sql(query):
    """
    Fetches data from a SQL database.
    """
    conn = psycopg2.connect(**DB_CONFIG)
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Example usage
# data = fetch_from_sql("SELECT * FROM climate_data")