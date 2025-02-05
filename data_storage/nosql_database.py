from pymongo import MongoClient

def save_to_mongodb(df, db_name, collection_name):
    """
    Saves data to a MongoDB collection.
    """
    client = MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    collection = db[collection_name]
    
    # Convert DataFrame to dictionary
    data = df.to_dict("records")
    
    # Insert data here
    collection.insert_many(data)

# Example usage
# save_to_mongodb(transformed_data, "climate_db", "climate_data")