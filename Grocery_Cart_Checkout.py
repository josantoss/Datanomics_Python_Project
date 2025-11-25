# Predefined dictionary of groceries with prices
groceries = {
    "apple": 10.0,
    "banana": 8.5,
    "milk": 25.0,
    "bread": 20.0,
    "egg": 2.5,
    "rice": 15.0,
    "coffee": 40.0
}
cart = {}  # Empty cart dictionary
print("Welcome to the Grocery Store!")
print("Available items and prices:")
for item, price in groceries.items():
    print(f" - {item.capitalize()}: {price} birr")
print("\nType the name of the item to add it to your cart.")
print('Type "checkout" when you are done.\n')
while True:
    item = input("Enter item name: ").lower()
    if item == "checkout":
        break
    if item not in groceries:
        print("Item not found. Please try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {item}: "))
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue
    except ValueError:
        print("Please enter a valid number for quantity.")
        continue
    # Add or update item in cart
    if item in cart:
        cart[item] += quantity
    else:
        cart[item] = quantity
    print(f"Added {quantity} {item}(s) to your cart.\n")
# Checkout summary
print("\n Final Bill:")
print("-" * 30)
total = 0
for item, quantity in cart.items():
    price = groceries[item]
    subtotal = price * quantity
    total += subtotal
    print(f"{item.capitalize():10} x {quantity:<3} = {subtotal:.2f} birr")
print("-" * 30)
print(f"Total: {total:.2f} birr")
print("Thank you for shopping with us! ")