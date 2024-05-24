from datetime import datetime

class PaymentDetails:
    def __init__(self, id, order_id, payment_method, payment_amount):
        self.id = id
        self.order_id = order_id
        self.payment_method = payment_method
        self.payment_amount = payment_amount
        self.payment_date = datetime.now()
        self.order = None  # Relación uno a uno con OrderDetails
