# main.py
# main.py
from ecommerce.user_payment import UserPayment
from ecommerce.user_address import UserAddress
from ecommerce.payment_details import PaymentDetails
from ecommerce.cart_item import CartItem
from ecommerce.shopping_session import ShoppingSession
from ecommerce.product_inventory import ProductInventory
from ecommerce.discount import Discount
from ecommerce.order_items import OrderItems
from ecommerce.order_details import OrderDetails
from ecommerce.user import User
from ecommerce.product_category import ProductCategory
from ecommerce.product import Product

def main():
    # Crear usuarios
    user = User(user_id=1, name="John Doe", email="john@example.com", password="securepassword")

    # Autenticar usuario
    if user.authenticate("securepassword"):
        print("Usuario autenticado")
    
    # Crear dirección de usuario
    address = UserAddress(address_id=1, user_id=user.user_id, street="123 Main St", city="Anytown", state="Anystate", postal_code="12345", country="USA")
    address.validate_address()

    # Crear una categoría de producto
    category = ProductCategory(category_id=1, name="Electronics", description="Electronic gadgets and devices")
    category.update_category(name="Updated Electronics", description="Updated description")

    # Crear un producto
    product = Product(product_id=1, name="Smartphone", description="Latest model smartphone", price=699.99, category_id=category.category_id, stock=50)
    products = [product]  # Lista de productos disponibles

    # Crear una sesión de compras
    session = ShoppingSession(session_id=1, user_id=user.user_id, total=0.0)
    
    # Añadir un ítem al carrito
    cart_item = CartItem(cart_item_id=1, session_id=session.session_id, product_id=product.product_id, quantity=2)
    cart_items = [cart_item]  # Lista de ítems en el carrito
    
    # Crear inventario de productos
    inventory = ProductInventory(inventory_id=1, product_id=product.product_id, quantity=50)
    inventory.update_stock(-2)  # Reducir stock después de añadir al carrito

    # Calcular total de la sesión de compras
    session.calculate_total(cart_items, products)
    print(f"Total de la sesión de compras: {session.total}")

    # Aplicar un descuento
    discount = Discount(discount_id=1, code="DISCOUNT10", percentage=10, expiry_date="2024-12-31")
    discounted_total = discount.apply_discount(session.total)
    print(f"Total después de aplicar descuento: {discounted_total}")

    # Procesar pago
    payment = UserPayment(payment_id=1, user_id=user.user_id, payment_type="Credit Card", provider="Visa", account_no="1234567890", expiry="12/24")
    payment.process_payment(discounted_total)
    
    # Crear detalles del pago
    payment_details = PaymentDetails(detail_id=1, order_id=1, payment_id=payment.payment_id, amount=discounted_total, date="2024-05-24")
    payment_details.confirm_payment()
    
    # Crear orden de detalles
    order_details = OrderDetails(order_id=1, user_id=user.user_id, order_date="2024-05-24", total=discounted_total, status="Pending")
    order_details.update_status("Completed")
    
    # Crear ítems de la orden
    order_item = OrderItems(order_item_id=1, order_id=order_details.order_id, product_id=product.product_id, quantity=cart_item.quantity, price=cart_item.get_price(products))
    total_price = order_item.calculate_total_price() * cart_item.quantity  # Multiplicar por la cantidad
    print(f"Total del ítem de la orden: {total_price}")


if __name__ == "__main__":
    main()
