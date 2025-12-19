class InputSanitizer:
    @staticmethod
    def digits_only(prompt: str) -> str:
        while True:
            s = input(prompt).strip().replace(" ", "")
            if not s:
                print("Empty input. Try again.")
                continue
            if not s.isdigit():
                print("Digits only (spaces allowed).")
                continue
            return s


class LuhnValidator:
    @staticmethod
    def is_valid(number: str) -> bool:
        total = 0
        for i, ch in enumerate(reversed(number)):
            d = ord(ch) - 48
            if i % 2 == 1:
                d *= 2
                if d > 9:
                    d -= 9
            total += d
        return total % 10 == 0


class CardVerificationApp:
    def run(self) -> None:
        print("Luhn Card Verification")
        num = InputSanitizer.digits_only("Enter card number (spaces allowed): ")
        print("Valid (Luhn)" if LuhnValidator.is_valid(num) else "Invalid (Luhn)")


if __name__ == "__main__":
    CardVerificationApp().run()
