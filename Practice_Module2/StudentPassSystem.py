class ScoreReader:
    @staticmethod
    def read(prompt: str):
        while True:
            s = input(prompt).strip()
            if s == "":
                return None
            try:
                v = float(s)
            except ValueError:
                print("Invalid score. Enter a number (e.g., 85.5).")
                continue

            if 0 <= v <= 100:
                return v
            print("Score must be between 0 and 100.")


class GradePolicy:
    @staticmethod
    def letter(avg: float) -> str:
        if avg >= 90:
            return "A"
        if avg >= 80:
            return "B"
        if avg >= 70:
            return "C"
        if avg >= 60:
            return "D"
        return "F"

    @staticmethod
    def passed(avg: float) -> bool:
        return avg >= 60


class StudentPassApp:
    def run(self) -> None:
        print("Student Pass System")
        print("Enter scores (0-100). Press Enter on empty input to finish.")

        scores = []
        while True:
            val = ScoreReader.read("Score (empty = finish): ")
            if val is None:
                break
            scores.append(val)

        if not scores:
            print("No scores entered.")
            return

        avg = sum(scores) / len(scores)
        letter = GradePolicy.letter(avg)
        status = "Passed" if GradePolicy.passed(avg) else "Failed"

        print(f"Count: {len(scores)}")
        print(f"Average: {avg:.2f}")
        print(f"Letter Grade: {letter}")
        print(f"Result: {status}")


if __name__ == "__main__":
    StudentPassApp().run()
