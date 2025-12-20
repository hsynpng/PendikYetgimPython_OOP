import random


def ask_int(text, lo=1, hi=1000):
    while True:
        raw = input(text).strip()
        try:
            val = int(raw)
        except ValueError:
            print("Geçersiz giriş. Tam sayı girin.")
            continue

        if val < lo or val > hi:
            print(f"{lo}-{hi} arasında bir sayı girin.")
            continue
        return val


def run():
    print("Çarpma Testi")
    total_q = ask_int("Kaç soru olsun? ", 1, 100)

    ok = 0
    for idx in range(1, total_q + 1):
        x = random.randint(1, 12)
        y = random.randint(1, 12)
        correct = x * y

        try:
            user_ans = int(input(f"Soru {idx}: {x} x {y} = ").strip())
        except ValueError:
            print("Geçersiz giriş, yanlış sayıldı.")
            continue

        if user_ans == correct:
            print("Doğru!")
            ok += 1
        else:
            print(f"Yanlış. Doğru cevap: {correct}")

    rate = (ok * 100 / total_q) if total_q else 0
    print(f"Bitti. Doğru: {ok}/{total_q} (%{rate:.1f})")


if __name__ == "__main__":
    run()
