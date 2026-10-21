# Program DFA Validasi Nama Variabel 
def is_huruf(c):
    # Mengecek apakah karakter berupa huruf a-z atau A-Z
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z')

def is_angka(c):
    # Mengecek apakah karakter berupa angka 0-9
    return '0' <= c <= '9'

def validasi_variabel(teks):
    # Cek jika string kosong
    if not teks:
        return False

    # 1. Karakter pertama harus huruf atau underscore (_)
    if not (is_huruf(teks[0]) or teks[0] == "_"):
        return False

    # 2. Karakter berikutnya boleh huruf, angka, atau underscore (_)
    for c in teks[1:]:
        if not (is_huruf(c) or is_angka(c) or c == "_"):
            return False  # Langsung tolak jika ada karakter terlarang (masuk trap state)

    return True


# --- Program Utama / Pengujian ---
if __name__ == "__main__":
    daftar_uji = ["nama_user", "_count1", "123name", "user-name", "Var_99", "a b", ""]

    print("=== PENGUJIAN VALIDASI NAMA VARIABEL (MANUAL) ===")
    for s in daftar_uji:
        status = "VALID" if validasi_variabel(s) else "TIDAK VALID"
        print(f"Input: {repr(s):<12} -> {status}")

    # Input manual
    print("\n--- COBA SENDIRI ---")
    teks = input("Masukkan nama variabel: ")
    if validasi_variabel(teks):
        print("Status: VALID")
    else:
        print("Status: TIDAK VALID")