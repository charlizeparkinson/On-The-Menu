from fastapi import APIRouter, Body # allows api requests in json body

from database.CRUD.ingredients import select_ingredients
from database.db_utils import get_connection # connects to database


router = APIRouter()

@router.post("/recipes/search")
def search_recipes(data: dict = Body(default={})):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    try:
        cur.execute(select_ingredients) # fetch all ingredients from kitchen
        kitchen = cur.fetchall()
        if not kitchen:
            return {"recipes": [], "message": "Oops - your kitchen is empty!"}

        kitchen_names = [item["ingredient_name"] for item in kitchen] # extract ingredient names
        priority_ingredients = kitchen_names[:3] # ingredients that have the top 3 closest expiration dates

        return {
            "kitchen": kitchen_names,
            "priority_ingredients": priority_ingredients
        }

    finally:
        cur.close()
        conn.close()
