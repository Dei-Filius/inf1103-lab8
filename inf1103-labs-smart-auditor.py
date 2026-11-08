import json
from pathlib import Path
from typing import Literal
import re

from digital_product import DigitalProduct
from inventory import Inventory
from physical_product import PhysicalProduct
from supplier import Supplier

INVENTORY_FILE_PATH: str = "data/inventory.json"
inventory_file: Path = Path(INVENTORY_FILE_PATH)


def load_inventory() -> Inventory:
    print()
    print("Loading inventory...")
    inventory = Inventory()
    try:
        with inventory_file.open("r") as file:
            for product_info in json.load(file):
                supplier_info = product_info["supplier"]
                supplier = Supplier(
                    supplier_info["id"],
                    supplier_info["name"],
                    supplier_info["contact_email"],
                )
                match product_info["type"]:
                    case "PHYSICAL":
                        product = PhysicalProduct(
                            product_info["id"],
                            product_info["name"],
                            product_info["price"],
                            product_info["stock"],
                            product_info["weight"],
                            supplier,
                        )
                    case "DIGITAL":
                        product = DigitalProduct(
                            product_info["id"],
                            product_info["name"],
                            product_info["price"],
                            product_info["stock"],
                            product_info["download_size"],
                            supplier,
                        )
                    case _:
                        raise ValueError("Unknown product type.")
                inventory.add_product(product)
    except FileNotFoundError:
        inventory_file.parent.mkdir(parents=True, exist_ok=True)
        inventory_file.touch()
    except (json.JSONDecodeError, ValueError):
        print("Inventory file might be corrupted.")
        print("Exiting...")
        exit()
    return inventory


def save_inventory(inventory: Inventory) -> None:
    print()
    print("Saving inventory...")
    with inventory_file.open("w") as file:
        json.dump(inventory.to_list(), file, indent=4)
    print("Inventory saved successfully to", INVENTORY_FILE_PATH)


def add_product(inventory: Inventory) -> None:
    print()
    print("Add New Product")
    product_id = get_product_id_input()

    if inventory.find_product(product_id):
        print("Product already exists.")
        return

    name = get_str_input("Product Name: ").strip()
    price = get_price_input("Price (omit $ sign): ")
    stock = get_int_input("Stock Quantity: ", 0)
    product_type = get_product_type_input()
    supplier_id = get_supplier_id_input()
    supplier_name = get_str_input("Supplier Name: ")
    supplier_contact_email = get_email_input("Supplier Contact Email: ")

    supplier = Supplier(supplier_id, supplier_name, supplier_contact_email)

    match product_type:
        case "PHYSICAL":
            weight = get_int_input("Product Weight(kg): ", 0)
            product = PhysicalProduct(product_id, name, price, stock, weight, supplier)
        case "DIGITAL":
            download_size = get_int_input("Product Downlaod Size(MB): ", 0)
            product = DigitalProduct(
                product_id, name, price, stock, download_size, supplier
            )
        case _:
            raise ValueError("Unknown product type.")
    inventory.add_product(product)
    print("Product added successfully!")


def update_stock(inventory: Inventory) -> None:
    print()
    print("Update Stock")
    product_id = get_product_id_input()
    product = inventory.find_product(product_id)

    if product is None:
        print("This Product is not in Inventory.")
        return

    print("Product Found!")
    print("------------------------------------------------")
    product.display_information()
    print("------------------------------------------------")

    stock = get_int_input("New Stock Quantity: ", 0)
    product.update_stock(stock)

    print()
    print("Product Updated!")
    print("------------------------------------------------")
    product.display_information()
    print("------------------------------------------------")


def find_product(inventory: Inventory) -> None:
    print()
    product_id = get_product_id_input()
    product = inventory.find_product(product_id)
    if product is None:
        print("This Product is not in Inventory.")
        return

    print("Product Found!")
    print("------------------------------------------------")
    product.display_information()
    print("------------------------------------------------")


