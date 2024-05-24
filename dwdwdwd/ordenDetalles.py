from datetime import datetime
from dwdwdwd.ordenDetalles import OrderDetails
from dwdwdwd.pago_detalles import PaymentDetails

class OrderDetails:
    def __init__(self, id, user_id, status):
        self.id = id
        self.user_id = user_id
        self.order_date = datetime.now()
        self.status = status
        self.items = []  # Lista de OrderItems
        self.payment = None  # Relación uno a uno con PaymentDetails

    def add_item(self, item):
        self.items.append(item)
        item.order = self

    def set_payment(self, payment):
        self.payment = payment
        payment.order = self
