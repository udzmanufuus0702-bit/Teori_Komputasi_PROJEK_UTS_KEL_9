# DFA Validasi Nama Variabel
# Aturan:
# - Karakter pertama harus huruf (a-z, A-Z) atau underscore (_)
# - Karakter berikutnya boleh huruf, angka (0-9), atau underscore (_)

# Definisi DFA
# Q  = {q0, q1, qT}
# Σ  = huruf, angka, underscore, dan karakter lain
# q0 = q0 (state awal)
# F  = {q1} (state akhir / diterima)
# qT = trap state (state jebakan, kalau sudah masuk tidak bisa keluar)


def jenis_karakter(c):
    """Mengelompokkan karakter jadi: huruf, angka, underscore, atau lain"""
    if c.isalpha() and c.isascii():
        return "huruf"
    elif c.isdigit():
        return "angka"
    elif c == "_":
        return "underscore"
    else:
        return "lain"


# Tabel transisi: delta[state][jenis karakter] = state berikutnya
delta = {
    "q0": {"huruf": "q1", "underscore": "q1", "angka": "qT", "lain": "qT"},
    "q1": {"huruf": "q1", "underscore": "q1", "angka": "q1", "lain": "qT"},
    "qT": {"huruf": "qT", "underscore": "qT", "angka": "qT", "lain": "qT"},
}

state_awal = "q0"
state_akhir = ["q1"]


def validasi(teks):
    state = state_awal
    print("Input :", teks)
    print("Jejak transisi:")

    # string kosong tidak punya karakter, langsung dicek state awal
    for c in teks:
        jenis = jenis_karakter(c)
        state_baru = delta[state][jenis]
        print(f"  {state} --'{c}' ({jenis})--> {state_baru}")
        state = state_baru

    print("State akhir :", state)

    if state in state_akhir:
        print("Status : VALID")
    else:
        print("Status : TIDAK VALID")
    print("-" * 40)


# Pengujian
daftar_uji = [
    "nama_user",
    "_count1",
    "123name",
    "user-name",
    "Var",
    "a b",
    "",
]

print("=== PENGUJIAN VALIDASI NAMA VARIABEL ===\n")
for s in daftar_uji:
    validasi(s)

# Input manual dari pengguna
print("\n=== COBA SENDIRI (ketik 'selesai' untuk keluar) ===")
while True:
    teks = input("Masukkan nama variabel: ")
    if teks == "selesai":
        break
    validasi(teks)
