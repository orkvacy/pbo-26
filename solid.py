from abc import ABC, abstractmethod


class EmailSender:
    def kirim(self, tujuan, pesan):
        print(f"[EMAIL ke {tujuan}] {pesan}")


class Rekening(ABC):
    def __init__(self, nama, email, jenis, saldo=0):
        self.nama = nama
        self.email = email
        self.jenis = jenis
        self.saldo = saldo
        self.email_sender = EmailSender()

    def setor(self, jumlah):
        self.saldo += jumlah
        self.email_sender.kirim(self.email, f"Setor {jumlah} berhasil")

    def tarik(self, jumlah):
        if self.jenis == "tabungan":
            biaya = 2500
        elif self.jenis == "giro":
            biaya = 5000
        else:
            biaya = 0

        total = jumlah + biaya
        if total > self.saldo:
            print("Saldo tidak cukup")
            return
        self.saldo -= total
        self.email_sender.kirim(self.email, f"Tarik {jumlah} berhasil, biaya {biaya}")

    def cetak_mutasi(self):
        print("=" * 30)
        print(f"Nama  : {self.nama}")
        print(f"Jenis : {self.jenis}")
        print(f"Saldo : Rp{self.saldo:,}")
        print("=" * 30)

    def simpan_ke_file(self):
        with open("data_rekening.txt", "a") as f:
            f.write(f"{self.nama},{self.jenis},{self.saldo}\n")

    @abstractmethod
    def cetak_buku_tabungan(self):
        pass


class RekeningTabungan(Rekening):
    def cetak_buku_tabungan(self):
        print(f"Mencetak buku tabungan {self.nama}")


class RekeningDigital(Rekening):
    def cetak_buku_tabungan(self):
        raise NotImplementedError("Rekening digital tidak punya buku tabungan")


class Deposito(Rekening):
    def tarik(self, jumlah):
        raise Exception("Deposito tidak bisa ditarik sebelum jatuh tempo")

    def cetak_buku_tabungan(self):
        print(f"Mencetak bilyet deposito {self.nama}")


def tarik_akhir_bulan(daftar_rekening, jumlah):
    for rekening in daftar_rekening:
        rekening.tarik(jumlah)


andi = RekeningTabungan("ridho", "ridho@mail.com", "tabungan", 500000)
budi = RekeningDigital("puncul", "puncul@mail.com", "digital", 300000)
citra = Deposito("alex", "alex@mail.com", "deposito", 1000000)

andi.setor(100000)
andi.tarik(50000)
andi.cetak_mutasi()
andi.simpan_ke_file()

tarik_akhir_bulan([andi, budi, citra], 10000)
budi.cetak_buku_tabungan()