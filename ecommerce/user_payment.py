class UserPayment:
    def __init__(self, payment_id, user_id, payment_type, provider, account_no, expiry):
        self.payment_id = payment_id
        self.user_id = user_id
        self.payment_type = payment_type
        self.provider = provider
        self.account_no = account_no
        self.expiry = expiry

    def process_payment(self, amount):
        # Implement payment processing logic here
        pass
