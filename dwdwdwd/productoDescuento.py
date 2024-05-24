from datetime import date, time

class ProductDiscount:
    id_discount = int
    name = str
    discount_percent = float
    activetimestamp = date, time
    created_at = date, time
    modified_at = date, time 
    deleted_at = date, time
    