import pytest

from shopping_cart import ShoppingCart


@pytest.fixture
def cart():
    cart_instance = ShoppingCart()
    cart_instance.items = {"Apple": {'price': 1.0, 'quantity': 2}}
    return cart_instance


def test_get_total(cart):
    total = cart.get_total()
    assert total == 2.0
