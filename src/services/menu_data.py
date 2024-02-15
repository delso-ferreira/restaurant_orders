import csv
from src.models.ingredient import Ingredient
from src.models.dish import Dish


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.ingredients = set()
        self.menu(source_path)

    def menu(self, source_path: str) -> None:
        with open(source_path, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                dish_name = row["dish"]
                dish_price = float(row["price"])
                ingredient_name = row["ingredient"]
                ingredient_amount = int(row["recipe_amount"])

                dish = next((
                    d for d in self.dishes if d.name == dish_name), None)
                if not dish:
                    dish = Dish(dish_name, dish_price)
                    self.dishes.add(dish)

                ingredient = next((
                    i for i in self.ingredients if i.name == ingredient_name),
                    None)
                if not ingredient:
                    ingredient = Ingredient(ingredient_name)
                    self.ingredients.add(ingredient)

            dish.add_ingredient_dependency(ingredient, ingredient_amount)


""" O que o next faz --> next(iterator, default)
https://docs.python.org/3/library/functions.html#next
 """

""" dictReader ->
https://docs.python.org/3/library/csv.html#csv.DictReader
"""
