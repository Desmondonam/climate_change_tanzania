import pandas as pd

def filter_by_location(df, location):
    """
    Filters data by location.
    """
    return df[df['location'] == location]

# Example usage
# filtered_data = filter_by_location(data, "Dar es Salaam")