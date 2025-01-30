import requests
import pandas as pd
from config import API_KEY

def fetch_weather_data(api_url, location, start_date, end_date):
    """
    Fetches weather data from an API.
    """
    params = {
        "location": location,
        "start_date": start_date,
        "end_date": end_date,
        "api_key": API_KEY
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

# Example usage
# weather_data = fetch_weather_data("https://api.weather.com/v1/data", "Dar es Salaam", "2023-01-01", "2023-12-31")