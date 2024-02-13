from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    dish1 = Dish('pizza', 50.0)
    assert dish1.name == 'pizza'
    assert dish1.price == 50.0

    dish1_comp = Dish('pizza', 50.0)
    assert hash(dish1) == hash(dish1_comp)
    assert dish1 == dish1_comp

    dish2 = Dish('Lasanha', 40.0)
    assert hash(dish1) != hash(dish2)
    assert dish1 != dish2


    Dish(dish1)
    Dish(dish2)
    assert dish1.name != dish2.name
    

    Dish(dish1)
    assert hash(dish1) == hash(dish1)

    Dish(dish1)
    assert repr(dish1) == "Dish('pizza', R$50.00)"

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish('pizza', '1111')

    with pytest.raises(ValueError, match="Dish price must be greater then zero."):
        Dish('pizza', 0)

    Dish(dish1).add_ingredient_dependency(Ingredient('queijo mussarela'), 1)
    Dish(dish1).add_ingredient_dependency(Ingredient('farinha'), 1)
    assert dish1.recipe.get(Ingredient('queijo mussarela')) == 1
    assert dish1.recipe.get(Ingredient('farinha')) == 1

    assert dish1.get_restrictions() == {
        Restriction.LACTOSE, Restriction.GLUTEN, Restriction.ANIMAL_DERIVED
    }
