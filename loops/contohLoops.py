
def contohForLoop1():
    # contoh for loop list sebagai iterable/pengulangan

    gorengan = ["piscok", "bakwan", "tempeGoreng", "tahuGoreng", "bala-Bala"]
    # variabel gorengan diisi dengan beberapa list
    for g in gorengan:
    # huruf g adalah variabel baru yang diisi oleh list yang ada idalam variabel gorengan
    # analoginya, isi dari sebuah list didalam variabel gorengan dipindahkan
    # kedalam variabel baru (g)
    # for g in gorengan: bisa dibaca dengan cara seperti dibawah ini
    # untuk setiap g didalam variabe gorengan:  atau
    # untuk setiap isi list ["piscok", "bakwan", "tempeGoreng", "tahuGoreng", "bala-Bala"] didalam variabel gorengan:
        print(g)
        # tampilkan ke layar isi dari semua list yang dimasukan kedalam variabel g yang baru

    print("\n", "=" * 50, "\n")

def contohForLoop2():
    # for didalam for
    gorengan = ["piscok", "bakwan", "tempeGoreng", "tahuGoreng", "bala-Bala"]
    buah = ["demangka", "jeruk", "apel", "mangga", "anggur"]
    sayur = ["kangkung", "woortel", "tomat", "bayam", "kentang"]

    daftarBelanja = [gorengan, buah, sayur]
    print(daftarBelanja)
    print("\n", "=" * 50, "\n")
    

    for subDaftarBelanja in daftarBelanja:
        print(subDaftarBelanja)
        print(" " * 50, "\n")
        # contoh yangi ini sama saja dengan contoh1 
        # hanya ditambah beberapa variabel yang diisi dengan list ditambah garis dan spasi sebagai menanda
        for komponen in subDaftarBelanja:
            print(komponen)
        print("\n", "=" * 50, "\n")
    print("\n", "=" * 50, "\n")
            # loop yang ini untuk menampilkan semua isi list dengan lebih rinci
            # menampilkan hasil looping yang pertama
            # kemudian diikuti oleh hasil looping yang kedua

def contohForLoop3():
    for i in range (0,10):
        # range adalah set/jajaran/barisan yang memiliki suatu komponen
        # (0, 10) adalah set/jajaran/barisan angka yang dimulai dari angka 0 sampai angka 10
        print(i)

    print("\n", "=" * 50, "\n")

    for i in range (1, 100, 10):
        # (1, 100, 10)
        # (start, stop, inkrement)
        # inkrement/penambahan.
        # jadi jika looping ini dimulai dari angka 1 dan menggunakan inkrement 10 artinya
        # 1 + 10 = 11 maka yang akan ditampilkan adalah angka 11, dan seterusnya ex: 11 + 10 = 21 
        print(i)

    print("\n", "=" * 50, "\n")

def contohForLoop4():
    for i in range (1, 15):
        if i == 13: # if i is 13: jika penulisan "==" diganti dengan "is" sering terjadi SyntaxWarning 
            print(i)

    print("\n", "=" * 50, "\n")

    for i in range (0, 20):
        if i == 13: # if i is 13: jika penulisan "==" diganti dengan "is" sering terjadi SyntaxWarning
            print("lantai", i)
            break
            # break digunakan untuk keluar dari loop secara paksa
            # karena nilai dari angka 13 sudah ditemukan, break langsung dieksekusi untuk keluar dari loop
        else:
            print("lantai tidak ditemukan")
    else:
        print("bangunan belum jadi")
            # jika else ditempatkan didalam for, hasilnya akan berbeda
            # karena looping masih berjalan
            # jadi, else diletakan diluar for supaya else tidak dieksekusi saat loopng sedang berjalan

    print("\n", "=" * 50, "\n")

    def test():
        for i in range(1,30):
            if i == 50: # if i is 13: jika penulisan "==" diganti dengan "is" sering terjadi SyntaxWarning
                print("nilai i adalah : ", i)
                break # break digunakan untuk keluar dari loop secara paksa
            else:
                print("nilai i hilang")
        for i in range (1,21):
            if i < 13:
                print(i, "kontol")
            elif i == 13:
                print(i, "  // ngentot //")
                continue # continue adalah kebalikan dari break
            else:
                print(i, "memek")

    print("\n", "=" * 50, "\n")



# while loop hampir sama dengan for loop tapi memiliki beberapa perbedaan
# sintaks dasar dari while loop seperti dibawah

# while kondisi selalu bernilai boolean True :
#     jalankan aksi

# else, brak, continue, pass juga bisa digunakan dalam while loop

