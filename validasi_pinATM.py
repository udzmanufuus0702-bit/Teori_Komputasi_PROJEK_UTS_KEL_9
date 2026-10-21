def validasi_pin(pin):
    # State awal
    state = 0

    # DFA membaca setiap karakter PIN
    for karakter in pin:
        if state < 6 and karakter.isdigit():
            state += 1
        else:
            return False

    # Diterima jika tepat 6 digit
    return state == 6


# Program utama
if __name__ == "__main__":
    pin = input("Masukkan PIN ATM: ")
    if validasi_pin(pin):
        print("PIN valid!")
    else:
        print("PIN tidak valid! PIN harus 6 digit angka.")