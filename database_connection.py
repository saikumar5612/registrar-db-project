# database_connection.py
import mysql.connector
from db_config import db_config

def connect():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Connected to the database successfully!")
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Test connection
if __name__ == "__main__":
    conn = connect()
    if conn:
        conn.close()
