from product import Product
from supplier import Supplier


class DigitalProduct(Product):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        download_size: int,
        supplier: Supplier,
    ):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size: int = download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"*Download Size: {self.__download_size}MB")

    def get_fulfilment_info(self) -> str:
        return "Delievered digitally"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "DIGITAL"
        data["download_size"] = self.__download_size
        return data
