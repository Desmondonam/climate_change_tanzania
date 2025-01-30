import psycopg2
from config import DB_CONFIG

def save_to_sql(df, table_name):
    """
    Saves data to a SQL database.
    """
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    # Create table if not exists
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            location TEXT,
            date DATE,
            temperature_c FLOAT,
            rainfall_mm FLOAT,
            co2_ppm FLOAT
        )
    """)
    
    # Insert data
    for _, row in df.iterrows():
        cursor.execute(f"""
            INSERT INTO {table_name} (location, date, temperature_c, rainfall_mm, co2_ppm)
            VALUES (%s, %s, %s, %s, %s)
        """, (row['location'], row['date'], row['temperature_c'], row['rainfall_mm'], row['co2_ppm']))
    
    conn.commit()
    cursor.close()
    conn.close()

# Example usage
# save_to_sql(transformed_data, "climate_data")