class CartItem:
    def __init__(self, cart_item_id, session_id, product_id, quantity):
        self.cart_item_id = cart_item_id
        self.session_id = session_id
        self.product_id = product_id
        self.quantity = quantity

    def get_price(self, products):
        # Buscar el producto por ID y devolver su precio
        for product in products:
            if product.product_id == self.product_id:
                return product.price
        return 0

