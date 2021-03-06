def sparator(arg):
    print("\n"* 3)
    print("#".center(59, "#"))
    print(arg.center(59, "#"))
    print("#".center(59, "#"))



def overview():
    sparator(" // Overview // ")
    print('''
    secara umum, statement/pernyataan sirksekusi sacara berurutan. statement/pernyataan
    dijalankan pertamakali, diikuti yang kedua dan seterusnya. mungkin ada situasi dimana
    kita membutuhkan suatu kode blok yang dijalankan secara berulang-ulang.

    bahasa python menyediakan berbagai macam kontrol struktur yang rumit dengan menggunakan
    banyak cara untuk menjalankan sebuah program.

    loop statement memungkinkan kita untuk menjalankan kode program secara berulang-ulang.
    python menyediakkan beberapa macam tipe loop/perulangan yang dibutuhkan tergantung program
    yang akan kita jalankan.

    // While Loop Statement //
    
        mengulang satu statement/pernyataan atau lebih atau grup dari sebuah statement.
        selama statement tertentu selalu memberikan hasil boolean True, maka blok kode
        programnya akan dieksekusi kecuali kenghasilkan boolean False.

    // For Loop Statement //

        menjalankan rangkaian dari sebuah statement/pernyataan secara berulang-ulang dan
        mempersingkat kode ynag mengatur loop variabel.

    // nested loop //

        pengulangan bersarang memungkinkan kita bisa menggunakan satu atau beberapa perulangan
        didalam while atau for loop lainnya.
    ''')



def while_loop():
    sparator(" // While Loop Statement // ")
    print('''
    while loop dalam python digunakan untuk menjalankan perulangan
    selama perulangan tersebut bernilai boolean true

    syntax while loop dalam python :

        while expresion/kondisi:
            statement(s)/pernyataan atau aksi

    statement(s)/pernyataan adalah, satu atau beberapa blok pernyataan
    dengan indentasi seragam. condition/kondisi atau ekspresi apapun
    dan true bukan zero value. loop akan terus diulangi jika kondisinya 
    bernilai true.

    ketika kondisi menjadi false, kontrol program akan dilewati kebaris 
    program selanjutnya mengikuti baris kode program.

    dalam python, semua pernyattaan yang diindentasikan oleh jumlah 
    ruang karakter yang sama setelah konstruksi pemrograman, dianggap 
    sebagai bagian dari satu blok kode. python menggunakan indentasi 
    sebagi metode pengelompokan pernyataan.

    kunci dari while loop adalah, loop/perulangan tidak akan berjalan 
    ketika kondisi menghasilkan boolean false. loop body akan dilewati 
    dan pernyataan pertama setelah loop akan dieksekusi.

    Contoh :

        #!/sur/bin/python3
        count = 0
        # basis
        while (count < 9):
        # selama count/0 kurang dari 9 (kondisi)
            print("the count is : ", count)
            # tampilkan nilai count (aksi)
            count = count + 1    
            # karena kondisi while diatas bernilai boolean true, 
            # maka count di basis awal akan ditambah satu, 
            # hasilnya akan dimasukan kedalam sebuah variabel 
            # yang diberi nama variabel count dan menggantikan 
            # count pada basis pertama. loop/perulangan akan
            # terus berlanjut sampai variabel count memiliki 
            # nilai yang tidak lebih dari 9.

        print("good bye")
        # karena perulangan terus berlanjut dan nilai count 
        # juga terus bertambah, maka jika nilai variabel count
        # akan melebihi angka 9 dan bernilai boolean false 
        # loop diatas akan dihentikan ketika nilai varibel count 
        # adalah 8

    ketika kode dijalankan akan menghasilkan :
    ''')

    #!/sur/bin/python3
    count = 0
    # basis
    while (count < 9):
    # selama count/0 kurang dari 9 (kondisi)
        print("the count is : ", count)
        # tampilkan nilai count (aksi)
        count = count + 1
        # karena kondisi while diatas bernilai boolean true,
        # maka count di basis awal akan ditambah satu,
        # hasilnya akan dimasukan kedalam sebuah variabel
        # yang diberi nama variabel count dan menggantikan
        # count pada basis pertama. loop/perulangan akan
        # terus berlanjut sampai variabel count memiliki
        # nilai yang tidak lebih dari 9.

    print("good bye")
    # karena perulangan terus berlanjut dan nilai count
    # juga terus bertambah, maka jika nilai variabel count
    # akan melebihi angka 9 dan bernilai boolean false
    # loop diatas akan dihentikan ketika nilai varibel count
    # adalah 8



