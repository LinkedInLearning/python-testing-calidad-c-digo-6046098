from freezegun import freeze_time
from unittest import TestCase
from unittest.mock import patch

from shopping_cart import ShoppingCart


class TestShoppingCartAddItem(TestCase):

    def setUp(self):
        self.cart = ShoppingCart()
        # self.cart.add_item("apple", 1.0, 2)
        # self.cart.add_item("banana", 0.5, 3)

    @freeze_time("2025-09-01")
    @patch("shopping_cart.ShoppingCart.get_total")
    def test_generate_receipt(self, mock_total):

        mock_total.return_value = 10
        receipt = self.cart.generate_receipt()

        self.assertEqual(receipt["subtotal"], 10)
        self.assertEqual(receipt["discount"], 0)
        self.assertEqual(receipt["total"], 10)
        mock_total.assert_called_once()

    @freeze_time("2025-09-03")
    @patch.object(ShoppingCart, "get_total", return_value=10)
    def test_generate_receipt_wednesday(self, mock_total):

        receipt = self.cart.generate_receipt()

        self.assertEqual(receipt["subtotal"], 10)
        self.assertEqual(receipt["discount"], 1.5)
        self.assertEqual(receipt["total"], 8.5)

        mock_total.assert_called_once()
