from fastapi import APIRouter
from database.db_utils import get_connection
from fastapi import Body
from database.CRUD.ingredients import select_ingredients
from database.CRUD.ingredients import insert_ingredient

router = APIRouter()

# read all ingredients in the table
@router.get("/ingredients")
def get_ingredients():
        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        cur.execute(select_ingredients)
        rows = cur.fetchall()

        cur.close()
        conn.close()
        return {"ingredients": rows}

# insert ingredient/s into table

@router.post("/ingredients", status_code=201)
def create_ingredient(data: dict = Body(...)):
    conn = get_connection()
    cur = conn.cursor()

    name = (data.get("ingredient_name") or "").strip().lower()
    ingredient_type = data.get("ingredient_type", "Unknown")
    quantity = data.get("ingredient_quantity", 0)
    unit_name = (data.get("unit_name") or "Unknown").strip()
    expiration_date = data.get("expiration_date")

    cur.execute(
        insert_ingredient,
        (name, ingredient_type, quantity, unit_name, expiration_date)
    )

    conn.commit()

    cur.close()
    conn.close()

    return {"message": "Ingredient added to the database successfully"}
