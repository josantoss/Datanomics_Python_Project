# Project 2: Intro to Programming with Python Project
# Q1. Vending Machine Program
# Build a program that:
# Displays a list of snacks and drinks with item numbers and prices.
# Asks the user to choose items by number in a loop.
# Keeps track of selected items and their prices.
# Ends when the user types “done”.
# Finally prints a receipt showing:
# List of selected items with prices
# Total cost
# Skills practiced: loops, input(), conditionals, lists/dictionaries, sum(), print formatting

# List of snacks and drinks with prices
menu = {
    1: {"item": "Chiko", "price": 35.00},
    2: {"item": "Fetira", "price": 22.50},
    3: {"item": "Samosa", "price": 12.50},
    4: {"item": "Doughnut", "price": 12.50},
    5: {"item": "Coffee", "price": 15.00},
    6: {"item": "Water 0.5 Litter", "price": 20.00},
    7: {"item": "Tea", "price": 10.50},
}

selected_items = []
total_cost = 0.0
# Display the items
print("Welcome to the Snack and Drink Shop!")
print("Here's our menu:")
for item_number, details in menu.items():
    print(f"{item_number}. {details['item']} - ${details['price']:.2f}")

while True:
    choice = input("Enter the item number to add to your order, or type 'done' to finish: ").lower()

    if choice == 'done':
        break

    try:
        item_number = int(choice)
        if item_number in menu:
            item_details = menu[item_number]
            selected_items.append(item_details)
            total_cost += item_details['price']
            print(f"{item_details['item']} added to your order.")
        else:
            print("Invalid item number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter an item number or 'done'.")

print("\n--- Your Receipt ---")
if not selected_items:
    print("No items were selected.")
else:
    for item in selected_items:
        print(f"{item['item']} - ${item['price']:.2f}")
    print(f"Total: ${total_cost:.2f}")
print("Thank you for choosing us!")
