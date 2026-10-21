# PROGRAM UTAMA VALIDASI AUTOMATA (DFA)

from validasi_email import DFAEmail
from validasi_pinATM import validasi_pin
from validasi_variabel import validasi_variabel


def uji_variabel():
    print("\n" + "=" * 45)
    print(" 1. VALIDASI NAMA VARIABEL")
    print("=" * 45)

    # Pengujian Otomatis Beberapa String
    daftar_uji = [
        "nama_user",
        "_count1",
        "123name",
        "user-name",
        "Var_99",
        "a b",
        "",
    ]
    print("[ Skenario Pengujian Otomatis ]")
    for teks in daftar_uji:
        status = "VALID (ACCEPT)" if validasi_variabel(teks) else "TIDAK VALID (REJECT)"
        print(f"Input: {repr(teks):<12} -> Status: {status}")

    # Coba Input Manual
    print("\n[ Uji Input Manual ]")
    teks = input("Masukkan nama variabel: ")
    status = "VALID (ACCEPT)" if validasi_variabel(teks) else "TIDAK VALID (REJECT)"
    print(f"Hasil: {status}")


def uji_email():
    print("\n" + "=" * 45)
    print(" 2. VALIDASI FORMAT EMAIL SEDERHANA")
    print("=" * 45)

    dfa = DFAEmail()

    # Pengujian Otomatis Beberapa String
    daftar_uji = [
        "budi123@gmail.com",
        "budi@gmail",
        "budi@@gmail.com",
        "user@domain.co.id",
    ]
    print("[ Skenario Pengujian Otomatis ]")
    for email in daftar_uji:
        valid, jejak = dfa.validasi(email)
        status = "VALID (ACCEPT)" if valid else "TIDAK VALID (REJECT)"
        print(f"Input : {email}")
        print(f"Jejak : {' -> '.join(jejak)}")
        print(f"Hasil : {status}\n")

    # Coba Input Manual
    print("[ Uji Input Manual ]")
    email = input("Masukkan email: ")
    valid, jejak = dfa.validasi(email)
    print(f"Jejak state : {' -> '.join(jejak)}")
    print(f"Hasil       : {'VALID (ACCEPT)' if valid else 'TIDAK VALID (REJECT)'}")


def uji_pin():
    print("\n" + "=" * 45)
    print(" 3. VALIDASI PIN ATM (6 DIGIT)")
    print("=" * 45)

    # Pengujian Otomatis Beberapa String
    daftar_uji = ["123456", "12345", "123a56", "000000", "1234567"]
    print("[ Skenario Pengujian Otomatis ]")
    for pin in daftar_uji:
        status = "VALID (ACCEPT)" if validasi_pin(pin) else "TIDAK VALID (REJECT)"
        print(f"Input: {repr(pin):<10} -> Status: {status}")

    # Coba Input Manual
    print("\n[ Uji Input Manual ]")
    pin = input("Masukkan PIN ATM: ")
    if validasi_pin(pin):
        print("Hasil: VALID (ACCEPT)")
    else:
        print("Hasil: TIDAK VALID (REJECT)")


def main():
    while True:
        print("\n" + "=" * 45)
        print("    PROGRAM IMPLEMENTASI DFA (VALIDASI INPUT)")
        print("=" * 45)
        print("1. Kasus Validasi Nama Variabel")
        print("2. Kasus Validasi Format Email Sederhana")
        print("3. Kasus Validasi PIN ATM")
        print("4. Keluar")
        print("=" * 45)

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            uji_variabel()
        elif pilihan == "2":
            uji_email()
        elif pilihan == "3":
            uji_pin()
        elif pilihan == "4":
            print("\nProgram selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid! Silakan masukkan angka 1-4.")


if __name__ == "__main__":
    main()