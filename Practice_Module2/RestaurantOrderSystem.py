class MenuCatalog:
    ITEMS = {
        1: ("Adana Kebab", 120.0),
        2: ("Lahmacun", 25.0),
        3: ("Iskender", 95.0),
        4: ("Salad", 30.0),
        5: ("Ayran", 8.0),
    }

    @classmethod
    def display(cls) -> None:
        print("Menu:")
        for k, (name, price) in cls.ITEMS.items():
            print(f"{k}) {name} - {price:.2f} TL")
        print("0) Finish order")

    @classmethod
    def exists(cls, item_id: int) -> bool:
        return item_id in cls.ITEMS

    @classmethod
    def get(cls, item_id: int):
        return cls.ITEMS[item_id]


class ConsoleInput:
    @staticmethod
    def read_int(prompt: str) -> int:
        while True:
            s = input(prompt).strip()
            try:
                return int(s)
            except ValueError:
                print("Invalid input. Enter an integer.")


class OrderCart:
    def __init__(self):
        self.lines = {}

    def add(self, item_id: int, qty: int) -> None:
        self.lines[item_id] = self.lines.get(item_id, 0) + qty

    def is_empty(self) -> bool:
        return len(self.lines) == 0

    def print_summary(self) -> None:
        total = 0.0
        print("\nOrder Summary:")
        for item_id in sorted(self.lines):
            qty = self.lines[item_id]
            name, price = MenuCatalog.get(item_id)
            line_total = price * qty
            total += line_total
            print(f"- {name} x{qty} = {line_total:.2f} TL")
        print(f"Total: {total:.2f} TL")


class RestaurantOrderApp:
    def run(self) -> None:
        print("Restaurant Order System")
        cart = OrderCart()

        while True:
            MenuCatalog.display()
            choice = ConsoleInput.read_int("Choose item id: ")
            if choice == 0:
                break
            if not MenuCatalog.exists(choice):
                print("Invalid item id.")
                continue

            qty = ConsoleInput.read_int("Quantity: ")
            if qty <= 0:
                print("Quantity must be positive.")
                continue

            cart.add(choice, qty)

        if cart.is_empty():
            print("No items selected.")
            return

        cart.print_summary()


if __name__ == "__main__":
    RestaurantOrderApp().run()
