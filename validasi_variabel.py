# Program DFA Sederhana: Validasi Nama Variabel
# Aturan:
# - Karakter pertama harus huruf (a-z, A-Z) atau underscore (_)
# - Karakter berikutnya boleh huruf, angka (0-9), atau underscore (_)

def validasi_variabel(teks):
    print(f"Input : '{teks}'")

    # Cek jika string kosong
    if not teks:
        print("Status : TIDAK VALID (String kosong)\n" + "-" * 40)
        return

    # 1. Validasi Karakter Pertama
    karakter_pertama = teks[0]
    if not (karakter_pertama.isalpha() or karakter_pertama == "_"):
        print(f"  Gagal di karakter pertama '{karakter_pertama}' (harus huruf atau _)")
        print("Status : TIDAK VALID\n" + "-" * 40)
        return

    # 2. Validasi Karakter Berikutnya (Sisa string)
    is_valid = True
    for c in teks[1:]:
        if not (c.isalnum() or c == "_"):
            print(f"  Gagal di karakter '{c}' (hanya boleh huruf, angka, atau _)")
            is_valid = False
            break

    # Hasil akhir
    if is_valid:
        print("Status : VALID")
    else:
        print("Status : TIDAK VALID")
    print("-" * 40)


# --- Pengujian Otomatis ---
daftar_uji = [
    "nama_user",
    "_count1",
    "123name",
    "user-name",
    "Var_99",
    "a b",
    "",
]

print("=== PENGUJIAN VALIDASI NAMA VARIABEL ===\n")
for s in daftar_uji:
    validasi_variabel(s)


# --- Input Manual dari Pengguna ---
print("\n=== COBA SENDIRI (ketik 'selesai' untuk keluar) ===")
while True:
    teks = input("Masukkan nama variabel: ")
    if teks.lower() == "selesai":
        print("Program selesai.")
        break
    validasi_variabel(teks)
