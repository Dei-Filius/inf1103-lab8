from order_line import OrderLine
from product import Product


class Order:
    def __init__(self, order_id: str) -> None:
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def calulate_total(self) -> float:
        return sum(order_line.calculate_subtotal() for order_line in self.order_lines)

    def display(self) -> None:
        print()
        print(f"Order {self.order_id}")
        print("------------------------------------------------")
        for idx, order_line in enumerate(self.order_lines, 1):
            print(f"{idx}) Quantity: {order_line.quantity}")
            order_line.product.display_information()
            print()
        print("------------------------------------------------")
        print(f"Total: ${self.calulate_total()}")
        print("------------------------------------------------")


    def remove_order_line(self, line_num: int) -> None:
        self.order_lines.pop(line_num - 1)
