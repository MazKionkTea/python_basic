#       // if... elif... else... //


"""
Pengambilan keputusan adalah, antisipasi kondisi yang terjadi 
selama pelaksanaan sebuah program dan tindakan tertentu 
yang diambil sesuai dengan kondisi.

Struktur keputusan mengevaluasi beberapa ekspresi 
yang menghasilkan TRUE atau FALSE sebagai hasilnya. 
kita perlu menentukan tindakan mana yang harus diambil 
dan pernyataan mana yang akan dijalankan jika hasilnya BENAR atau SALAH.

Berikut ini adalah bentuk umum dari struktur pengambilan keputusan 
khas yang ditemukan di sebagian besar bahasa pemrograman 

Bahasa pemrograman Python mengasumsikan nilai non-zero 
dan non-null sebagai TRUE, dan nilai zero atau null values sebagai nilai FALSE

Bahasa pemrograman Python menyediakan jenis pernyataan pengambilan keputusan berikut.

    if statements               Pernyataan if terdiri dari ekspresi Boolean diikuti oleh satu atau beberapa pernyataan.
    

        if expression:          # condition
            statement(s)        # action
        else:                   # if condition not fullfield
            statement(s)        # action

    
    
    if...else statements        Pernyataan if dapat diikuti oleh pernyataan opsional lainnya, yang dijalankan ketika ekspresi boolean FALSE.


        if condition1:          # condition 1
            action              # action
        elif condition2:        # if condition 1 not fullfield
            action              # action
        elif condition3:        # if condition 2 not fullfield
            action              # action
        else:                   # if all condition not fullfield
            action              # action



    nested if statements        Anda dapat menggunakannya jika atau jika pernyataan di dalam pernyataan lain jika atau jika pernyataan(s).


        if expression1:          # condition 1
            statement(s)         # action
            if expression1.1:    # making nested if to collecting data for condition1
                statement(s)     # action
            elif expression1.2:  # if condition 1.1 not fullfield
                statement(s)     # action
            else:                # if 1.1 and 1.2 condition in nested if not fullfield
                statement(s)     # action
        elif expression2:        # if condition 1 not fullfield
            statement(s)         # action
        else:                    # if all condition not fullfield
            statement(s)         # action



    // Single Statement Suites //

jika rangkaian klausa/ketentuan if hanya terdiri dari satu baris, 
ketentuan tersebut dapat menggunakan baris yang sama dengan pernyataan header.

contoh :

    #!/usr/bin/python3
    var = 100
    if ( var == 100 ) : print ("Value of expression is 100")
    print ("Good bye!")

jika kode ditas dieksekusi, akan menghasilkan tampilan dilayar sebagai berikut-

    Value of expression is 100
    Good bye!



"""




#       // stack and queues //


"""






"""