def contohWhileLoop1():
    angka = 1 # basis awal
    while angka <= 5:
        # selama nilai dari variabel angka kurang dari 5 atau true
        print("kanyut", angka)
        # jalankan/eksekusi perintah ini
        angka += 1
        # nilai dari variabel angka ditambah 1 lalu jalankan lagi perulangan
        # bisa juga dengan cara angka = angka + 1
        # (+=) tanda samadengan harus ditempatkan dibelakang. jika terbalik, while loop akan menjadi infinite
        # nilai variabel angka pada basis awal akan ditmbahkan satu setiap kali looping
        # dan mengulangi proses looping dampai kondisi while menjadi boolean false
    print("\n", "while loop berakhir dan tampilan ini berada diluar while loop")

    print("\n", "=" * 50, "\n")

# kita bisa membuat while loop ang terus berjalan
# sampai loop tersebut memberikan sebuah nilai tertentu
# sengan menggunakan metode boolean

def contohWhileLoop2():
    start = True
    # variabel yang bernilai boolean
    angka = 1
    # variabel yang memiliki nilai integer
    while start:
    # selama variabel start bernilai boolean true
        print("while loop berjalan sebanyak", angka, "kali")
        # jalankan/eksekusi perintah ini
        if angka == 15:
        # jika varibel yang bernama angka memiliki nilai 15
        # sintaks diatas bisa juga ditulis "if angka is 15:"
        # tetapi penggunaan "is" bisa menimbulkan erorr jika tidak tepat tipe datanya
            start = False
            # variabel start yang tadinya bernilai boolean true
            # diganti nilainya menjadi boolean false
            print("\n", "while loop sudah berakhir")
            # lalu jalankan perintah print diatas
        angka = angka + 1

    print("\n", "=" * 50, "\n")

def contohWhileLoop3():
    # menggunakan else dalam while loop
    angka = 1
    # variabel yang bernama angka yang memiliki nilai integer
    while angka <= 10:
    # selama variabel yang bernama angka memilki nilai kurang dari/sama dengan 10
        print("nilai saat ini adalah", angka)
        # jalankan perintah print diatas
        angka += 1
        # tambahkan nilai variabel angka sengan angka 1
        # lalu lakukan lagi perulangan sampai nilai variabel angka memiliki nilai 10
    else:
    # while sebagai kondisi perrtama
    # else adalah kondisi lainnya
    # jika while loop sudah berakhir
    # atau jika kondisi while loop tidak terpenuhi
        print("\n", "nilai akhir adalah", angka)
        # jalankan perintah print diatas

    print("\n", "=" * 50, "\n")

def contohWhileLoop4():
    # menggunakan else, break dan menambahkan if dalam while loop
    angka = 1
    # variabel yang bernama angka yang memiliki nilai integer
    while angka <= 10:
    # selama variabel yang bernama angka memilki nilai kurang dari/sama dengan 10
        print(angka, "kurang dari 10")
        # jalankan perintah print diatas
        if angka == 7:
        # jika variabel yang bernama angka memiliki nilai 7
            print("\n", "looping berhenti di angka", angka)
            # jalankan perintah print diatas
            break
            # sama seperti dalam for loop, break bisa digunakan untuk menghentikan suatu program
            # jika break dieksekusi, while loop akan langsung keluar dari pengulangan
            # dan perintah lain dibawahnya tidak akan dieksekusi karena langsung keluar dari loop
        print("nilai variabel angka telah ditambah")
        # jalankan perintah print diatas
        angka += 1
        # nilai inkrement
    else:
        print("keluar dari loop tanpa mengeksekusi break")
        # jalankan perintah print diatas

    print("\n", "=" * 50, "\n")

def contohWhileLoop5():
    # menggunakan else, continue dan menambahkan if dalam while loop
    angka = 1
    # variabel yang bernama angka yang memiliki nilai integer
    while angka < 10:
    # selama variabel yang bernama angka memilki nilai kurang dari/sama dengan 10
        print(angka, "kurang dari 10")
        # jalankan perintah print diatas
        if angka == 7:
            # jika variabel yang bernama angka memiliki nilai 7
            print(angka, "adalah angka yag dicari, tetapi", angka, "kurang dari 10")
            # jalankan perintah print diatas
            angka += 1
            # nilai inkrement
            continue
            # continue. perintah ini berpotensi akan terjadi ifinite loop
            # karena jika continue dieksekusi, proses looping akan langsung naik ke atas
            # kembali ke posisi while loop tanpa menabahkan nilai variabel angka terlebih dahulu
            # triknya menambahkan inkremen diatas continue
        print("nilai variabel angka telah ditambah")
        # jalankan perintah print diatas
        angka += 1
        # nilai inkrement
    else:
        print("\n", "keluar dari loop")

    print("\n", "=" * 50, "\n")