def for_loop():
    sparator(" // For Loop Statements // ")
    print('''
    for loop memiliki kemampuan untuk melakukan iterasi/pengulangan
    atas item dari urutan apapun, list/daftar, atau string.

    Sintaks :

        for iterating_var in sequence:
            # variabel yang mendukung pengulangan dalam sebuah urutan
            statement(s)
            # jalankan sebuah aksi

    jika urutan berisi daftar ekspresi/ungkapan, urutan tersebut dievaluasi 
    terlebih dahulu. kemudian, item pertama dalam urutan 
    ditetapkan kedalam variabel iterasi/pengulangan iterating_var 
    selanjutnya, blok pernyataan dijalankan sampai seluruh 
    urutan habis,

    Contoh :

        >>> range(5)fungsi range()
        bult-in fungsi range() adalah fungsi yang tepat untuk 
        iterasi/pengulangan pada urutan angka. hal ini menghasilkan 
        iterator pengembangan aritmatika.

    Contoh :

        range(0,5)
        >>> list(range(5))
        [0,1,2,3,4]

    range() menghasilkan iterator utuk bilangan bulat ang dimulai 
    dari angka 0 sampai 4 untuk memperoleh daftar objek 
    urutan/rangkaian tersebut.

    untuk mendapatkan urutan list objek, maka ketik list(), 
    sekaarang daftar ini dapat diiterasi menggunakan for statement 

    contoh :

        >>> for var in list(range(5)):
                print(var)

    contoh :

        #!/usr/bin/python3
        for letter in "python":     #traversal of a string sequence
            print("current letter : ", letter)
        print()

        fruits = ["banana", "apple", "mango"]
        for fruit in fruits:        # traversal of list sequence
            print("current fruit : ", fruit)
        print("good bye")
    
    ketika kode dijalankan akan menghasilkan :
    ''')

    #!/usr/bin/python3
    for letter in "python":     #traversal of a string sequence
        print("current letter : ", letter)
    print()

    fruits = ["banana", "apple", "mango"]
    for fruit in fruits:        # traversal of list sequence
        print("current fruit : ", fruit)
    print("good bye")



def nested_loop():
    sparator(" // Nested Loop // ")
    print('''
    python memungkikan penggunaan satu loop di dalam loop lain. 

    Sintaks :

        for iterating_var in sequence:
            for iterating_var in sequence:
                statement(s)
            statement(s)

        while expression:
            while expression:
                statement(s)
            statement(s)

    catatan tentang loop bersarang adalah, kita dapat menempatkan 
    sema jenis loop didalam jenis loop lainnya. misalnya for loop 
    dapat berada dalam beberapa saat loop atau sebaliknya.

    contoh :

    program berikur menggunakan loop nestad-for 
    untuk menamilkan tabel perkalian 1- 10

        #!/usr/bin/python3
        import sys
        for in range(1,11):
            for j in range(1,11):
                k = j * j
                print(k, end=" ")
            print()

        # fungsi print() dalam loop ini memiliki end=" ". tujuannya adalah 
        # untuk menambakan spasi, bukan baris baru. oleh karena itu, 
        # angka akan muncul dalam satu baris.
        # print() terakhir akan dieksekusi pada akhir bagian dalam untuk loop.

    ketika kode dieksekusi akan menghasilkan :
    ''')

    #!/usr/bin/python3
    import sys
    for in range(1,11):
        for j in range(1,11):
            k = j * j
            print(k, end=" ")
        print()

    # fungsi print() dalam loop ini memiliki end=" ". tujuannya adalah 
    # untuk menambakan spasi, bukan baris baru. oleh karena itu, 
    # angka akan muncul dalam satu baris.
    # print() terakhir akan dieksekusi pada akhir bagian dalam untuk loop.



def single_suite_loop():
    sparator(" // Single Statement Suite // ")
    print('''
    hampir sama dengan if statement, jika suatu kondisi dalam
    while loop hanya terdiri dari satu statement/pernyataan,
    pernyataan tersebut bisa ditempatkan pada baris yang sama
    dengan while header.

    Contoh :

        #!/usr/bin/python3
        flag = 1
        while (flag): print("given flag is really true")
        print("good bye")
        # contoh loop seperti ini akan membawa kita kedalam infinity loop

    ketika kode dijalankan akan menghasilkan :
    ''')

    #!/usr/bin/python3
    flag = 1
    while (flag): print("given flag is really true")
    print("good bye")
    # contoh loop seperti ini akan membawa kita kedalam infinity loop



