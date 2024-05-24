class OrderDetails:
    def __init__(self, order_id, user_id, order_date, total, status):
        self.order_id = order_id
        self.user_id = user_id
        self.order_date = order_date
        self.total = total
        self.status = status

    def update_status(self, status):
        # Implement status update logic here
        self.status = status
