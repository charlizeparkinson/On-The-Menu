from fastapi import APIRouter
from database.db_utils import get_connection
from database.CRUD.ingredients import select_ingredients

router = APIRouter()

@router.get("/ingredients")
def get_ingredients():
        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        cur.execute(select_ingredients)
        rows = cur.fetchall()

        cur.close()
        conn.close()
        return {"ingredients": rows}
