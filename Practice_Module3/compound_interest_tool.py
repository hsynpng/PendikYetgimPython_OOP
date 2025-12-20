def ask_float(text):
    while True:
        raw = input(text).strip()
        try:
            num = float(raw)
        except ValueError:
            print("Geçersiz giriş. Sayı girin.")
            continue

        if num < 0:
            print("Negatif değer girilemez.")
            continue
        return num


def ask_pos_int(text):
    while True:
        raw = input(text).strip()
        try:
            num = int(raw)
        except ValueError:
            print("Geçersiz giriş. Tam sayı girin.")
            continue

        if num <= 0:
            print("Pozitif bir tam sayı girin.")
            continue
        return num


def run():
    print("Bileşik Faiz Hesaplayıcı")
    principal = ask_float("Ana para (TL): ")
    annual_rate = ask_float("Yıllık faiz oranı (%): ")
    years = ask_pos_int("Yıl sayısı: ")

    total = principal
    print("\nYıl sonu bakiyeleri:")
    for year in range(1, years + 1):
        total *= (1 + annual_rate / 100)
        print(f"Yıl {year}: {total:.2f} TL")

    print(f"Toplam: {total:.2f} TL (Başlangıç: {principal:.2f} TL, Faiz: {annual_rate}%)")


if __name__ == "__main__":
    run()
