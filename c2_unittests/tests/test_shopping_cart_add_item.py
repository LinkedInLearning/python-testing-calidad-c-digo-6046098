from unittest import TestCase

from shopping_cart import ShoppingCart


class TestShoppingCartAddItem(TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    def tearDown(self):
        self.cart = None

    def test_add_new_item(self):
        result = self.cart.add_item("apple", 1.0, 2)
        self.assertEqual(result, "Item added")

    def test_add_item_zero_quantity(self):
        result = self.cart.add_item("apple", 1.0, 0)
        self.assertEqual(result, "Quantity must be greater than zero")
