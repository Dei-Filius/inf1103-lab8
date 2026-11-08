from abc import ABC, abstractmethod
from supplier import Supplier


class Product(ABC):
    """
    Abstract Product Class.
    """

    def __init__(
        self, product_id: str, name: str, price: float, stock: int, supplier: Supplier
    ) -> None:
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock
        self.supplier: Supplier = supplier

    def update_stock(self, stock: int) -> None:
        if stock < 0:
            raise ValueError("stock cannot be negative")

        self.__stock = stock

    def display_information(self) -> None:
        print(f"ID: {self.__product_id}", end=" | ")
        print(f"Name: {self.__name}", end=" | ")
        print(f"Price: ${self.__price:.2f}", end=" | ")
        print(f"Stock: {self.__stock}")
        self.supplier.display_information()

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

    def to_dict(self) -> dict:
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.supplier.to_dict(),
        }

    @property
    def product_id(self) -> str:
        return self.__product_id

    @property
    def price(self) -> float:
        return self.__price
