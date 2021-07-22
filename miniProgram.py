def variabel():
    print(
        """
        #=====================================================================================#
        #                                                                                     #
        #                                                                                     #
        #                                   " Variabel "                                      #
        #                                                                                     #
        #                                                                                     #
        #   Variabel tidak lain adalah lokasi memori yang dipesan untuk menyimpan nilai.      #
        #   Ini berarti bahwa ketika kita membuat variabel, Kita memesan beberapa             #
        #   ruang dalam memori.                                                               #
        #                                                                                     #
        #   Variabel Python tidak perlu deklarasi eksplisit untuk memesan ruang memori.       #
        #   Deklarasi terjadi secara otomatis saat Kita menetapkan nilai ke variabel.         #
        #   Tanda sama dengan (=) digunakan untuk menetapkan nilai ke variabel.               #
        #                                                                                     #
        #   Operan di sebelah kiri operator = adalah nama variabel                            #
        #   dan operan di sebelah kanan operator = adalah nilai yang disimpan dalam variabel. #
        #   cara menetapkan sebuah nilai kedalam sebuah variabel dapat dilihat dibawah.       #
        #                                                                                     #
        #   Contoh :                                                                          #
        #                                                                                     #
        #       namaVariabel = nilaiVariabel                                                  #
        #                                                                                     #
        #                                                                                     #
        #           counter = 100           # memiliki tipe data integer                      #
        #           miles	= 1000.0    # memiliki tipe data desimal                      #
        #           name	= "John"    # memiliki tipe data string                       #
        #                                                                                     #
        #   variabel juga bisa diisi dengan berbagai macam tipe data.                         #
        #                                                                                     #
        #                                                                                     #
        #    [00]   Back                                                                      #
        #    [99]   Exit                                                                      #
        #                                                                                     #
        #=====================================================================================#
        """
    )
    pilihan = int(input("##>>>   ")) # dalam fungsi variabel()
    # user diminta memilih program
    if pilihan == 00: # kondisi pertama yang harus dipenuhi saat fungsi varaibel() berjalan 
    # jika user memasukan angka 00
        menu()
        # jalankan fungsi menu()
    elif pilihan == 99: # kondisi kedua jika kodisi pertama tidak terpenuhi
    # dan jika user memasukan angka 99
        exit()
        # keluar dari program
    else: # kondisi lainya (jika kondisi pertama dan kedua tidak terpenuhi) 
    # dan jika user memeilih selain pilihan yang ada diatas
        print("Pilihan Tidak Tersedia")
        # tampilkan
        variabel()
        # jalankan lagi fungsi variabel

def basicOperator():
    print(
        """
        #=====================================================================================#
        #                                                                                     #
        #                                                                                     #
        #                                " Tipe-tipe Operator "                               #
        #                                                                                     #
        #                                                                                     #
        #        Bahasa Python mendukung tipe operator berikut                                #
        #                                                                                     #
        #     [1] • Arithmetic Operators/Operator Aritmatika                                  #
        #     [2] • Comparison (Relational) Operators/Perbandingan Operator penghubung        #
        #     [3] • Assignment Operators/Operator Penugasan                                   #
        #     [4] • Logical Operators/Operator Logika                                         #
        #     [5] • Membership Operators/Operator Keanggotaan                                 #
        #     [6] • Identity Operators/Operator Identitas                                     #
        #     [7] • Bitwise Operators/Operator Bitwise                                        #
        #                                                                                     #
        #                                                                                     #
        #    [00]   Back                                                                      #
        #    [99]   Exit                                                                      #
        #                                                                                     #
        #                                                                                     #
        #=====================================================================================#
        """
    )
    pilihan = int(input("##>>>    ")) # dalam fungsi basicOperator()
    if pilihan == 1: 
        aritmatika()       
    elif pilihan == 2:
        perbandingan()      
    elif pilihan == 3:
        penugasan()       
    elif pilihan == 4:
        logika()       
    elif pilihan == 5:
        keanggotaan()      
    elif pilihan == 6:
        identitas()       
    elif pilihan == 7:
        print("Bitwise Sedang Diupdate...!!!")
        basicOperator()
    elif pilihan == 00:
        menu()
    elif pilihan == 99:
        exit()
    else:
        print("Pilihan Tidak Tersedia...")
        basicOperator()

