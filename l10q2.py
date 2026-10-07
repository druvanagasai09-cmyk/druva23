def final_price(price, discount=10) :
    discount_amount = price * discount / 100
    return price - discount_amount

price = float(input("enter product price:"))

print("price with default 10% discount:", final_price(price))

discount = float(input("enter the discount percentage:"))
print("price with entered discount:", final_price(price, discount))