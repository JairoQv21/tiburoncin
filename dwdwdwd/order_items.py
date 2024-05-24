from dwdwdwd.producto import Product

class OrderItems:
    def __init__(self, id, order_id, product_id, product_name, quantity, price):
        self.id = id
        self.order_id = order_id
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.order = None  # Relación muchos a uno con OrderDetails
