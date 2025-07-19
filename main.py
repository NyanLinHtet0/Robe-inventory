from item import Item
from inventory import inventory
from item_manager import Item_manager


def input_item():
    id = input("Enter item ID (e.g., 0101): ")
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    fees = float(input("Enter item fees: "))
    quantity = int(input("Enter quantity: "))
    date = input("Enter date (e.g., MM/DD/YYYY): ")
    return Item(id, name, price, fees, quantity, date)

def input_sale():
    id = input("Enter item ID to sell: ")
    price = float(input("Enter selling price per item: "))
    quantity = int(input("Enter quantity to sell: "))
    date = input("Enter date of sale (e.g., MM/DD/YYYY): ")
    return id, price, quantity, date

def main():
    inven = inventory()
    item = Item(300 , 30, 2, '01/14/2024')
    item2 = Item(500 , 50, 2, '01/15/2024')
    inven.add_item("0101", "Malaysia", item)
    inven.add_item("0101", "Malaysia",item2)
    inven.sell_item("0101",1000, 4, "02/14/2024")
    while True:
        print("\n=== Inventory Menu ===")
        print("1. Add item")
        print("2. Sell item")
        print("3. View inventory")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            item = input_item()
            inven.add_item(item)
            print("Item added.")

        elif choice == '2':
            id, price, quantity, date = input_sale()
            inven.sell_item(id, price, quantity, date)
            print("Sale attempted.")

        elif choice == '3':
            print("\n=== Inventory ===")
            try:
                inven.print()
            except KeyError:
                print("Inventory is empty or no items in '01'-'01' category.")

        elif choice == '4':
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
