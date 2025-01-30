import pandas as pd

def clean_data(df):
    """
    Cleans the raw data by handling missing values and duplicates.
    """
    # Drop duplicates
    df = df.drop_duplicates()
    
    # Fill missing values
    df['temperature_k'].fillna(df['temperature_k'].mean(), inplace=True)
    df['rainfall_mm'].fillna(0, inplace=True)
    df['co2_ppm'].fillna(df['co2_ppm'].median(), inplace=True)
    
    return df

# Example usage
# cleaned_data = clean_data(raw_data)