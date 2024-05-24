from dwdwdwd.categoriaProducto import ProductCategory
from dwdwdwd.productoDescuento import ProductDiscount
from dwdwdwd.productoInventario import ProductInventory
from datetime import datetime

class Product:
    def __init__(self, id_product, name, SKU, category_id, inventory_id, price, discount_id, created_at=None, modified_at=None, deleted_at=None):
        self.id_product = id_product
        self.name = name
        self.SKU = SKU
        self.category_id = category_id
        self.inventory_id = inventory_id
        self.price = price
        self.discount_id = discount_id
        self.created_at = created_at or datetime.now()
        self.modified_at = modified_at
        self.deleted_at = deleted_at

if __name__ == '__main__':
    # Example usage
    product = Product(
        id_product=1,
        name="Example Product",
        SKU="EX123",
        category_id=ProductCategory.id_category,
        inventory_id=ProductInventory.id_inventory,
        price=19.99,
        discount_id=ProductDiscount.id_discount
    )
