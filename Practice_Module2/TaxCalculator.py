class NumberReader:
    @staticmethod
    def non_negative_float(prompt: str) -> float:
        while True:
            s = input(prompt).strip()
            try:
                v = float(s)
            except ValueError:
                print("Invalid input. Enter a non-negative number.")
                continue

            if v >= 0:
                return v
            print("Invalid input. Enter a non-negative number.")


class ProgressiveTax:
    BRACKETS = [(10000, 0.00), (30000, 0.10), (100000, 0.20)]
    TOP_RATE = 0.30
    TOP_START = 100000

    @classmethod
    def compute(cls, income: float) -> float:
        tax = 0.0
        lower = 0

        for upper, rate in cls.BRACKETS:
            if income <= lower:
                break
            taxable = min(upper - lower, income - lower)
            tax += taxable * rate
            lower = upper

        if income > cls.TOP_START:
            tax += (income - cls.TOP_START) * cls.TOP_RATE

        return tax


class TaxCalculatorApp:
    def run(self) -> None:
        print("Tax Calculator (sample brackets)")
        income = NumberReader.non_negative_float("Enter annual income: ")
        tax = ProgressiveTax.compute(income)
        net = income - tax

        print(f"Gross income: {income:.2f} TL")
        print(f"Tax due: {tax:.2f} TL")
        print(f"Net income: {net:.2f} TL")


if __name__ == "__main__":
    TaxCalculatorApp().run()