def aritmatika():
    print(
        """
        #=====================================================================================#
        #                                                                                     #
        #                                                                                     #
        #                   " Arithmetic Operators/Operator Aritmatika "                      #
        #                                                                                     #
        #                                                                                     #
        #           Bahasa Python mendukung tipe operator berikut                             #
        #                                                                                     #
        #       Asumsikan variabel a memiliki nilai 10 dan variabel b memiliki nilai 21       #
        #                                                                                     #
        #        [1]  +   (Penjumlahan)          Contoh : a + b = 31                          #
        #        [2]  -   (Pengurangan)          Contoh : a – b = -11                         #
        #        [3]  *   (Perkalian)            Contoh : a * b = 210                         #
        #        [4]  /   (Pembagian)            Contoh : b / a = 2.1                         #
        #        [5]  **  (Perpangkatan)         Contoh : a**b =10 to the power 20            #
        #        [6]  %   (Modulus)              Contoh : b % a = 1                           #
        #        [7]  //  (Floor Division)       Contoh : 9//2 = 4 and 9.0//2.0 = 4.0         #
        #                                                                                     #
        #                                                                                     #
        #    [00]   Back                                                                      #
        #    [99]   Exit                                                                      #
        #                                                                                     #
        #                                                                                     #
        #=====================================================================================#
        """
    )

    pilihan = int(input("   >>>    "))
    if pilihan == 00:
        basicOperator()
    elif pilihan == 99:
        exit()
    else:
        print("Pilihan Tidak Tersedia")
        aritmatika()

def perbandingan():
    print(
        """
        #=====================================================================================#
        #                                                                                     #
        #                                                                                     #
        #      " Comparison (Relational) Operators/Perbandingan Operator penghubung "         #
        #                                                                                     #
        #                                                                                     #
        #           Bahasa Python mendukung tipe operator berikut                             #
        #                                                                                     #
        #                                                                                     #
        #       Asumsikan variabel a memiliki nilai 10 dan variabel b memiliki nilai 20       #
        #                                                                                     #
        #    [1]  ==  (Jika nilai dua operan sama, maka kondisinya menjadi benar.)            #
        #              Contoh : (a == b) is not true                                          #
        #                                                                                     #
        #    [2]  !=  (Jika nilai dari dua operan tidak sama, maka kondisi menjadi benar)     #
        #              Contoh : (a!= b) is true                                               #
        #                                                                                     #
        #    [3]  >   (Jika nilai operan kiri lebih besar dari nilai operan kanan,            #
        #              maka kondisi menjadi benar)                                            #
        #              Contoh : (a > b) is not true                                           #
        #                                                                                     #
        #    [4]  <   (Jika nilai operan kiri kurang dari nilai operan kanan,                 #
        #              maka kondisi menjadi benar)                                            #
        #              Contoh : (a < b) is true                                               #
        #                                                                                     #
        #    [5]  >=  (Jika nilai operan kiri lebih besar dari atau sama dengan nilai         #
        #              operan kanan, maka kondisi menjadi benar)                              #
        #              Contoh : (a >= b) is not true                                          #
        #                                                                                     #
        #    [6]  <=  (Jika nilai operan kiri kurang dari atau sama dengan nilai              #
        #              operan kanan, maka kondisi menjadi benar)                              #
        #              Contoh : (a <= b) is true                                              #
        #                                                                                     #
        #                                                                                     #
        #    [00]   Back                                                                      #
        #    [99]   Exit                                                                      #
        #                                                                                     #
        #                                                                                     #
        #=====================================================================================#
        """
    )
    pilihan = int(input("   >>>    "))
    if pilihan == 00:
        basicOperator()
    elif pilihan == 99:
        exit()
    else:
        print("Pilihan Tidak Tersedia")
        perbandingan()

