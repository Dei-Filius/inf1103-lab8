from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

# 2.2 
# Deleting a variable to a supplier object only removes that variable's 
# reference. The object still exists. Each Product object is still able to 
# retrieve the supplier object becuase they still hold a reference regardless of
# that deleted variable.

supplier1 = Supplier("S1", "S1", "S@S1.sg")
phy_prod = PhysicalProduct("P001", "p1", 1.0, 1, 5, supplier1)
digi_prod = DigitalProduct("P001", "p1", 1.0, 1, 5, supplier1)

phy_prod.display_information()
digi_prod.display_information()

# 3.2
# Product objects still "work" after removal from the Inventory because only a 
# reference to the Product object is stored in Inventory.

# 4.3
# Assuming "add the same Product" means the same Product object, then there 
# should still be 1. Since each Order object will instantiation their own 
# OrderLine, then there will be 2 OrderLine objects.

# 6.3
# Yes this violates LSP as valid inputs to the parent Product class's 
# implementation would raise an error in the DigitalProduct subclass. Given the
# fact that stock of digital products have no meaning, stock attribute should 
# behave like weight attribute which is defined in PhysicalProduct class and not
# in Product class. This of course gives rise to the need for type checking 
# before users can update the stock of a Product. However this check is done 
# outside of the Inventory class's perview. 

# 7.2
# Behaves as indented. Only 1 loop and no product type checking.