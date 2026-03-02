def show_menu():
    print("Taco Palace Menu")
    print("1. Taco       $3.50")
    print("2. Burrito    $4.99")
    print("3. Nachos     $5.25")
    print("4. Soft Drink $1.95")
    print("5. Quit")


def get_price(choice):
    prices = {1: 3.50, 2: 4.99, 3: 5.25, 4: 1.95}
    return prices.get(choice, 0)


# Main program to present options to customer
print("Welcome to Taco Palace! ...")
order = []  # list of item names
total = 0.0

while True:
    show_menu()
    try:
        choice = int(input("Enter your selection (1-5): "))
    except:
        print("Please enter a number.")
        continue

    if choice == 5:
        break
    elif 1 <= choice <= 4:
        items = ["Taco", "Burrito", "Nachos", "Soft Drink"]
        item_name = items[choice - 1]
        price = get_price(choice)

        print(f"You selected {item_name}")
        order.append(item_name)
        total += price
    else:
        print("Invalid choice. Try again.")

# Final output to customer
if order:
    print("\nYou ordered:", ", ".join(order))
    print(f"Your total ${total:.2f}")
else:
    print("You ordered nothing. Goodbye!")