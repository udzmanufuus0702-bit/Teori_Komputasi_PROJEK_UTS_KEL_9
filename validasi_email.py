class DFAEmail:
    def __init__(self):
        self.state_awal = "q0"
        self.state_akhir = {"q4"}

        # Tabel transisi DFA
        self.transisi = {
            "q0": {
                "HURUF": "q1",
                "ANGKA": "q1",
                "LAINNYA": "q_dead"
            },
            "q1": {
                "HURUF": "q1",
                "ANGKA": "q1",
                "AT": "q2",
                "LAINNYA": "q_dead"
            },
            "q2": {
                "HURUF": "q2",
                "ANGKA": "q2",
                "TITIK": "q3",
                "LAINNYA": "q_dead"
            },
            "q3": {
                "HURUF": "q4",
                "LAINNYA": "q_dead"
            },
            "q4": {
                "HURUF": "q4",
                "LAINNYA": "q_dead"
            },
            "q_dead": {
                "HURUF": "q_dead",
                "ANGKA": "q_dead",
                "AT": "q_dead",
                "TITIK": "q_dead",
                "LAINNYA": "q_dead"
            }
        }

    def kelompok_simbol(self, karakter):
        if karakter.isascii() and karakter.isalpha():
            return "HURUF"
        elif karakter.isascii() and karakter.isdigit():
            return "ANGKA"
        elif karakter == "@":
            return "AT"
        elif karakter == ".":
            return "TITIK"
        else:
            return "LAINNYA"

    def validasi(self, email):
        state = self.state_awal
        jejak = [state]

        for karakter in email:
            simbol = self.kelompok_simbol(karakter)
            state = self.transisi[state].get(
                simbol, "q_dead"
            )
            jejak.append(state)

        valid = state in self.state_akhir
        return valid, jejak

def main():
    dfa = DFAEmail()

    print("=" * 45)
    print("VALIDASI FORMAT EMAIL SEDERHANA")
    print("Metode: Deterministic Finite Automata")
    print("=" * 45)

    while True:
        email = input("\nMasukkan email (atau 'keluar'): ")

        if email.lower() == "keluar":
            print("Program selesai.")
            break

        valid, jejak = dfa.validasi(email)

        print("Input       :", repr(email))
        print("Jejak state :", " -> ".join(jejak))

        if valid:
            print("Hasil       : VALID (ACCEPT)")
        else:
            print("Hasil       : TIDAK VALID (REJECT)")

if __name__ == "__main__":
    main()
