import random


class ChoiceParser:
    MAP = {
        "r": "rock",
        "p": "paper",
        "s": "scissors",
        "rock": "rock",
        "paper": "paper",
        "scissors": "scissors",
    }

    @classmethod
    def read(cls, prompt: str) -> str:
        while True:
            s = input(prompt).strip().lower()
            if s in cls.MAP:
                return cls.MAP[s]
            print("Invalid choice. Use r/p/s or rock/paper/scissors.")


class RpsRules:
    WINS = {("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")}

    @classmethod
    def outcome(cls, player: str, comp: str) -> int:
        if player == comp:
            return 0
        return 1 if (player, comp) in cls.WINS else -1


class RoundConfig:
    @staticmethod
    def read_best_of() -> int:
        s = input("Number of rounds (odd, e.g., 3): ").strip()
        try:
            n = int(s)
        except ValueError:
            n = 3
        if n <= 0:
            n = 3
        if n % 2 == 0:
            n += 1
        return n


class RockPaperScissorsGame:
    def run(self) -> None:
        print("Rock-Paper-Scissors")
        rounds = RoundConfig.read_best_of()
        needed = rounds // 2 + 1

        p_score = 0
        c_score = 0

        for i in range(1, rounds + 1):
            print(f"--- Round {i} ---")
            player = ChoiceParser.read("Your choice (r/p/s): ")
            comp = random.choice(("rock", "paper", "scissors"))
            print(f"Computer: {comp}")

            res = RpsRules.outcome(player, comp)
            if res == 0:
                print("Draw")
            elif res == 1:
                print("You win")
                p_score += 1
            else:
                print("You lose")
                c_score += 1

            if p_score == needed or c_score == needed:
                break

        print(f"Final: You {p_score} - Computer {c_score}")
        if p_score > c_score:
            print("Match won!")
        elif p_score < c_score:
            print("Match lost.")
        else:
            print("Match drawn.")


if __name__ == "__main__":
    RockPaperScissorsGame().run()
