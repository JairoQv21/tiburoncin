class Product:
    def __init__(self, product_id, name, description, price, category_id, stock):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id
        self.stock = stock

    def update_stock(self, quantity):
        # Implement stock update logic here
        self.stock += quantity
