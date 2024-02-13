from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    dish1 = Dish('pizza', 50.0)
    dish2 = Dish('Lasanha', 40.0)
    assert dish1.name != dish2.name
    assert dish1 != dish2

    Dish(dish1)
    assert hash(dish1) == hash(dish1)

    Dish(dish1)
    Dish(dish2)
    assert hash(dish1) != hash(dish2)

    Dish(dish1)
    assert dish1.name == 'pizza'
    assert dish1.price == 50.0

    Dish(dish1)
    assert repr(dish1) == "Dish('pizza', R$50.00)"

    with pytest.raises(TypeError):
        Dish('pizza', '20')

    with pytest.raises(ValueError):
        Dish('pizza', 300)

    Dish(dish1).add_ingredient_dependency(Ingredient('queijo mussarela'), 1)
    Dish(dish1).add_ingredient_dependency(Ingredient('farinha'), 1)
    assert dish1.recipe.get(Ingredient('queijo mussarela')) == 1
    assert dish1.recipe.get(Ingredient('farinha')) == 1

    assert dish1.get_restrictions() == {
        Restriction.LACTOSE, Restriction.GLUTEN, Restriction.ANIMAL_DERIVED
    }