def else_loop():
    sparator(" // Using Else Statement in Loops // ")
    print('''
    Python mendukung else statement yang terkait dengan pernyataan loop

        - jika else statement digunakan dengan for loop,
        else statement dieksekusi ketika loop telah habis
        dari daftar iterasi/pengulangan.

        - jika else statement digunakan dengan while loop,
        else statement dieksekusi saat kondisi menjadi false.


    Contoh :

        #!/usr/bin/python3
        count = 0
        # basis awal
        while count < 5:
        # kondisi nilai variabel count harus kurang dari angka 5
            print(count, " is less than 5")
            count = count + 1
            # nilai variabel count akan ditambahkan 1 selama loop berlangsung
        else:
        # kondisi lain
            print(count, " is not less than 5")
            # menampilkan kelayar jika nilai varibel count
            # tidak lebih kecil dari angka 5

    ketika kode dijalankan akan menghasilkan :
    ''')

    #!/usr/bin/python3
    count = 0
    # basis awal
    while count < 5:
    # kondisi nilai variabel count harus kurang dari angka 5
        print(count, " is less than 5")
        count = count + 1
        # nilai variabel count akan ditambahkan 1 selama loop berlangsung
    else:
    # kondisi lain
        print(count, " is not less than 5")
        # menampilkan kelayar jika nilai varibel count
        # tidak lebih kecil dari angka 5
    
    print('''
    python mendukung else statement yang terkait dengan loop statement 

        - jika else statement digunakan dengan for loop, blok kode 
        else dijalankan hanya jika untuk loop berakhir secara normal 
        (dan bukan dengan break statement)
        
        - jika else statement digunakan dengan whilw loop, 
        else statement dijalankan ketika kondisi menjadi false.

    Contoh :

        #!/usr/bin/python3
        numbers = [1,2,3,4,5,6,7,8,9]
        for num in numbers:
            if num %2 == 0:
                print("the list contain an even number")
                break
        else:
            print("the list doesn't contain even number")
    ''')

    #!/usr/bin/python3
    numbers = [1,2,3,4,5,6,7,8,9]
    for num in numbers:
        if num %2 == 0:
            print("the list contain an even number")
            break
    else:
        print("the list doesn't contain even number")



def infinite_loop():
    sparator(" // Infinite Loop // ")
    print('''
    loop menjadi perulangan/loop yang tidak terbatas dan tidak
    akan berhenti jika sebuah kondisi tidak pernah menjadi false.
    maka, harus hati-hati dalam penggunaan loop.

    tapi infinite loop juga bisa berguna dalam pemrograman klien/server
    dimana klien atau server perlu berjalan secara terus menerus
    agar klien dan server bisa terus berkomunikasi kapanpun tanpa henti
    ketika diperlukan.


    Contoh :

        #!/usr/bin/python3
        var = 1
        while var == 1:
        # kondisi dimana nilai var harus bernilai 1
            num = int(input("enter a number : "))
            # user diminta memasukan sebuah angka dan dimsukan kedalam sebuah varibel
            # perulangan ini akan menjadi perulangan yang tidak terbatas
            # karena varibel num tidak berhubungn dengan while loop
            print("you entered number : ", num)
            # menampilkan ulang input yang simasukan oleh user

        print("good bye")
        # perintah ini tidak akan dieksekusi karena loopning diatas
        # akan selalu bernilai false, dan program hanya bisa
        # dihentikan secara paksa dengan cara menekan keyboard CTRL + C

    ketika kode dijalankan akan menghasilkan :
    ''')

    #!/usr/bin/python3
    var = 1
    while var == 1:
    # kondisi dimana nilai var harus bernilai 1
        num = int(input("enter a number : "))
        # user diminta memasukan sebuah angka dan dimsukan kedalam sebuah varibel
        # perulangan ini akan menjadi perulangan yang tidak terbatas
        # karena varibel num tidak berhubungn dengan while loop
        print("you entered number : ", num)
        # menampilkan ulang input yang simasukan oleh user

    print("good bye")
    # perintah ini tidak akan dieksekusi karena loopning diatas
    # akan selalu bernilai false, dan program hanya bisa
    # dihentikan secara paksa dengan cara menekan keyboard CTRL + C



def loop_control():
    sparator(" // Loop Control Statement // ")
    print('''
    loop control statement mengubah eksekusi dari urutan normalnya, 
    ketika eksekusi meniggalkan lingkup, semua objek yang dibuat dalam 
    lingkup tersebut dihancurkan.

    kontrol staement yang didukung python yaitu :

        - break statement
        mengakhiri loop statement dan mentransfer eksekusi 
        ke statement yang langsung mengikuti loop.
        
        - continue statement
        menyebabkan loop melewatkan sisa body loop dan segera 
        menguji ulang kondisinnya sebelum mengulangi,
        
        - pass statement
        pernyataan pass di python digunakan ketika pertnyataan 
        diperlukan secara sintatis, tetapi anda tidak ingin perintah 
        atau kode apapun dijalankan.
    ''')



