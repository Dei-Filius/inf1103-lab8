from digital_product import DigitalProduct
from inventory import Inventory
from order import Order
from physical_product import PhysicalProduct
from product import Product
from supplier import Supplier

# 2.2
# Deleting a variable to a supplier object only removes that variable's
# reference. The object still exists. Each Product object is still able to
# retrieve the supplier object becuase they still hold a reference regardless of
# that deleted variable.

print("\n===TEST 2.2===")
supplier1 = Supplier("S1", "S1", "S@S1.sg")
phy_prod = PhysicalProduct("P001", "p1", 1.0, 100, 5, supplier1)
digi_prod = DigitalProduct("P002", "p2", 1.0, 100, 5, supplier1)

del supplier1

phy_prod.display_information()
print()
digi_prod.display_information()


# 3.2
# Product objects still "work" after removal from the Inventory because only a
# reference to the Product object is stored in Inventory.

print("\n===TEST 3.2===")
inventory = Inventory()
inventory.add_product(phy_prod)
inventory.remove_product(phy_prod.product_id)

try:
    phy_prod.display_information()
    print("\nTest passed, product still works.")
except Exception as err:
    print("\nTest failed.")
    print(err)


# 4.3
# Assuming "add the same Product" means the same Product object, then there
# should still be 1. Since each Order object will instantiation their own
# OrderLine, then there will be 2 OrderLine objects.

print("\n===TEST 4.3===")
order1 = Order("O1")
order1.add_order_line(phy_prod, 1)
order1.add_order_line(digi_prod, 1)
order1.display()

order2 = Order("O2")
order2.add_order_line(phy_prod, 1)
order2.add_order_line(digi_prod, 1)
order2.display()

order1.remove_order_line(1)
order1.display()

order2.remove_order_line(2)
order2.display()


# 6.2
print("\n===TEST 6.2===")


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


show_product_details(phy_prod)
print()
show_product_details(digi_prod)

try:
    show_product_details(phy_prod)
    print()
    show_product_details(digi_prod)
    print("\nTest passed, function accepts both Physical and Digital.")
except Exception as err:
    print("\nTest failed.")
    print(err)

# 6.3
# One expectation that Product class establishes is that all product has a
# get_fulfilment_info() method which is defined as a abstract method.
#
# Yes the code snippet violates LSP as valid inputs to the parent Product class's
# implementation would raise an error in the DigitalProduct subclass. Given the
# fact that stock of digital products have no meaning, stock attribute should
# behave like weight attribute which is defined in PhysicalProduct class and not
# in Product class. This of course gives rise to the need for type checking
# before users can update the stock of a Product. However this check is done
# outside of the Inventory class's perview.


# 7.2
# Behaves as indented. Only 1 loop and no product type checking.

print("\n===TEST 7.2===")

inventory2 = Inventory()
inventory2.add_product(phy_prod)
inventory2.add_product(digi_prod)
inventory2.display_all()

# 7.3
# Polymorphism is demonstrated because the 2 different classes PhydicalProduct 
# and DigitalProduct are able to be treated as 1 common based class. Although 
# treated as a common Product class they still displayed different information 
# unique to their own class. 
# LSP supports this becuase it enforces child classes to maintain the same
# expectations of the parent class. This makes it safe and predictable. 
