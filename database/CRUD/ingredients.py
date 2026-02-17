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

# update ingredient statement
update_ingredient = """
UPDATE ingredients
SET
  ingredient_name = %s,
  ingredient_type = %s,
  ingredient_quantity = %s,
  unit_name = %s,
  expiration_date = %s
WHERE ingredient_id = %s
"""

# delete ingredient execution
delete_ingredient = """
DELETE FROM ingredients
WHERE ingredient_id = %s
"""

# select ingredients - if 2 or more ingredients expire on the same date, order them via their id number in asc order
select_ingredients = """
SELECT * FROM ingredients
ORDER BY expiration_date ASC, ingredient_id ASC;
"""