total_amount = 0
total_discount = 0
most_expensive = None
cheapest = None
highest_quantity = None

print("Enter details for 5 products")

for i in range(1, 6):
    product_id = input(f"\nProduct {i} ID: ")
    name = input("Product name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    amount = price * quantity

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "quantity": quantity,
    }

    if most_expensive is None or price > most_expensive["price"]:
        most_expensive = product
    if cheapest is None or price < cheapest["price"]:
        cheapest = product
    if highest_quantity is None or quantity > highest_quantity["quantity"]:
        highest_quantity = product

    if amount > 5000:
        discount_rate = 10
    elif amount >= 3000:
        discount_rate = 5
    else:
        discount_rate = 0

    discount = amount * discount_rate / 100
    final_amount = amount - discount

    print("\nProduct Details")
    print(f"ID: {product_id}")
    print(f"Name: {name}")
    print(f"Price: {price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Amount: {amount:.2f}")
    print(f"Discount: {discount_rate}%")
    print(f"Discount Amount: {discount:.2f}")
    print(f"Final Price: {final_amount:.2f}")

    total_amount += final_amount
    total_discount += discount

print("\n-----------------------------")
print(f"Total Discount: {total_discount:.2f}")
print(f"Total Bill: {total_amount:.2f}")
print("-----------------------------")
print(f"Most Expensive Product: {most_expensive['name']} ({most_expensive['price']:.2f})")
print(f"Cheapest Product: {cheapest['name']} ({cheapest['price']:.2f})")
print(
    f"Highest Quantity Purchased: "
    f"{highest_quantity['name']} ({highest_quantity['quantity']})"
)
