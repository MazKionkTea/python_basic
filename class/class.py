# class bisa dianalogikan sebagai template yang bisa dipakai
# oleh semua objek dengan nilai default yang sama.
# contoh :
# manusia sebagai class dan manusia memiliki banyak nama
# tetapi manusia yang memiliki berbagai macam nama terebut 
# masih memiliki satu template default yang sama yaitu "manusia"

# class namaClass():
#     def __init__(self) -> None:
#         pass


# class contohClass():
#     def namaFungsi(self):
#         pass

# // private attribute

# cara nembuat kede secara private dan hanya bisa diakses oleh
# kode tertentu yaitu dengan cara menambahkan dpuble underscore
# pada bagian depan kode.

# contoh :






class manusia():
    def __init__(self, nama, umur, tinggiBadanm, beratBadan) -> None:
        self.nama = nama
        self.umur = umur
        self.tinggi = tinggiBadanm
        self.berat = beratBadan

    def hoby(self):
        hobi = ["work", "music", "learning", "bully", "eksperiment"]
        self.myHoby = hobi
    
con = manusia("kosim", "29 tahun", "155 cm", "40 kg")

print(con.hoby())
        

def contoh1():
    pass

