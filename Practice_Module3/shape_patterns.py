def ask_int(text, lo=1, hi=50):
    while True:
        raw = input(text).strip()
        try:
            val = int(raw)
        except ValueError:
            print("Geçersiz giriş. Tam sayı girin.")
            continue

        if val < lo or val > hi:
            print(f"{lo}-{hi} arasında olmalı.")
            continue
        return val


def draw_triangle(n):
    for k in range(1, n + 1):
        print("*" * k)


def draw_pyramid(n):
    for row in range(n):
        pad = " " * (n - row - 1)
        stars = "* " * (row + 1)
        print(pad + stars)


def draw_square(n):
    for _ in range(n):
        print("* " * n)


def run():
    print("Desen Oluşturucu")
    print("1) Sağ üçgen")
    print("2) Piramit")
    print("3) Kare")
    mode = ask_int("Seçim (1-3): ", 1, 3)
    size = ask_int("Boyut (1-50): ", 1, 50)
    print()

    if mode == 1:
        draw_triangle(size)
    elif mode == 2:
        draw_pyramid(size)
    else:
        draw_square(size)


if __name__ == "__main__":
    run()
