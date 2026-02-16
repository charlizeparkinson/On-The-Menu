"""
THE PLAN:

INGREDIENTS TABLE CRUD
- INSERT INGREDIENT
- UPDATE INGREDIENT DETAILS
- DELETE INGREDIENT

"""

# validation and normalisation of the input before insert statement execution

# execution of the insert statement
insert_ingredient = """
INSERT INTO ingredients
    (ingredient_name, ingredient_type, ingredient_quantity, unit_name, expiration_date)
VALUES
    (%s, %s, %s, %s, %s)
"""