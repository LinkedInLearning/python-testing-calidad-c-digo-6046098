import pytest

from shopping_cart import ShoppingCart


@pytest.fixture
def cart():
    #Setup
    cart_intance = ShoppingCart()
    print("Setup: ShoppingCart created")
    yield cart_intance

    #Teardown
    print("Teardown: ShoppingCart test finished")


def test_add_item_quantity_zero(cart):
    response = cart.add_item("Apple", 1.0, 0)
    assert response == "Quantity must be greater than zero"


def test_add_new_item():
    cart = ShoppingCart()
    response = cart.add_item("Banana", 0.5, 1)
    assert response == "Item added"
    assert cart.items["Banana"] == {"price": 0.5, "quantity": 1}


def test_add_existing_item():
    cart = ShoppingCart()
    cart.items = {"Orange": {"price": 0.8, "quantity":2}}
    assert cart.items["Orange"] == {"price": 0.8, "quantity":2}

    response = cart.add_item("Orange", 0.8, 3)
    assert response == "Item added"
    assert cart.items["Orange"] == {"price": 0.8, "quantity":5}


@pytest.mark.parametrize(
    "name, price, quantity, expected",
    [
        ("Apple", 1.0, 0, "Quantity must be greater than zero"),
        ("Banana", 0.5, 1, "Item added")
    ]
)
def test_add_item_parametrized(cart, name, price, quantity, expected):
    response = cart.add_item(name, price, quantity)
    assert response == expected
