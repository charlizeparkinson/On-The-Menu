CREATE DATABASE IF NOT EXISTS food_waste;

USE food_waste;

-- ingredients table
-- user inserts ingredients and this is where it is stored
-- ingredients that user currently owns
CREATE TABLE IF NOT EXISTS ingredients (
ingredient_id INT AUTO_INCREMENT PRIMARY KEY,
ingredient_name VARCHAR(250) NOT NULL UNIQUE,
ingredient_type ENUM(
    'Protein',
    'Carbohydrate',
    'Vegetable',
    'Fruit',
	'Dairy',
	'Seasoning',
	'Other',
	'Unknown'
) DEFAULT 'Unknown' NOT NULL,
ingredient_quantity DECIMAL(10,2) DEFAULT 0 NOT NULL,
unit_name VARCHAR(20) DEFAULT 'Unknown' NOT NULL,
expiration_date DATE NOT NULL,
date_added DATE NOT NULL DEFAULT (CURRENT_DATE)
);

-- recipes (library of recipe data)
CREATE TABLE IF NOT EXISTS recipes (
    recipe_id INT AUTO_INCREMENT PRIMARY KEY,
    api_recipe_id INT NOT NULL UNIQUE,
    recipe_name VARCHAR(250) NOT NULL,
    recipe_instructions TEXT NOT NULL,
    recipe_meal ENUM(
    'Breakfast',
    'Lunch',
    'Dinner',
    'Dessert',
    'Snack',
    'Other',
    'Unknown'
    ) DEFAULT 'Unknown' NOT NULL,
    recipe_type ENUM(
    'Meaty',
    'Vegetarian',
    'Vegan',
    'Dairy-Free',
    'Other',
    'Unknown'
    ) DEFAULT 'Unknown' NOT NULL,
    serving_size DECIMAL(10,2) DEFAULT 0 NOT NULL
);

-- recipe_ingredients 
CREATE TABLE IF NOT EXISTS recipe_ingredients (
    recipe_id INT NOT NULL,
    ingredient_name VARCHAR(250) NOT NULL,
    required_quantity DECIMAL(10,2) DEFAULT 0 NOT NULL,
    unit_name VARCHAR(20) DEFAULT 'Unknown' NOT NULL,
    PRIMARY KEY (recipe_id, ingredient_name),
    FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id) ON DELETE CASCADE
);

-- generated_recipes (this is temporary, and unless the user saves a recipe these recipes will be rewritten every time recipes are generated)
CREATE TABLE IF NOT EXISTS generated_recipes (
    recipe_id INT NOT NULL,
    PRIMARY KEY (recipe_id),
    FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id) ON DELETE CASCADE
);


-- saved_recipes - references the recipes table
CREATE TABLE IF NOT EXISTS saved_recipes (
  saved_recipe_id INT AUTO_INCREMENT PRIMARY KEY,
  recipe_id INT NOT NULL UNIQUE,
  date_saved DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id) ON DELETE CASCADE
);


