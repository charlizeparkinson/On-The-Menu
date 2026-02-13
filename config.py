import os
from dotenv import load_dotenv

load_dotenv

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

"""
Create a .env file that looks like this

DB_HOST=your_localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=food_waste
"""
