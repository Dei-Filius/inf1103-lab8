from product import Product
from can_be_shipped import CanBeShipped
from supplier import Supplier

SHIPPING_RATE = 4.0


class PhysicalProduct(Product, CanBeShipped):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        weight: float,
        supplier: Supplier,
    ):
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight: float = weight

    def display_information(self) -> None:
        super().display_information()
        print(f"*Weight: {self.__weight}kg")

    def calculate_shipping_cost(self) -> float:
        return self.__weight * SHIPPING_RATE

    def get_fulfilment_info(self) -> str:
        return "Require physical shipping"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "PHYSICAL"
        data["weight"] = self.__weight
        return data
