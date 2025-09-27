import freezegun
import pytest

from shopping_cart import ShoppingCart


@pytest.fixture
def cart():
    cart_instance = ShoppingCart()
    cart_instance.items = {"Apple": {'price': 1.0, 'quantity': 2}}
    yield cart_instance


@freezegun.freeze_time("2025-09-01")
def test_generate_receipt_no_discount(cart, mocker):
    mocker.patch.object(cart, "get_total", return_value=10)

    receipt = cart.generate_receipt()

    assert receipt['subtotal'] == 10
    assert receipt['discount'] == 0
    assert receipt['total'] == 10
    assert receipt['discount_rate'] == 0


@freezegun.freeze_time("2025-09-03")
def test_generate_receipt_with_discount(cart, mocker):
    mocker.patch.object(cart, "get_total", return_value=10)

    receipt = cart.generate_receipt()

    assert receipt['subtotal'] == 10
    assert receipt['discount'] == 1.5
    assert receipt['total'] == 8.5
    assert receipt['discount_rate'] == 0.15
