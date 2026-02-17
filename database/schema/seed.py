from database.db_utils import get_connection

seed_data = [
    ("milk", "Dairy", 2, "litres", "2026-02-20"),
    ("chicken breast", "Protein", 500, "grams", "2026-02-18"),
    ("rice", "Carbohydrate", 1, "kg", "2026-06-01"),
    ("spinach", "Vegetable", 150, "grams", "2026-02-17"),
    ("tomatoes", "Vegetable", 500, "grams", "2026-02-19"),
    ("eggs", "Protein", 12, "pieces", "2026-02-25"),
    ("yogurt", "Dairy", 750, "ml", "2026-02-16"),
    ("garlic", "Seasoning", 3, "cloves", "2026-03-10"),
    ("onions", "Vegetable", 5, "pieces", "2026-03-01"),
    ("cheddar cheese", "Dairy", 350, "grams", "2026-02-22"),
]

insert_sql = """
INSERT INTO ingredients
(ingredient_name, ingredient_type, ingredient_quantity, unit_name, expiration_date)
VALUES (%s, %s, %s, %s, %s)
"""

def run_seed():
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("TRUNCATE TABLE ingredients")

        for item in seed_data:
            cur.execute(insert_sql, item)

        conn.commit()
        print("Database truncated and seed data inserted successfully.")

    except Exception as e:
        conn.rollback()
        print("Error inserting seed data:", e)

    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    run_seed()

