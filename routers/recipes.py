import requests
from fastapi import APIRouter, Body, HTTPException
from database.CRUD.ingredients import select_ingredients
from database.db_utils import get_connection # connects to database
from config import SPOONACULAR_API_KEY


router = APIRouter()

@router.post("/recipes/search")
def search_recipes(data: dict = Body(default={})):
    if not SPOONACULAR_API_KEY:
        raise HTTPException(status_code=500, detail="missing SPOONACULAR_API_KEY in .env")

    # fetch ingredients from database
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    try:
        cur.execute(select_ingredients) # fetch all ingredients from table
        kitchen = cur.fetchall()
    finally:
        cur.close()
        conn.close()

    if not kitchen:
        return {"recipes": [], "message": "Oops - your kitchen is empty!"}
    kitchen_ingredients = [item["ingredient_name"] for item in kitchen]
    priority_ingredients = kitchen_ingredients[:3]

    # filters request body
    diet = data.get("diet")
    recipe_type = data.get("type")
    number = int(data.get("number", 10))

    # spoonacular API call
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
    "apiKey": SPOONACULAR_API_KEY,
    "ingredients": ",".join(priority_ingredients),  # top 3 expiring
    "number": number,
    "ranking": 2,
    "ignorePantry": True
    }

    r = requests.get(url, params=params, timeout=15)
    if r.status_code != 200:
        raise HTTPException(status_code=502, detail=f"Spoonacular error: {r.text}")

    candidates = r.json()

    # filtering so ingredients in generated recipes only contain ingredients user already has, excluding 'kitchen staples'
    kitchen_staples = {
        "salt", "pepper", "water", "oil", "olive oil", "butter"
    }

    def is_allowed_to_be_missing(missed_ingredients: list[dict]) -> bool:
        for ing in missed_ingredients:
            name = (ing.get("name") or "").strip().lower()
            if name not in kitchen_staples:
                return False
        return True

    pantry_only = [
        rec for rec in candidates
        if is_allowed_to_be_missing(rec.get("missedIngredients", []))
    ]

    return {
    "priority_ingredients": priority_ingredients,
    "recipes_found": len(candidates),
    "pantry_only_count": len(pantry_only),
    "example_missing": candidates[0].get("missedIngredients", []) if candidates else []
}
