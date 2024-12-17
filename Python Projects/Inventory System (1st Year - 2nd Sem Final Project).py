
from datetime import datetime
import os

categories = ['CPU', 'GPU', 'COOLER', 'RAM', 'MOTHERBOARD', 'CASE', 'STORAGE', 'PSU']

inventory_files = {
    'CPU': "CPU Inventory",
    'GPU': "GPU Inventory",
    'COOLER': "Cooler Inventory",
    'RAM': "RAM Inventory",
    'MOTHERBOARD': "Motherboard Inventory",
    'CASE': "Case Inventory",
    'STORAGE': "Storage Inventory",
    'PSU': "PSU Inventory"
}

keywords = ['Added', 'Deleted', 'Edited', 'Viewed', 'Opened', 'Closed']

def add_product():
    print("==================================================\n")
    print(f"Enter [00] if you'd like to exit.")
    name = input("Product Name: ").upper()

    if name == '00':
        return

    id = input("Item ID: ").upper()

    if id == '00':
        return

    while True:
        category = input("Category: ").upper()

        if category == "00":
            return

        if category in categories:
            break
        else:
            print("\nPlease determine if it's a CPU, GPU, Cooler, RAM, Motherboard\n"
                  "Case, Storage, or PSU. Any other input is invalid.")

    quantity = input("Quantity: ")

    if quantity == '00':
        return

    quantity = int(quantity)

    filename = inventory_files[category]

    id_check = False
    new_lines = []

    if os.path.exists(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

        for line in lines:
            parts = line.strip().split(' - ')
            if parts[0] == id:
                part = parts[-1].split()
                current_quantity = int(part[1])
                new_quantity = current_quantity + quantity
                part[1] = f"{new_quantity}"
                updated = ' '.join(part)
                parts[-1] = f'{updated}'
                line = ' - '.join(parts) + '\n'
                id_check = True
            new_lines.append(line)

    if not id_check:
        addlog = datetime.now()
        formatted = addlog.strftime("%m-%d-%Y %I:%M:%S %p")
        new_lines.append(f"{id} - {name} - {category}: {quantity} | Added on: {formatted}\n")

    with open(filename, 'w') as file:
        file.writelines(new_lines)

    with open('Record Logs', 'a') as eggnog:
        eggnog.writelines(f'{formatted} - Added Product: [{id} - {name} - {category}]\n')

    print("\nProduct Added Successfully!\n")
    print("\n==================================================\n")



def edit_product_quantity():

    print("==================================================\n")
    while True:
        print(f"Enter [00] if you'd like to exit.")
        category = input("Enter Category: ").upper()

        if category == "00":
            return

        if category in categories:
            break
        else:
            print("\nPlease determine if it's a CPU, GPU, Cooler, RAM, Motherboard\n"
                  "Case, Storage, or PSU. Any other input is invalid.")

    filename = inventory_files[category]

    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        print("No product has been added yet! Please add one first.")
        return

    with open(filename, 'r') as file:
        lines = file.readlines()

    while True:
        id = input("Enter Product ID: ").upper()
        updated = False

        if id == "00":
            return

        new_lines = []
        for line in lines:
            parts = line.strip().split(" - ")
            part = parts[-1].split()
            if parts[0] == id:
                currquan = int(part[1].split()[0])
                prevquan = currquan
                while True:
                    new_quantity = input("Enter New Quantity: ")
                    if new_quantity.isdigit():
                        new_quantity = int(new_quantity)
                        break
                    else:
                        print("Please enter a valid integer for the quantity.")
                part[1] = str(new_quantity)
                linya = " ".join(part)
                parts[-1] = linya
                line = " - ".join(parts) + "\n"
                updated = True
            new_lines.append(line)

        if not updated:
            print(f"\nProduct ID '{id}' does not exist. Please try again.\n")
        else:
            with open(filename, 'w') as file:
                file.writelines(new_lines)

            addlog = datetime.now()
            formatted = addlog.strftime("%m-%d-%Y %I:%M:%S %p")

            with open('Record Logs', 'a') as eggnog:
                eggnog.writelines(f'{formatted} - Edited Product: [{id}-{category}] quantity to: {new_quantity} from {prevquan}\n')

            print(f"\nQuantity for Product ID: '{id}' updated successfully!\n")
            break
        print("==================================================\n")

def del_product():

    print("==================================================\n")
    while True:
        print(f"Enter [00] if you'd like to exit.")
        category = input("Enter Category: ").upper()

        if category == "00":
            return

        if category in categories:
            break
        else:
            print("\nPlease determine if it's a CPU, GPU, Cooler, RAM, Motherboard\n"
                  "Case, Storage, or PSU. Any other input is invalid.")


    file_name = inventory_files.get(category)

    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        print("No products have been added yet!")
        return

    with open(file_name, 'r') as file:
        lines = file.readlines()

    while True:
        item_id = input("Enter Item ID: ").upper().strip()

        if item_id == "00":
            return

        update = False

        with open(file_name, 'w') as file:
            for line in lines:
                content = line.strip().split(" - ")
                if content[0].strip().upper() == item_id:
                    print(f"\nDeleting {item_id}...")
                    update = True
                else:
                    file.write(line)

        if not update:
            print(f'\n{item_id} does not exist. Please try again.\n')
        else:
            addlog = datetime.now()
            formatted = addlog.strftime("%m-%d-%Y %I:%M:%S %p")

            with open('Record Logs', 'a') as eggnog:
                eggnog.writelines(
                    f'{formatted} - Deleted Product: [{item_id}-{category}]\n')
            print("\nProduct deleted successfully!\n")
            break

        print("==================================================\n")


def view_inventory():

    addlog = datetime.now()
    formatted = addlog.strftime("%m-%d-%Y %I:%M:%S %p")

    print("==================================================\n")
    print("Search by: \n")
    print("1.) View All")
    print("2.) Search by Category\n")
    print(f"Enter [00] if you'd like to exit.")
    choice = int(input("Enter your choice: "))

    if choice == 00:
        return

    elif choice == 1:
        print("==================================================\n")

        with open('Record Logs', 'a') as eggnog:
            eggnog.writelines(f'{formatted} - Viewed Inventory by: "View All"\n')

        for category, file_name in inventory_files.items():
            print(f"Category: {category}")
            print("Item ID - Name - Class - Quantity\n")
            if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
                with open(file_name, 'r') as file:
                    print(file.read())

            else:
                print("No products in inventory.")
            print()

            print("==================================================\n")

    elif choice == 2:
        while True:
            category = input("Enter Category: ").upper()

            if category == '00':
                return

            if category in categories:
                break
            else:
                print("\nPlease determine if it's a CPU, GPU, Cooler, RAM, Motherboard\n"
                      "Case, Storage, or PSU. Any other input is invalid.")

        filename = inventory_files[category]

        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            print("\n==================================================\n")
            print("No product has been added yet! Please add one first.\n")
            return

        with open(filename, 'r') as file:
            print("==================================================\n")
            print(f"Category: {category}")
            print("Item ID - Name - Class - Quantity\n")
            print(file.read())

        with open('Record Logs', 'a') as eggnog:
            eggnog.writelines(f'{formatted} - Viewed Inventory by: "Search by Category"\n')



def item_availability():

    print("\n==================================================\n")
    while True:
        print(f"Enter [00] if you'd like to exit.")
        category = input("Enter Category: ").upper()

        if category == "00":
            return

        if category in categories:
            break
        else:
            print("\nPlease determine if it's a CPU, GPU, Cooler, RAM, Motherboard\n"
                  "Case, Storage, or PSU. Any other input is invalid.")

    filename = inventory_files[category]

    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        print("\nNo product has been added yet! Please add one first.")
        return

    with open(filename, 'r') as file:
        lines = file.readlines()

    while True:
        id = input("Enter Item ID: ").upper().strip()

        if id == '00':
            return

        light = False

        for line in lines:
            parts = line.strip().split(" - ")
            part = parts[-1].split()
            if parts[0] == id:
                print("\n==================================================\n")
                print(f'Category: {category}\n')
                print("\t  Name\t\t\t\t Quantity\n")
                print(f"{parts[1]} \t\t\t{part[1]}\n")
                light = True
                break

        if not light:
            print("\n==================================================\n")
            print("This ID does not exist! Please try again.")
            print("\n==================================================\n")
        else:
            break

    addlog = datetime.now()
    formatted = addlog.strftime("%m-%d-%Y %I:%M:%S %p")

    with open('Record Logs', 'a') as eggnog:
        eggnog.writelines(f'{formatted} - Checked item availability of: {id}\n')


def logrecords():

    addlog = datetime.now()
    formatted = addlog.strftime("%m-%d-%Y %I:%M:%S %p")

    print("\n==================================================\n")
    print(f"Enter [00] if you'd like to exit.")
    print("How would you like to view the Record Logs?\n")
    print('1.) View All')
    print('2.) View by Keyword\n')

    choice = input("Enter your choice: ")

    if choice == '00':
        return

    elif choice == '1':
        print("\n==================================================\n")
        with open('Record Logs', 'r') as eggnog:
            lines = eggnog.readlines()

        for line in lines:
            print(line.strip())

    elif choice == '2':
        while True:
            print("\n==================================================\n")
            keys = input("Enter keyword: ").capitalize()

            if keys == '00':
                return

            if keys in keywords:
                print("\n==================================================\n")
                with open('Record Logs', 'r') as eggnog:
                    lines = eggnog.readlines()

                for line in lines:
                    if keys in line:
                        print(line.strip())
                print()
                break

            else:
                print("Please enter a valid keyword!\n"
                    "[Added, Deleted, Edited, Viewed, Opened, Closed]")

    with open('Record Logs', 'a') as eggnog:
        eggnog.writelines(f'{formatted} - Viewed Log Records\n')

def main():

    key = "cybertech123"

    addlog = datetime.now()
    formatted = addlog.strftime("%m-%d-%Y %I:%M:%S %p")

    with open('Record Logs', 'a') as eggnog:
        eggnog.writelines(f'{formatted} - System Opened/Started\n')

    print("==================================================")
    print("\nWelcome to CyberTech PC's Inventory System!")
    print("Please input master key to continue...\n\n")

    while True:
        entry = input("Master Key: ")
        print("\n==================================================\n")

        if entry != key:
            print("Key Incorrect! Please try again.\n")
            continue
        else:
            break

    while True:
        print("==================================================")
        print("\nMain Menu: ")
        print("\t1.) Add Product")
        print("\t2.) Edit Product Quantity")
        print("\t3.) Delete Product")
        print("\t4.) View Inventory")
        print("\t5.) Check Item Availability")
        print("\t6.) View Records")
        print("\t7.) Exit")

        try:
            print('\nWARNING: PLEASE REFRAIN FROM ENTERING THE VALUE [00], AS THIS EXITS THE PROGRAM. THANK YOU!')
            choice = int(input("\nEnter Your Choice (1-7): "))
            if choice < 1 or choice > 7:
                print("Please Enter Numbers 1-7 Only.")
            else:
                print(f"\nYou selected option {choice}.\n")

                match choice:
                    case 1:
                        add_product()
                    case 2:
                        edit_product_quantity()
                    case 3:
                        del_product()
                    case 4:
                        view_inventory()
                    case 5:
                        item_availability()
                    case 6:
                        logrecords()
                    case 7:
                        print("\nThank you for using the system!\n")
                        print("==================================================")

                        addlogs = datetime.now()
                        formatteds = addlogs.strftime("%m-%d-%Y %I:%M:%S %p")

                        with open('Record Logs', 'a') as eggnog:
                            eggnog.writelines(f'{formatteds} - System Closed/Exited\n')

                        exit()

        except ValueError:
            print("Invalid input! Please enter a number.")

        print("==================================================\n")

main()

