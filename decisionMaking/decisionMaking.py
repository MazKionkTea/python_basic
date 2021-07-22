#               // if Statement //


# syntax :

#     if statement/kondisi:
#         action/aksi

# contoh :

variabel = 5
# sebuah variabel yang memiliki nilai 5

if variabel < 6:
# cara mudah membaca kode diatas yaitu 
# jika nilai variabel kurng dari angka 6 maka:
# if statement dan diikuti dengan kondisi untuk membuat keputusan
# jika kondisi terpenuhi ataupun tidak terpenuhi 
# akan menghasilkan suatu aksi 
    print(variabel, "Kurang Dari 6")
    # aksi akan dieksekusi tergantung dari kondisi if statement
    # jika kondisi terpenuhi aksi akan dijalankan
    # dan melanjutkan kode dibawahnya 
    # atau sebaliknya 

# dari contoh diatas kondisinya harus terpenuhi
# supaya aksi bisa dibawahnya dieksekusi
# jika kondisinya tidak terpenuhi 
# blok kode aksi akan dilewati menuju kode dibawahnya



#               // if ... else Statement //


# syntax :

#     if statement/kondisi:
#         action/aksi
#     else:
#         action/aksi

# contoh :

variabel = 5
# sebuah variabel yang memiliki nilai 5

if variabel < 4:
# cara mudah membaca kode diatas yaitu 
# jika nilai variabel kurng dari angka 6 maka:
# if statement dan diikuti dengan kondisi untuk membuat keputusan
# jika kondisi terpenuhi ataupun tidak terpenuhi 
# akan menghasilkan suatu aksi 
    print(variabel, "Lebih Dari 4")
    # aksi akan dieksekusi tergantung dari kondisi if statement
    # jika kondisi terpenuhi aksi akan dijalankan
    # dan melanjutkan kode dibawahnya 
    # atau sebaliknya
else:
# else bisa disebut sebagai kondisi alternatif
# jika kondisi pada if satemenet tidak terpenuhi
# dan akan menghasilkan aksi lainnya
    print(variabel, "Kurang Dari 6")
# dari contoh diatas kondisinya harus terpenuhi
# supaya aksi bisa dibawahnya dieksekusi
# jika kondisinya tidak terpenuhi 
# blok kode aksi akan dilewati menuju kode dibawahnya

# contoh lain dengan menggunakan input

variabel = int(input("Masukan angka 1 - 5 : "))
# variabel yang nilainya tergantung dari inputan user
# input dari user harus angka 1 - 5
if variabel < 3:
    print(variabel, "Kurang Dari 3")
else:
    print(variabel, "Lebih Dari 3")

