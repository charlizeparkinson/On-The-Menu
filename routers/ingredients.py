from fastapi import APIRouter, Body, HTTPException
from database.db_utils import get_connection
from database.CRUD.ingredients import select_ingredients, insert_ingredient, update_ingredient, delete_ingredient
from mysql.connector.errors import IntegrityError, DatabaseError

router = APIRouter()

# read all ingredients in the table
@router.get("/ingredients")
def get_ingredients_endpoint():
        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        cur.execute(select_ingredients)
        rows = cur.fetchall()

        cur.close()
        conn.close()
        return {"ingredients": rows}

# insert ingredient/s into table
@router.post("/ingredients", status_code=201)
def add_ingredient_endpoint(data: dict = Body(...)):
    conn = get_connection()
    cur = conn.cursor()

    try:
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

        return {"message": "Ingredient added to the database successfully"}

    except IntegrityError as e:
        conn.rollback()
        if getattr(e, "errno", None) == 1062: # mysql duplicate entry error code
            raise HTTPException(status_code=409, detail="This ingredient name already exists")
        raise HTTPException(status_code=400, detail="Invalid data")

    except DatabaseError:
        conn.rollback()
        raise HTTPException(status_code=500, detail="Database error")

    finally:
        cur.close()
        conn.close()

# delete ingredient endpoint
@router.delete("/ingredients/{ingredient_id}")
def delete_ingredient_endpoint(ingredient_id: int):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(delete_ingredient, (ingredient_id,))
        conn.commit()

        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Ingredient not found")
        return {"message": "Ingredient deleted successfully"}

    except DatabaseError:
        conn.rollback()
        raise HTTPException(status_code=500, detail="Database error")

    finally:
        cur.close()
        conn.close()

# updating ingredients
@router.put("/ingredients/{ingredient_id}")
def update_ingredient_endpoint(ingredient_id: int, data: dict = Body(...)):
    conn = get_connection()
    cur = conn.cursor()

    try:
        name = (data.get("ingredient_name") or "").strip().lower()
        if not name:
            raise HTTPException(status_code=400, detail="ingredient_name is required")

        ingredient_type = data.get("ingredient_type", "Unknown")
        quantity = data.get("ingredient_quantity", 0)
        unit_name = (data.get("unit_name") or "Unknown").strip()
        expiration_date = data.get("expiration_date")
        if not expiration_date:
            raise HTTPException(status_code=400, detail="expiration_date is required")

        cur.execute(
            update_ingredient,
            (
                name,
                ingredient_type,
                quantity,
                unit_name,
                expiration_date,
                ingredient_id
            )
        )

        conn.commit()

        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Ingredient not found")

        return {"message": "Ingredient updated successfully"}

    except IntegrityError as e:
        conn.rollback()
        if getattr(e, "errno", None) == 1062:
            raise HTTPException(status_code=409, detail="This ingredient name already exists")
        raise HTTPException(status_code=400, detail="Invalid data")

    except DatabaseError:
        conn.rollback()
        raise HTTPException(status_code=500, detail="Database error")

    finally:
        cur.close()
        conn.close()
