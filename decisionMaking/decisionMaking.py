def sparator(arg = "#"):
    print("\n" * 3)
    print("#".center(59, "#"))
    print(arg.center(59, "#"))
    print("#".center(59, "#"))



def overview():
    sparator(" // Overview // ")
    print('''
    decision making (pengambilan keputusan) adalah antisipasi dari sebuah kondisi
    yang terjadi ketika menjalankan sebuah program dan menententukan aksi
    tergantung dari sebuah/suatu kondisi.

    struktur keputusan menilai beberapa expression/ungkapan/satement yang menghasilkan
    True atau False. kita harus menentukan aksi apa yang akan diambil dari statement
    untuk dijalankan ketika hasilnya True atau False dan sebaliknya.

    bahasa pemrograman python menganggap apapun nilai non-zero dan mom-null
    sebagai True dan zero atau null value sebagai False. bahasa pemrograman
    python menyediakan beberapa dari statement pengambilan keputusan.

        if statement
        (sebuah if statement terdiri dari boolean exspression yang diikuti
        omeh satu atau banyak statement)

        if...else statement
        (if statement bisa diikuti dengan opsional else statement. yang dijalankan
        ketika boolean expression hasilnya False)

        nested if statement
        (kita bisa menggunakan satu if atau else statement didalam if atau else if yang lain)
    ''')



def if_statement():
    sparator(" // if Statement // ")
    print('''
    if statement hampir sama dengan bahase pemrograman yang lain. if statement terdapat
    sebuah logocal expression (ungkapan logis) menggunakan sebuah data yang dibandingkan
    dan sebuah keputusan akan diambil berdasarkan hasil dari sebuah perbandingan

    Sintaks :

        if expression:
            statement(s)

    atau untuk lebih mudah dipahami dengan cara dibawah :

        if kondisi:
            # sebuah kondisi yang menghasilkan nilai boolean True atau False
            aksi
            # jalankan aksi

        atau

        if syarat:
            # dibutuhkan syarat yang hasilnya terpenuhi atau tidak terpenuhi
            jalankan aksi
            # jalankan aksi

    jika boolean expression True, maka blok statement(s) didalam if statement
    dijalankan. dalam python statement didalam sebuah blok ditentukan dengan
    indentasi setelah simbol semi colon (:). jika boolean expression False, maka
    set kode pertama setelah akhir blok dijalankan.

    Contoh :

        #!/usr/bin/python3
        var1 = 100
        if var1:
            print("i got a true expression value")
            print(var1)

        var2 = 0
        if var2:
            print("2 -Got a true expression value")
            print(var2)
            print("Good bye!")

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

    ketika kode dijalankan akan menghasilkan :
    ''')

    #!/usr/bin/python3
    var1 = 100
    if var1:
        print("i got a true expression value")
        print(var1)

    var2 = 0
    if var2:
        print("2 -Got a true expression value")
        print(var2)
        print("Good bye!")

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



def if_elif_else():
    sparator(" // if...elif...else Statement // ")
    print('''
    sebuah else statement bisa digabungkan dengan if statement. sebuah else statement
    terdapat blok kode yang akan dijalankan jika conditional expression (ungkapan kondisi)
    dalam if statement menghasilkan nilai 0 atau False. else statement adalan
    optional statement dan bisa menggunalan satu else dalam if statement.

    Sintaks :

        if expression:
            statement(s)
        else:
            statement(s)

            atau

        if statement/kondisi:
            action/aksi
        else:
            action/aksi

    Contoh :

        #!/usr/bin/python3
        amount = int(input("Enter amount: "))
        if amount<1000:
            discount = amount*0.05
            print("Discount",discount)
        else:
            discount = amount*0.10
            print("Discount",discount)
            print("Net payable:",amount-discount)

        # Dalam contoh di atas, diskon dihitung pada input amount.
        # Peringkat dari discount adalah 5%, Jika jumlahnya kurang dari 1000, dan 10% jika di atas 10.000.

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

    ketika kode dijalankan akan menghasilkan :
    ''')

    #!/usr/bin/python3
    amount = int(input("Enter amount: "))
    if amount<1000:
        discount = amount*0.05
        print("Discount",discount)
    else:
        discount = amount*0.10
        print("Discount",discount)
        print("Net payable:",amount-discount)

    # Dalam contoh di atas, diskon dihitung pada input amount.
    # Peringkat dari discount adalah 5%, Jika jumlahnya kurang dari 1000, dan 10% jika di atas 10.000.

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



