from src.models.ingredient import Ingredient
from src.models.ingredient import Restriction


def test_ingredient():

    ingredient1 = Ingredient('queijo mussarela')
    ingredient2 = Ingredient('queijo provolone')
    assert ingredient1 != ingredient2

    ingredient1 = Ingredient('queijo mussarela')
    ingredient2 = Ingredient('queijo mussarela')
    assert hash(ingredient1) == hash(ingredient2)

    ingredient1 = Ingredient('queijo mussarela')
    ingredient2 = Ingredient('queijo mussarela')
    assert ingredient1 == ingredient2

    ingredient1 = Ingredient('queijo mussarela')
    ingredient2 = Ingredient('queijo provolone')
    assert not ingredient1 == ingredient2

    ingredient1 = Ingredient("queijo mussarela")
    assert ingredient1.name == "queijo mussarela"
    assert ingredient1.restrictions == {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED
    }

    ingredient1 = Ingredient("queijo mussarela")
    assert repr(ingredient1) == "Ingredient('queijo mussarela')"

    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo provolone")
    assert not hash(ingredient1) == hash(ingredient2)

    ingredient1 = Ingredient("queijo mussarela")
    assert ingredient1.restrictions != {Restriction.GLUTEN}