def penugasan():
    print(
        """
        #=====================================================================================#
        #                                                                                     #
        #                                                                                     #
        #                   " Assignment Operators/Operator Penugasan "                       #
        #                                                                                     #
        #                                                                                     #
        #           Bahasa Python mendukung tipe operator berikut                             #
        #                                                                                     #
        #                                                                                     #
        #       Asumsikan variabel a memiliki nilai 10 dan variabel b memiliki nilai 20       #
        #                                                                                     #
        #       [1]  =    (Menetapkan nilai dari operan sisi kanan ke operan sisi kiri)       #
        #                  Contoh : c = a + b memasukan nilai dari a + b ke c                 #
        #                                                                                     #
        #       [2]  +=   (Ini menambahkan operan kanan ke operan kiri dan menetapkan         #
        #                  hasilnya ke operan kiri)                                           #
        #                  Contoh : c += a sama seperti  c = c + a                            #
        #                                                                                     #
        #       [3]  *=   (Ini mengalikan operan kanan dengan operan kiri                     #
        #                  dan menetapkan hasil ke operan kiri)                               #
        #                  Contoh : c *= a sama seperti c = c * a                             #
        #                                                                                     #
        #       [4]  /=   (Ini membagi operan kiri dengan operan kanan                        #
        #                  dan menetapkan hasilnya ke operan kiri)                            #
        #                  Contoh : c /= a atau c = c/ac. /= a atau c = c/a                   #
        #                                                                                     #
        #       [5]  %=   (Dibutuhkan modulus menggunakan dua operan                          #
        #                  dan menetapkan hasilnya ke operan kiri)                            #
        #                  Contoh : c %= a sama seperti c = c % a                             #
        #                                                                                     #
        #       [6]  **=  (Melakukan penghitungan eksponensial (daya) pada operator           #
        #                  dan menetapkan nilai ke operan kiri)                               #
        #                  Contoh : c **= a sama seperti c = c ** a                           #
        #                                                                                     #
        #       [7]  //=  (Ini melakukan pembagian lantai pada operator                       #
        #                  dan menetapkan nilai ke operan kiri)                               #
        #                  Contoh : c //= a sama seperti c = c // a                           #
        #                                                                                     #
        #                                                                                     #
        #    [00]   Back                                                                      #
        #    [99]   Exit                                                                      #
        #                                                                                     #
        #                                                                                     #
        #=====================================================================================#
        """
    )
    pilihan = int(input("##>>>    "))
    if pilihan == 00:
        basicOperator()
    elif pilihan == 99:
        exit()
    else:
        print("Pilihan Tidak Tersedia")
        penugasan()

def logika():
    print(
        """
        #=====================================================================================#
        #                                                                                     #
        #                                                                                     #
        #                       " Logical Operators/Operator Logika "                         #
        #                                                                                     #
        #                                                                                     #
        #           Bahasa Python mendukung tipe operator berikut                             #
        #                                                                                     #
        #                                                                                     #
        #       Asumsikan variabel a memiliki nilai True dan variable b nilainya False        #
        #                                                                                     #
        #    [1]  and Logical AND                                                             #
        #         (Jika kedua operan benar maka kondisi menjadi benar)                        #
        #              Contoh : (a and b) is False                                            #
        #                                                                                     #
        #    [2]  or Logical OR                                                               #
        #         (Jika nilai dari dua operan tidak sama, maka kondisi menjadi benar)         #
        #              Contoh : (a or b) is True                                              #
        #                                                                                     #
        #    [3]  not Logical NOT                                                             #
        #         Digunakan untuk membalikkan status logika operannya)                        #
        #              Contoh : Not(a and b) is True                                          #
        #                                                                                     #
        #                                                                                     #
        #    [00]   Back                                                                      #
        #    [99]   Exit                                                                      #
        #                                                                                     #
        #                                                                                     #
        #=====================================================================================#
        """
    )
    pilihan = int(input("##>>>    "))
    if pilihan == 00:
        basicOperator()
    elif pilihan == 99:
        exit()
    else:
        print("Pilihan Tidak Tersedia")
        logika()

