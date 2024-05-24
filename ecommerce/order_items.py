class OrderItems:
    def __init__(self, order_item_id, order_id, product_id, quantity, price):
        self.order_item_id = order_item_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    def calculate_total_price(self):
        # Implement total price calculation logic here
        return self.quantity * self.price
