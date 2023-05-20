# Initialize product prices and quantities
product_prices = {"Product A": 20, "Product B": 40, "Product C": 50}
product_quantities = {}

# Ask for quantity and gift wrapping information for each product
for product in product_prices:
    quantity = int(input(f"Enter the quantity of {product}: "))
    product_quantities[product] = quantity
    gift_wrapping = input(f"Is {product} wrapped as a gift? (yes/no): ")

# Calculate subtotal
subtotal = sum(product_prices[product] * product_quantities[product] for product in product_prices)

# Apply discounts
discount_name = ""
discount_amount = 0

if subtotal > 200:
    discount_name = "flat_10_discount"
    discount_amount = 10
elif any(product_quantities[product] > 10 for product in product_prices):
    discount_name = "bulk_5_discount"
    discount_amount = min(product_prices[product] * product_quantities[product] * 0.05 for product in product_prices)
elif sum(product_quantities.values()) > 20:
    discount_name = "bulk_10_discount"
    discount_amount = subtotal * 0.1
elif sum(product_quantities.values()) > 30 and any(product_quantities[product] > 15 for product in product_prices):
    discount_name = "tiered_50_discount"
    discount_amount = sum(
        (product_quantities[product] - 15) * product_prices[product] * 0.5
        for product in product_prices
        if product_quantities[product] > 15
    )

# Calculate gift wrap fee
gift_wrap_fee = sum(product_quantities[product] for product in product_quantities) * 1

# Calculate shipping fee
shipping_fee = (sum(product_quantities.values()) - 1) // 10 * 5 + 5

# Calculate total
total = subtotal - discount_amount + gift_wrap_fee + shipping_fee

# Output the details
print("Product Details:")
for product in product_prices:
    print(f"{product}: Quantity - {product_quantities[product]}, Total - {product_prices[product] * product_quantities[product]}")
print(f"Subtotal: {subtotal}")
print(f"Discount Applied: {discount_name}, Amount: {discount_amount}")
print(f"Gift Wrap Fee: {gift_wrap_fee}")
print(f"Shipping Fee: {shipping_fee}")
print(f"Total: {total}")