def keanggotaan():
    print(
        """
        #=====================================================================================#
        #                                                                                     #
        #                                                                                     #
        #                    " Membership Operators/Operator Keanggotaan "                    #
        #                                                                                     #
        #                                                                                     #
        #           Bahasa Python mendukung tipe operator berikut                             #
        #                                                                                     #
        #                                                                                     #
        #       Operator keanggotaan Python menguji keanggotaan secara berurutan,             #
        #       seperti string, daftar, atau tuple. Ada dua operator keanggotaan.             #
        #                                                                                     #
        #    [1]  in        (Mengevaluasi ke true, jika menemukan variabel                    #
        #                   dalam urutan yang ditentukan dan false sebaliknya)                #
        #         Contoh : x in y, di sini menghasilkan 1 jika x adalah anggota urutan y.     #
        #                                                                                     #
        #    [2]  not in    (Mengevaluasi ke true, jika tidak menemukan                       #
        #                   variabel dalam urutan yang ditentukan dan false sebaliknya)       #
        #         Contoh : x tidak dalam y, di sini tidak menghasilkan 1                      #
        #                  jika x bukan anggota urutan y.                                     #
        #                                                                                     #
        #                                                                                     #
        #    [00]   Back                                                                      #
        #    [99]   Exit                                                                      #
        #                                                                                     #
        #                                                                                     #
        #=====================================================================================#
        """
    )
    pilihan = int(input("##>>>    "))
    if pilihan == 00:
        basicOperator()
    elif pilihan == 99:
        exit()
    else:
        print("Pilihan Tidak Tersedia")
        keanggotaan()

def identitas():
    print(
        """
        #=====================================================================================#
        #                                                                                     #
        #                                                                                     #
        #                      " Identity Operators/Operator Identitas "                      #
        #                                                                                     #
        #                                                                                     #
        #           Bahasa Python mendukung tipe operator berikut                             #
        #                                                                                     #
        #                                                                                     #
        #       Operator keanggotaan Python menguji keanggotaan secara berurutan,             #
        #       seperti string, daftar, atau tuple. Ada dua operator keanggotaan.             #
        #                                                                                     #
        #    [1]  is        (Mengevaluasi ke true jika variabel di kedua sisi operator        #
        #                   menunjuk ke objek yang sama dan salah sebaliknya)                 #
        #         Contoh : x adalah y, berikut adalah hasil dalam 1                           #
        #                  jika id(x) sama dengan id(y).                                      #
        #                                                                                     #
        #    [2]  is not    (Mengevaluasi ke false jika variabel di kedua sisi operator       #
        #                   menunjuk ke objek yang sama dan benar sebaliknya)                 #
        #         Contoh : x tidak y, di sini tidak menghasilkan 1                            #
        #                  jika id(x) tidak sama dengan id(y).                                #
        #                                                                                     #
        #                                                                                     #
        #    [00]   Back                                                                      #
        #    [99]   Exit                                                                      #
        #                                                                                     #
        #                                                                                     #
        #=====================================================================================#
        """
    )
    pilihan = int(input("   >>>    "))
    if pilihan == 00:
        basicOperator()
    elif pilihan == 99:
        exit()
    else:
        print("Pilihan Tidak Tersedia")
        identitas()

def menu():
    print(
        """
        #=====================================================================================#
        #                                                                                     #
        #                                                                                     #
        #                                  " Python Basic "                                   #
        #                                                                                     #
        #                                                                                     #
        #                [1]     Variable                [9]     Dictionary                   #
        #                [2]     Basic Operator          [10]    Set                          #
        #                [3]     Decicion Making         [11]    Time & Date                  #
        #                [4]     Loops                   [12]    Function                     #
        #                [5]     Number                  [13]    Modules                      #
        #                [6]     String                  [14]    Files I/O                    #
        #                [7]     Lists                   [15]    Excepttion Handling          #
        #                [8]     Tuples                                                       #
        #                                                                                     #
        #                                                                                     #
        #                [99]     Exit                                                        #
        #                                                                                     #
        #                                                                                     #
        #=====================================================================================#
        """
    )
    pilihan = int(input("##>>>   ")) # dalam fungsi menu()
        # user diminta memilih program
    if pilihan == 00: # kondisi pertama yang harus dipenuhi saat fungsi menu() berjalan
        # jika user memasukan angka 00
        menu()
        # jalankan fungsi menu()
    elif pilihan == 1: # kondisi kedua yang harus dipenuhi jika kondisi pertama tidak terpenuhi
        # dan jika user memeasukan angka 1
        variabel()
        # jalankan fungsi variabel()
    elif pilihan == 2:
        basicOperator()
    elif pilihan == 99:
        exit()
    else:
        print("Maaf Pilihan Program Sedang Dalam Proses")
        menu()
