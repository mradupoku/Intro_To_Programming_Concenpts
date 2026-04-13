class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class VendingMachine:
    def __init__(self):
        # Initializing the 6 required beverages
        self.inventory = [
            Beverage("Water", 1.00),
            Beverage("Cola", 1.50),
            Beverage("Orange Juice", 2.00),
            Beverage("Iced Tea", 1.75),
            Beverage("Coffee", 2.25),
            Beverage("Sparkling Water", 1.25)
        ]

    def display_menu(self):
        print("\n--- Vending Machine Menu ---")
        for i, item in enumerate(self.inventory, 1):
            print(f"{i}. {item.name} - ${item.price:.2f}")
        print("0. Exit (Admin Only)")

    def start(self):
        while True:
            self.display_menu()
            try:
                choice = int(input("\nSelect a beverage number: "))

                if choice == 0:
                    print("Shutting down...")
                    break

                if 1 <= choice <= len(self.inventory):
                    selected_item = self.inventory[choice - 1]
                    self.process_transaction(selected_item)
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def process_transaction(self, item):
        print(f"You selected {item.name}. The price is ${item.price:.2f}.")

        try:
            money_inserted = float(input("Insert money: $"))

            if money_inserted >= item.price:
                change = money_inserted - item.price
                print(f"Vending {item.name}...")
                if change > 0:
                    print(f"Dispensing change: ${change:.2f}")
                print("Enjoy your drink!")
            else:
                shortfall = item.price - money_inserted
                print(f"Insufficient funds. You need ${shortfall:.2f} more. Transaction cancelled.")
        except ValueError:
            print("Invalid payment amount. Transaction cancelled.")


# Running the simulation
if __name__ == "__main__":
    machine = VendingMachine()
    machine.start()
