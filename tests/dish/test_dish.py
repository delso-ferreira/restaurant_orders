from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
import pytest


def test_dish():
    dish = Dish("Presunto", 10.0)
    assert dish.name == "Presunto"
    assert dish.price == 10.0

    equal_dish = Dish("Presunto", 10.0)
    assert hash(dish) == hash(equal_dish)
    assert dish == equal_dish

    nonequal_dish = Dish("Risoto", 50.0)
    assert hash(dish) != hash(nonequal_dish)
    assert dish != nonequal_dish

    repr_dish = "Dish('Presunto', R$10.00)"
    assert repr(dish) == repr_dish

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Presunto", "1")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Risoto", 0.0)

    dish.add_ingredient_dependency(Ingredient("creme de leite"), 1)
    dish.add_ingredient_dependency(Ingredient("camarão"), 1)
    assert dish.get_ingredients() == {
        Ingredient("creme de leite"),
        Ingredient("camarão"),
    }

    assert dish.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.LACTOSE,
    }
