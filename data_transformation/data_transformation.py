import pandas as pd

def transform_data(df):
    """
    Transforms the cleaned data.
    """
    # Convert temperature from Kelvin to Celsius
    df['temperature_c'] = df['temperature_k'] - 273.15
    
    # Aggregate data by location and date
    transformed_df = df.groupby(['location', 'date']).agg({
        'temperature_c': 'mean',
        'rainfall_mm': 'sum',
        'co2_ppm': 'mean'
    }).reset_index()
    
    return transformed_df

# Example usage
# transformed_data = transform_data(cleaned_data)