def elif_statement():
    sparator(" // elif Statement // ")
    print('''
    elif Statement memungkinkan kita untuk memeriksa beberapa ekspresi
    True dan menjalankan blok kode segera setelah salah satu kondisi mengevaluasi menjadi True

    Mirip dengan else, elif statement adalah opsional. Namun, tidak seperti else,
    Untuk yang ada di sebagian besar pernyataan, Mungkin ada nomor arbitray (berubah-ubah)
    dari elif statements Mengikuti if.

    Sintak :

        if expression1:
            statement(s)
        elif expression2:
            statement(s)
        elif expression3:
            statement(s)
        else:
            statement(s)
            
            atau

        if expression1/kondisi1:
            action/aksi
        elif expression2/kondisi2:
            action/aksi
        elif expression3/kondisi3:
            action/aksi
        else:
            action/aksi

    Inti python tidak memberikan switch atau case statements seperti dalam bahasa lain,
    tetapi kita dapat menggunakan if...statements untuk mensimulasikan switch case sebagai berikut :

    Contoh :

        #!/usr/bin/python3
        amount = int(input("Enter amount: "))
        if amount<1000:
            discount = amount*0.05
            print("Discount",discount)
        elif amount<5000:
            discount = amount*0.10
            print("Discount",discount)
        else:
            discount = amount*0.15
            print("Discount",discount)
        print("Net payable:",amount-discount)

    ketika kode dijalankan akan menghasilkan :
    ''')

    #!/usr/bin/python3
    amount = int(input("Enter amount: "))
    if amount<1000:
        discount = amount*0.05
        print("Discount",discount)
    elif amount<5000:
        discount = amount*0.10
        print("Discount",discount)
    else:
        discount = amount*0.15
        print("Discount",discount)
    print("Net payable:",amount-discount)



def nested_if_statements():
    sparator(" // Nested if Statements // ")
    print('''
    Mungkin ada situasi ketika kita ingin memeriksa kondisi lain setelah kondisi menjadi True.
    Dalam situasi seperti itu, kita dapat menggunakan konstruksi if bersarang.
    Dalam konstruksi if bersarang, kita dapat memiliki konstruksi if...elif...else di dalam
    konstruksi if...elif...else lain.

    Sintak :

        if expression1:
            statement(s)
            if expression1:
                statement(s)
            elif expression2:
                statement(s)
            elif expression3:
                statement(s)
            else:
                statement(s)
        elif expression2:
            statement(s)
        else:
            statement(s)
            
            atau

        if expression1/kondisi1:
            action/aksi
            if expression1/kondisi1:
                action/aksi
            elif expression2/kondisi2:
                action/aksi
            elif expression3/kondisi3:
                action/aksi
            else:
                action/aksi
        elif expression2/kondisi2:
            action/aksi
        else:
            action/aksi

    Contoh :

        # !/usr/bin/python3
        num=int(input("enter number"))
        if num %2 == 0:
            if num %3 == 0:
                print("Divisible by 3 and 2")
            else:
                print("divisible by 2 not divisible by 3")
        else:
            if num %3 == 0:
                print("divisible by 3 not divisible by 2")
            else:
                print("not Divisible by 2 not divisible by 3")

    ketika kode dijalankan akan menghasilkan :
    ''')

    # !/usr/bin/python3
    num=int(input("enter number"))
    if num %2 == 0:
        if num %3 == 0:
            print("Divisible by 3 and 2")
        else:
            print("divisible by 2 not divisible by 3")
    else:
        if num %3 == 0:
            print("divisible by 3 not divisible by 2")
        else:
            print("not Divisible by 2 not divisible by 3")



def single_statement_suites():
    sparator(" // Single Statement Suites // ")
    print('''
    Jika rangkaian if clause (ketentuan) hanya terdiri dari satu baris,
    ia mungkin berada pada baris yang sama dengan pernyataan header.
    Berikut adalah contoh satu baris if clause.

    Contoh :

        #!/usr/bin/python3
        var = 100
        if (var == 100): print("Value of expression is 100")
        print("Good bye!")

    ketika kode dijalankan akan menghasilkan :
    ''')

    #!/usr/bin/python3
    var = 100
    if (var == 100): print("Value of expression is 100")
    print("Good bye!")



########################################################################

# Decision Making
overview()
if_statement()
if_elif_else()
elif_statement()
nested_if_statements()
single_statement_suites()

########################################################################
