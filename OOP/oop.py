# class bisa disebut juga sebagai template atau juga bisa disebut sebahgai objek/instenses
# class/objek memiliki dua parameter
#     - atrubut/pengenal
#     - method/hal yang bisa dilakukan
# 
# contoh :
# 
# class NamaClass:
#     def __init__(self):
#         pass
# 
# class manusia:
#     def __init__(self) -> None:
#         self.nama = nama
#         self.umur = umur
#         self.tinggi = tinggi
#         self.berat = berat


class Karyawan:
# deklarasi class dan nama class
# atau template
    jumlah = 0
    # jumlah adalah static variabel dam ikut kedalam class
    def __init__(self, nama, umur, tinggi, berat, divisi):
    # costruktor (akan sieksekusi pertamakali saat objek dibuat)
        self.nama = nama
        self.umur = umur
        self.tinggi = tinggi
        self.berat = berat
        self.divisi = divisi
        # baris kode ditatas bisa disebut attribut
        # atau instense/objek variabel
        Karyawan.jumlah += 1
        # untuk menghitung jumlah yang telah ditambahkan 
        # kedalam clss objek.
        # jumlah akan ditambahkan satu kedalam static variabel
        # untuk setiap kali objek dibuat.

    # cara membuat method sama saja seperti memnuat fungsi
    # hanya ada penambahan self didalamnya karena berada 
    # didalam objek.
    # - merhod tanpa argumen dan return/void function 
    #   contoh :
    #       def method(self):
    #           pass
    # - method dengan argumen
    #       def method(self, arg1, arg2):
    #           pass
    # - methid dengan return
    #       def method(self):
    #           return
    # - method dengan argumen dan return
    #       def method(self, arg1, arg2):
    #           return
    #           pass
    
    def keahlian(self, keahlian1, keahlian2, keahlian3, keahlian4):
    # method 1 (fungsi dari suatu objek)
        self.keahlian1 = keahlian1
        self.keahlian2 = keahlian2
        self.keahlian3 = keahlian3
        self.keahlian4 = keahlian4
        print(self.nama, "memiliki keahlian")

    # method memiliki dua interaksi
    # - interaksi dengan client
    #   contohnya karakter yang bergerak dalam game yang bisa 
    #   dilihat oleh user.
    # - interaksi antar objek 
    #   contohnya karakter yang bisa saling serang dalam game.

    def tugas(self, tugas1, tugas2, tugas3, tugas4):
    # method 2 (fungsi dari suatu objek)
        self.tugas1 = tugas1
        self.tugas2 = tugas2
        self.tugas3 = tugas3
        self.tugas4 = tugas4

    # method juga bisa kita analogikan seperti fungsi tombol
    # contoh :
    # ukuran, warna, atau teks yang ada pada tombol
    # adalah sebagai atributnya (pengenal).
    # dan fungsi, efek, atau aksi adalah method
    # ketika tombol tersebut kita klik (fungsi dari tombol tsb). 

    def gaji(self, gajiPokok, lemburan, bonus):
        self.gajiPokok = gajiPokok
        self.lemburan = lemburan
        self.bonus = bonus
        totalGaji = gajiPokok + lemburan + bonus
        print("total gaji", self.nama, "adalah", "Rp.", totalGaji)
        return totalGaji

   


