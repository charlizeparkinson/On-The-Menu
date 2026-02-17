import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")


"""
Create a .env file that looks like this

DB_HOST=your_localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=food_waste

SPOONACULAR_API_KEY=your_key_here

"""
