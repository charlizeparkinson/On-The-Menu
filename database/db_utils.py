import mysql.connector # connects python to db
from mysql.connector import Error # Error class for db specific exception
from dotenv import load_dotenv # loads env variables from .env file
import os # allows access to env variables via os.getenv

load_dotenv() # loads all vars from .env for os.getenv() access

# stores values from .env as python variables
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


# db connection
def get_connection():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return connection
    except Error as e: # catches error
        print(f"Error connecting to MySQL: {e}")
        return None