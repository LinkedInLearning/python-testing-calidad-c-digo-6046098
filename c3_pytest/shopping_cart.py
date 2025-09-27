from datetime import datetime


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity):
        if quantity <= 0:
            return "Quantity must be greater than zero"

        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {
                'price': price, 'quantity': quantity
            }
        return "Item added"

    def get_total(self):
        total = 0
        for item in self.items.values():
            total += item['price'] * item['quantity']
        return total

    def generate_receipt(self):
        now = datetime.now()
        total = self.get_total()
        weekday = now.weekday()  # Monday=0, Sunday=6
        discount = 0
        discount_rate = 0
        if weekday == 2:  # Wednesday
            discount_rate = 0.15
            discount = total * discount_rate
        grand_total = total - discount
        items_list = []
        for name, info in self.items.items():
            items_list.append({
                'name': name,
                'quantity': info['quantity'],
                'price': info['price'],
                'subtotal': info['quantity'] * info['price']
            })
        receipt = {
            'datetime': now.isoformat(),
            'weekday': now.strftime('%A'),
            'items': items_list,
            'subtotal': total,
            'discount_rate': discount_rate,
            'discount': discount,
            'total': grand_total
        }
        return receipt
