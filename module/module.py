"""
modul mengijinkan kita agar bisa mengatur  kode python yang telah kita buat 
mengelompokan kode yang sejenis kedalam sebuah modul sehingga kode 
yang telah kita buat bisa lebih difahami dan digunakan. modul dalam python objek 
dapat kita berikan nama apapun.

mudahnya, sebuah modul adalah kode python yang tetap. modul bisa 
diisi dengan sebuah fungsi, class dan variabel. modul juga bisa 
jadi adalah sebuah program kode yang bisa dijalankan.
"""

# contoh :
def printFunct(par):
    print("hello :", par)
    return


"""
        // The import Statement

kita bisa menggunakan sumber file python apapun sebagai sebuah modul 
dengan mengeksekusi import statement/perintah import dalam beberapa 
sumber kode python yang lain.

sintaks import adalah sbb :

    import namaModul[, subModul1][, subModul2]

contoh :

    #!/usr/bin/python3
    import basicOperator
    # memasukan/mengimport modul basicOperator

"""