def break_statement():
    sparator(" // Break Statement // ")
    print('''
    break digunakan untuk penghentian prematue dari loop saat ini. 
    setelah meninggalkan loop, eksekusi pada pernyataan berikutnya 
    dilanjutkan seperti pernyataan break tradisional di bahasa C.

    penggunaan break/istirahat yang paling umum adalah ketika 
    beberapa kondisi eksternal dipicu membutuhkan keluar terburu-buru 
    dari loop. break statement bisa digunakan baik dalam while dan for loop.

    jika menggunakan loop bersarang, break statement menghentikan 
    eksekusi loop terdalam dan mulai mengeksekusibaris kode berikutnya 
    setelah blok.

    Contoh :

        #!/usr/bin/python3
        # ex 1 :
        for letter in "python":
            if letter == "h":
                break
            print("current letter : ", letter)

        # ex 2:
        var = 10
        while var > 0:
            print("current variable value : ", var)
            var = var -1
            if var == 5:
                break
        print("good bye")

        # program berikut menunjukan penggunaan break dalam sebuah for loop 
        # iterasi/pengulangan dari sbuah list. pengguna memasukan angka yang 
        # sicari dalam daftar. jika ditemukan, maka loop diakhiri dengan pesan 
        # "dihentikan".

        #!/usr/bin/python3
        no = int(input("enter number : "))
        numbers = [1,2,3,4,5,6,7,8,9]
        for num in numbers:
            if num == no:
                print("number found in list")
                break
        else:
            print("number not found in list")

    ketika kode dijalankan akan menghasilkan :
    ''')

    #!/usr/bin/python3
    # ex 1 :
    for letter in "python":
        if letter == "h":
            break
        print("current letter : ", letter)

    # ex 2:
    var = 10
    while var > 0:
        print("current variable value : ", var)
        var = var -1
        if var == 5:
            break
    print("good bye")

    # program berikut menunjukan penggunaan break dalam sebuah for loop 
    # iterasi/pengulangan dari sbuah list. pengguna memasukan angka yang 
    # sicari dalam daftar. jika ditemukan, maka loop diakhiri dengan pesan 
    # "dihentikan".

    #!/usr/bin/python3
    no = int(input("enter number : "))
    numbers = [1,2,3,4,5,6,7,8,9]
    for num in numbers:
        if num == no:
            print("number found in list")
            break
    else:
        print("number not found in list")



def continue_statement():
    sparator(" // Continue Statement // ")
    print('''
    continue statement, mengembalikan kontrol ke awal loop saat ini. 
    ketika ditemui loop memulai iterasi/pengulangan berikutnya tanpa 
    mengeksekusi pernyataan yang tersisa dalam iterasi saat ini.
    continue statement bisa digunakan dalam while atau for loop.

    Contoh :

        #!/usr/bin/python3
        # ex 1
        for letter in "python":
            if letter == "h":
                continue
            print("current letter : ", letter)

        # ex 2
        var = 10
        while var > 0:
            var = var -1
            if var == 5:
                continue
            print("current variable value : ", var)
        print("good bye")
    
    ketika kode dijalankan akan menghasilkan :
    ''')

    #!/usr/bin/python3
    # ex 1
    for letter in "python":
        if letter == "h":
            continue
        print("current letter : ", letter)

    # ex 2
    var = 10
    while var > 0:
        var = var -1
        if var == 5:
            continue
        print("current variable value : ", var)
    print("good bye")



def pass_statement():
    sparator(" // Pass Statement // ")
    print('''
    pass digunakan ketika pernyataan diperlukan secara sintaksis tetapi anda tidak ingin 
    perintah atau kode apapun dijalankan.

    pass statement adalah operasi null; tidak ada yang terjadi ketika 
    mengeksekusi. pass statement juga berguna ditempat-tempat dimana 
    kode anda pada akhirnya akan pergi, tetapi belum ditulis.

    Contoh :

        #!/usr/bin/python3
        for letter in "python":
            if letter == "h":
                pass
                print("this is pass block")
            print("current letter : ", letter)

        print("good bye")

    ketika kode dijalankan akan menghasilkan : 
    ''')

    #!/usr/bin/python3
    for letter in "python":
        if letter == "h":
            pass
            print("this is pass block")
        print("current letter : ", letter)

    print("good bye")



