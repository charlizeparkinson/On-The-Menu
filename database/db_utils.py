import mysql.connector
from config import DB_CONFIG
from mysql.connector import Error # Error class for db specific exception
from dotenv import load_dotenv # function to load env vars from .env file
import os

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)
load_dotenv() # loads all vars from .env for os.getenv() access

# reads db name and db credentials from env var, and use them to establish connection to database
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
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None