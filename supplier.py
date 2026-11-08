class Supplier:
    def __init__(self, supplier_id: str, name: str, email: str) -> None:
        self.__supplier_id = supplier_id
        self.__name = name
        self.__contact_email = email

    def display_information(self) -> None:
        print(f"Supplier ID: {self.__supplier_id}", end=" | ")
        print(f"Name: {self.__name}", end=" | ")
        print(f"Email: ${self.__contact_email}")

    def to_dict(self) -> dict:
        return {
            "id": self.__supplier_id,
            "name": self.__name,
            "contact_email": self.__contact_email,
        }
