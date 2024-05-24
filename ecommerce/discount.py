class Discount:
    def __init__(self, discount_id, code, percentage, expiry_date):
        self.discount_id = discount_id
        self.code = code
        self.percentage = percentage
        self.expiry_date = expiry_date

    def apply_discount(self, total):
        # Implement discount application logic here
        return total * (1 - self.percentage / 100)