def exit_app(inventory: Inventory):
    save_inventory(inventory)
    print()
    print("Thank you for using Inventory Management System.")
    print("Program terminated.")
    exit()


def get_str_input(msg: str) -> str:
    """
    Get non-empty string from user
    """
    while True:
        user_input = input(msg)
        if user_input:
            return user_input
        print("Invalid. Input is empty. Try again.")


def get_int_input(msg: str, minimum=None, maximum=None) -> int:
    """
    get int from user within min max value.
    """
    while True:
        try:
            user_input = int(input(msg))
            if minimum is not None:
                if user_input < minimum:
                    raise ValueError()
            if maximum is not None:
                if user_input > maximum:
                    raise ValueError()
            return user_input
        except ValueError:
            print("Invalid. Try again.")


def get_price_input(msg: str) -> float:
    """
    Get valid price from user, price >=0
    """
    while True:
        try:
            user_input = round(float(input(msg)), 2)
            if user_input < 0:
                raise ValueError()
            return user_input
        except ValueError:
            print("Invalid. Try again.")


def get_product_id_input() -> str:
    """
    Get valid Product ID from user, starts with P then followed by digits.
    """
    while True:
        try:
            user_input = input("Product ID (Pxxx): ").strip().upper()
            if not (user_input.startswith("P") or user_input[1:].isdigit()):
                raise ValueError()
            return user_input
        except ValueError:
            print("Invalid Product ID. Try again.")


def get_supplier_id_input() -> str:
    """
    Get valid Supplier ID from user, starts with S then followed by digits.
    """
    while True:
        try:
            user_input = input("Supplier ID (Sxxx): ").strip().upper()
            if not (user_input.startswith("S") or user_input[1:].isdigit()):
                raise ValueError()
            return user_input
        except ValueError:
            print("Invalid Supplier ID. Try again.")


def get_email_input(msg: str) -> str:
    """
    Get valid email
    """
    while True:
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        email = input(msg).strip().upper()
        if re.fullmatch(pattern, email) is None:
            print("Invalid email")
        else:
            return email


def get_product_type_input() -> Literal["PHYSICAL", "DIGITAL"]:
    """
    Get valid Product type from user.
    """
    while True:
        try:
            user_input = input("Product Type: ").strip().upper()
            if user_input not in ["PHYSICAL", "DIGITAL"]:
                raise ValueError()
            return user_input
        except ValueError:
            print("Invalid Product ID. Try again.")


def display_menu(menu: list[dict]) -> None:
    print()
    print("----------- MENU -----------")
    for i, page in enumerate(menu, 1):
        print(f"{i}. {page["text"]}")
    print("----------------------------")


def main() -> None:
    try:
        inventory: Inventory = load_inventory()

        menu: list[dict] = [
            {"text": "Exit", "action": lambda: exit_app(inventory)},
            {"text": "Display All Products", "action": lambda: inventory.display_all()},
            {"text": "Add Product", "action": lambda: add_product(inventory)},
            {"text": "Update Stock", "action": lambda: update_stock(inventory)},
            {"text": "Search Product", "action": lambda: find_product(inventory)},
            {"text": "Save Inventory", "action": lambda: save_inventory(inventory)},
        ]

        print("""
========================================
INVENTORY MANAGEMENT SYSTEM
========================================
        """)
        while True:
            try:
                display_menu(menu)
                option = get_int_input("Enter option: ", 0, len(menu) - 1)
                try:
                    menu[option]["action"]()
                except KeyboardInterrupt:
                    continue
            except KeyboardInterrupt:
                exit_app(inventory)
                break

    except json.decoder.JSONDecodeError:
        print(f"Error decoding json file {INVENTORY_FILE_PATH}")
        print("Exiting...")
    except KeyboardInterrupt:
        print("Exiting...")


if __name__ == "__main__":
    main()
