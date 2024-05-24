class ShoppingSession:
    def __init__(self, session_id, user_id, total):
        self.session_id = session_id
        self.user_id = user_id
        self.total = total

    def calculate_total(self, cart_items, products):
        # Calcular el total usando los precios de los productos
        self.total = sum(item.get_price(products) * item.quantity for item in cart_items)

