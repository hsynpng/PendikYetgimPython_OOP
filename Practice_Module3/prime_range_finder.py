import math


def ask_int(text):
    while True:
        raw = input(text).strip()
        try:
            return int(raw)
        except ValueError:
            print("Geçersiz giriş. Bir tam sayı girin.")


def list_primes(x, y):
    lo = min(x, y)
    hi = max(x, y)

    if hi < 2:
        return []

    lo = max(2, lo)
    flag = [True] * (hi + 1)
    flag[0] = False
    flag[1] = False

    for p in range(2, int(math.isqrt(hi)) + 1):
        if flag[p]:
            step_start = p * p
            for m in range(step_start, hi + 1, p):
                flag[m] = False

    return [n for n in range(lo, hi + 1) if flag[n]]


def run():
    print("Asal Sayı Aralığı Bulucu")
    a = ask_int("Başlangıç: ")
    b = ask_int("Bitiş: ")

    arr = list_primes(a, b)
    if arr:
        print(f"{a} ve {b} arası asal sayılar:")
        print(", ".join(str(n) for n in arr))
    else:
        print("Bu aralıkta asal sayı yok.")


if __name__ == "__main__":
    run()
