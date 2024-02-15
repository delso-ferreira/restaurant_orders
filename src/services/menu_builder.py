from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData
from src.models.ingredient import Restriction

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=Restriction) -> List[Dict]:
        main_menu = []
        dishes = self.menu_data.dishes
        
        for dish in dishes:
            if restriction is None or not dish.get_restrictions().intersection(restriction):
                dict_menu = {
                    "name": dish.name,
                    "price": dish.price,
                    "ingredients": [ ingredient for ingredient in dish.get_ingredients() ],
                    "price": dish.price,
                    "restrictions": [ restriction for restriction in dish.get_restrictions() ]
                }

                if restriction is not None:
                    dict_menu["restrictions"] = list(dish.get_restrictions().intersection(restriction))

                main_menu.append(dict_menu)
            return main_menu    
