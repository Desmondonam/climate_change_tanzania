def validate_data(df):
    """
    Validates the integrity of the transformed data.
    """
    if df.isnull().any().any():
        raise ValueError("Data contains missing values.")
    if df.duplicated().any():
        raise ValueError("Data contains duplicates.")
    return True

# Example usage
# validate_data(transformed_data)