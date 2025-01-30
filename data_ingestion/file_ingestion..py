import pandas as pd

def read_csv(file_path):
    """
    Reads data from a CSV file.
    """
    return pd.read_csv(file_path)

def read_excel(file_path):
    """
    Reads data from an Excel file.
    """
    return pd.read_excel(file_path)

def read_json(file_path):
    """
    Reads data from a JSON file.
    """
    return pd.read_json(file_path)

# Example usage
# data = read_csv("data/weather_data.csv")