import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="desmond2@HB",  # Hardcoded for testing
    database="tanzania_climate_change",
    port=3306
)

print("Connected successfully!")  # If this works, env loading is the issue