def iterating_sequence_index():
    sparator(" // Iterating by Sequence Index // ")
    print('''
    cara alternatif iterasi melalui setiap item adalah 
    dengan index diimbangi kedalam urutan itu sendiri.

    Contoh :

        #!/usr/bin/python3
        fruits = ["banana", "apple", "mango"]
        for index in range(len(fruits)):
            print("current fruit : ", fruits[index])
        print("good bye")

        # mengabil bantuan dari fungsi len(), yeng menyediakan jumlah 
        # total elemen dalam tuple serta fungsi bawaan range() untuk 
        # memberi urutan aktual unruk iterasi.

    ketika kode dieksekusi akan menghasilkan :
    ''')

    #!/usr/bin/python3
    fruits = ["banana", "apple", "mango"]
    for index in range(len(fruits)):
        print("current fruit : ", fruits[index])
    print("good bye")

    # mengabil bantuan dari fungsi len(), yeng menyediakan jumlah 
    # total elemen dalam tuple serta fungsi bawaan range() untuk 
    # memberi urutan aktual unruk iterasi.



def iterator_and_generator():
    sparator(" // Iterator and Generator // ")
    print('''
    iterator adalah objek yang memungkinkan programer utuk melintasi 
    semua elemen dan koleksi, terlepas dari implementasi spesifiknya. 
    di python, ojek iteratir mengimplementasikan sua metode iter() dan next()

    string, list, atau tuple objek bisa digunakan untuk membuat iterator.

    Contoh :

        #!/usr/bin/python3
        import sys
        list = [1,2,3,4]
        it = iter(list)
        # this build an iterator object
        print(next(it))
        # prints next available element in iterator
        # iterator object can be traversed using regular for statement

        for x in it:
            print(x, end=" ")

        # or using next() function

        while True:
            try:
                print(next(it))
            except StopIteration:
                sys.exit()
                # you have to import sys module for this

        # generator adalah fungsi yang menghasilkan urutan nilai dengan 
        # menggunakan metode hasil.

        # ketika fungsi generator dipanggil, ia mengembalikan objek generator 
        # bahkan tanpa mengeksekusi fungsinya. ketika metode next() dipanggil 
        # untuk pertamakalinya, fungsi tersebut mulai dijalankanhingga mencapai 
        # pernyataan hasil yang mengembalikan nilai yang dihasilkan. 
        # hasil yang terus melacak yaitumengingat eksekusi terakhir dan panggilan 
        # next() kedua berlanjut dari nilai sebelmnya.

        import sys
        def fibonacci(n):
        # generator function
            a, b, counter = 0, 1, 0
            while true:
                if (counter > n):
                    return
                yield a
                a, b = b, a + b
                counter += 1
        f = fibonacci(5)
        # f is iterator object

        while true:
            try:
                print(next(f), end=" ")
            except StopIteration:
                sys.exit()
    
    ketika kode dijalankan akan menghasilkan :
    ''')

    #!/usr/bin/python3
    import sys
    list = [1,2,3,4]
    it = iter(list)
    # this build an iterator object
    print(next(it))
    # prints next available element in iterator
    # iterator object can be traversed using regular for statement

    for x in it:
        print(x, end=" ")

    # or using next() function

    while True:
        try:
            print(next(it))
        except StopIteration:
            sys.exit()
            # you have to import sys module for this

    # generator adalah fungsi yang menghasilkan urutan nilai dengan 
    # menggunakan metode hasil.

    # ketika fungsi generator dipanggil, ia mengembalikan objek generator 
    # bahkan tanpa mengeksekusi fungsinya. ketika metode next() dipanggil 
    # untuk pertamakalinya, fungsi tersebut mulai dijalankanhingga mencapai 
    # pernyataan hasil yang mengembalikan nilai yang dihasilkan. 
    # hasil yang terus melacak yaitumengingat eksekusi terakhir dan panggilan 
    # next() kedua berlanjut dari nilai sebelmnya.

    import sys
    def fibonacci(n):
    # generator function
        a, b, counter = 0, 1, 0
        while true:
            if (counter > n):
                return
            yield a
            a, b = b, a + b
            counter += 1
    f = fibonacci(5)
    # f is iterator object

    while true:
        try:
            print(next(f), end=" ")
        except StopIteration:
            sys.exit()



########################################################################

# Loops
overview()
while_loop()
for_loop()
nested_loop()
single_suite_loop()
else_loop()
infinite_loop()
loop_control()
break_statement()
continue_statement()
pass_statement()
iterating_sequence_index()
iterator_and_generator()

########################################################################
