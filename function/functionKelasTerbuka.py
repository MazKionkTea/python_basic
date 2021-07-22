#       // fungsi //

print("\n", "="*20, " Fungsi", "="*20, "\n")

# fungsi tanpa input/argumrn
# syntaks :

#   def namaFungsi();
#       aksi

# contoh :

def contohFungsi1():
    print(
    """
    ===============================================
    ========= fungsi tanpa input/argumen ==========
    ===============================================
    """
    )
# def adalah kita sudah mendefinisikan bahwa kita akan membuat fungsi
# contohFungsi1 adalah nama fungsinya
# karena ini bukan fungsi yang menggunakan input/argumen
# tanda kurung disamping nama fungsi tidak perlu diisi apapun
    print("\n", "ini adalah contoh fungsi tanpa input/argumen", "\n")
    # jalankan perintah print
    print("\n", "="*20, " Fungsi", "="*20, "\n")
    # jalankan perintah print

# cara pemanggilannya yaitu 
# dengan cara memanggil nama fungsinya diikuti dengan tanda kurung
# contohnya : namaFungsi()

#contohFungsi1()



# fungsi dengan input/argumen
# sintaks :

#   def namaFungsi(input/argumrn):
#       aksi

# contoh :

def contohFungsi2(kg):
    print(
    """
    ===============================================
    ======== fungsi dengam input/argumen ==========
    ===============================================
    """
    )
# input/argumen ditampatkan pada kurung disebelah nama fungsi
# karena ini fungsi yang menggunakan input/argumen
# tanda kurung disamping nama fungsi perlu diisi input/argumen
    harga = 10
    # variabel yang memiliki nilai 10
    hargaTotal = kg * harga
    # varibel baru yang nilainya berisi hasil dari 
    # perkalian variabrl harga dikalikan dengan argumen
    print("harga", kg,  "ayam adalah", hargaTotal, "rupiah")
    # jalankan perintah print
    print("\n", "ini adalah contoh fungsi dengan input/argumen", "\n")
    # jalankan perintah print
    print("\n", "="*20, " Fungsi", "="*20, "\n")
    # jalankan perintah print

# cara pemanggilannya yaitu 
# dengan cara memanggil nama fungsinya diikuti dengan tanda kurung
# karena ini adalah fungsi dengan input/argumen
# maka kita harus mengisi input/argumen yang ada didalam tanda kurung
# contohnya : namaFungsi(input/argumen)

#contohFungsi2(10)


def contohFungsi3(nama):
    print(
    """
    ===============================================
    ======== fungsi dengam input/argumen ==========
    ===============================================
    """
    )
    print("aku adalah", nama)
    print("\n", "="*20, " Fungsi", "="*20, "\n")

#contohFungsi3("kontoolll")



# def contohFungsi3(nama = input("input : ")):
#     print("aku adalah", nama)
#     print("\n", "="*20, " Fungsi", "="*20, "\n")
# contohFungsi3()



# fungsi dengan keyword argumen

# contoh :
def contohFungsi4(nama, pekerjaan):
    print(
    """
    ===============================================
    ======= fungsi dengam default argumen =========
    ===============================================
    """
    )
# fungsi dengan menggunakan lebih dari satu argumen
# akan dieksekusi berurutan dari kiri ke kanan
    print("aku adalah", nama, "dan aku seorang", pekerjaan)
    print("\n", "="*20, " Fungsi", "="*20, "\n")
# yang membedakan dari argumen bisa adalah
# argumen dalam fungsi diatas harus diisi secara spesifik
# contohnya :
# contohFungsi4(nama="kosim", pekerjaan="pengangguran")
# fungsi yang menggunakan argumen lebih dari satu
# akan dieksekusi secara berurutan pada contohFungsi4(nama, pekerjaan)
# argumen yang pertama kali dieksekusi adalah argumen nama terlebih dahulu
# kemudian argumen pekerjaan akan dieksekusi setelahnya
# jika kita mamasukan argumen seperti ini : contohFungsi4("kosim", "pengangguran")
# hasilnya tidak akan erorr
# tapi jika terbalik seperti contohFungsi4("pengangguran", "kosim")
# hasilnya akan perbalik
# cara mengakses argumen pada fungsi ini bisa dengan cara
# contohFungsi4("kosim", "pengangguran")
# atau
# contohFungsi4(nama="kosim", pekerjaan="pengangguran")

#contohFungsi4("kosim", "pengangguran")



# fungsi dengam default argumen

# contoh :
def contohFungsi5(nama="'nama tidak diisi'", pekerjaan="'pekerjaan tidak diisi'", sifat="'sifat tidak diisi'"):
    print(
    """
    ===============================================
    ======= fungsi dengam default argumen =========
    ===============================================
    """
    )
# fungsi dengan menggunakan lebih dari satu atau dua argumen
# karena menggunakan nilai default pada argumen tersebut maka
# jika argunennya tidak diisi maka argumen defaultlah yang akan dieksekusi
# akan dieksekusi berurutan dari kiri ke kanan
    print("aku adalah", nama)
    print("dan aku seorang", pekerjaan)
    print("sifatku", sifat)
    print("\n", "="*20, " Fungsi", "="*20, "\n")
# sama dengan contoh fungsi yang sbelumnya
# cara mengaksesnya juga sama
# tapi karena fungsi ini memiliki tiga argumen
# jika salah satu argumennya tidak diisi maka argumen default yang akan di eksekusi

#contohFungsi5("kosim", "pengangguran", "pemalas")



# fungsi dengan return value/fungsi yang dapat mengembalikan nilai

def kuadrat(argumen):
    print(
    """
    ===============================================
    =========== fungsi dengan return ==============
    ===============================================
    """
    )
    kuadrat = argumen ** 2
    print("nilai dari", argumen, "kuadrat adalah", kuadrat)
    print("nillai returnnya adalah", kuadrat)
    
    print("\n", "="*20, " Fungsi", "="*20, "\n")
    
    return kuadrat

#kuadrat(5)




# fungsi dengan return value dan multiplr argumrn

def tambah(a, b):
    tambah = a + b
    return tambah
    # test return [tamah, 2, 3, 4]
#print(tambah(2, 2))


# membuat fungsi anonimous dengan lambda

# syntax
# namaFungsiAnonim = lambda argument: argument
ex = lambda a, b: a + b
# ex adalah nama fungsi anonim/variabel yang memiliki nilai fungsi anonim lambda
# lambda a,b adalah keyword anonim lambda diikuti argumen dan bisa menggunakan lebih dari satu argumen
# a + b adalah argumen yang akan dieksekusi, diproses, dan bisa ditampilkan ke layar
ex(2,2)
# cara memanggil fungsi anonim lambda
"""
jika dalam fungsi biasa dapat ditulis seperti di bawah

    def ex(a, b):                   # nama fungsi yang diikuti argumen
        ex = a + b                  # argumen yang akan diproses dan dieksekusi
        return ex                   # mengembalikan hasil akhir/nilai atau value dari suatu fungsi

    ex(argumen a, argumen b)        # cara pemanggilan

jika menggunakan lambda penulisannya seperti dibawah

    ex = lambda a, b: a + b         # ex = nama fungsi, lambda a, b = argumen
                                    # a + b = argumen yang akan diproses dan dieksekusi

    ex(argumen a, argumen b)        # cara pemanggilan

"""








































# print("\n", "="*20, " Fungsi", "="*20, "\n")