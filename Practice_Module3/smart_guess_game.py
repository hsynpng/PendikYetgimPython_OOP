import random
import math


def ask_int(text, lo=None, hi=None):
    while True:
        raw = input(text).strip()
        try:
            val = int(raw)
        except ValueError:
            print("Hatalı giriş. Tam sayı girin.")
            continue

        if lo is not None and val < lo:
            print(f"En az {lo} olmalı.")
            continue
        if hi is not None and val > hi:
            print(f"En fazla {hi} olmalı.")
            continue
        return val


def run():
    print("Gelişmiş Sayı Tahmin Oyunu")
    start = ask_int("Minimum değer (örn: 1): ")
    end = ask_int("Maksimum değer (örn: 100): ", start + 1)

    target = random.randint(start, end)
    limit = max(5, int(math.log2(end - start + 1)) + 3)

    tries = 0
    points = 100
    left, right = start, end
    penalty = max(1, int(100 / limit))

    while tries < limit:
        print(f"Hak: {limit - tries} | Aralık: [{left}, {right}] | Puan: {points}")
        pick = ask_int("Tahmin: ", left, right)
        tries += 1

        if pick == target:
            print(f"Tebrikler! {tries}. denemede bildin. Puanın: {points}")
            return

        if pick < target:
            print("Daha büyük dene.")
            left = max(left, pick + 1)
        else:
            print("Daha küçük dene.")
            right = min(right, pick - 1)

        points -= penalty

    print(f"Bitti. Doğru sayı: {target}. Puanın: {points}")


if __name__ == "__main__":
    run()
