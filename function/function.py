def sparator(arg = "#"):
    print("\n" * 3)
    print("#".center(59, "#"))
    print(arg.center(59, "#"))
    print("#".center(59, "#"))



def overview():
    sparator(" // Fungsi // ")
    print('''
    Fungsi adalah sebuah blok kode yang teratur, dan bisa dipakai
    secara berulang kali. menggunakan Fungsi dalam python menjadikan
    aplikasi kita lebih teratur. python menyediakan kita built-in fungsi
    seperti perintah print() dan lain-lain adalah yang bisa dipanggil
    atau dieksekusi berulang kali.

    tapi kita juga bisa membuat fungsi kita sendiri yang
    didefinisikan/ditetapkan oleh kita sendiri.
    ''')



    def mendefinisikan_fungsi():
        sparator(" // Mendefinisikan Sebuah Fungsi // ")
        print('''
        kita bisa mendefinisikan sebuah fungsi berdasarkan jenis fungsi itu sendiri.
        ada beberapa aturan jika ingin membuat sebuah fungsi dalam python

        > blok kode fungsi diawali dengan keyword def
        di'ikuti nama fungsi nya dilanjutkan dengan
        tanda kurung ( () ) diakhiri dengan titik dua (:)
        
        > apapun input parameter atau argumen harus
        ditempatkan didalam tanda kurung. kita juga bisa
        menentukan parameter didalam kurung tersebut.
        
        > statemen pertama dalam sebuah fungsi bisa
        saja opsional statement.
        
        > setiap kode fungsi dimulai dengan tanda titik
        dua (:) dan indentasi
        
        > statement dari return [expression] adalah akhir
        dari blok kode fungsi. sebagai pilihan, return
        expression/return statement tanpa argumen bisa
        dilewati, tetapi nilai dari return'nya bersifat none.
        
        Sintaks :
        
            def namaFungsi( parameter ):
                "function_docstring"
                function_suite
                return [expression]
                
                atau
                
            def namaFungsi(parameter):
                kondisi
                aksi
                return aksi
            
        secara default, parameter memiliki tingkah laku
        tergantun posisi dan didefinisikan dari fungsi tsb. 
        
        contoh:
        
            def printme(str):
                "tulisan ini dilewati dalam fungsi ini"
                print(str)
                return
            
            printme()
        
        berdasarkan contoh di atas, fungsi ini mengabil
        string parameter sebagai input dan akan dicetak
        dilayar setelah fungsinya di panggil.

        ketika kode dijalankan akan menampilkan :
        ''')

        def printme(str):
                print("tulisan ini dilewati dalam fungsi ini")
                print(str)
                return
            
        printme("ok")
        # karena contoh fungsi ini membutuhkan sebuah argumen/parameter
        # yang memiliki tipe data string (str) maka argumennya/parameter
        # harus diisi oleh string
    
    mendefinisikan_fungsi()



    def memangil_fungsi():
        sparator(" // Memangil Sebuah Fungsi // ")
        print('''
        mendefinisikan fungsi melalui nama, secara spesifik parameter tersebut
        dimasukan kedalam fungsi dan stuktur blok kode.
        dan cara mengeksekusi/memanggil fungsi tersebut dengan cara mengetikan
        nama dari fungsi tersebut. dari contoh fungsi di atas,
        kita cukup mengetikan printme(). karena fungsi di atas memiliki
        parameter str, berarti kita harus memasukan parameter string didalam
        tanda kurung tersebut. dan cara pemanggilannya printme("wkwkwkwk")
        ''')
    
    memangil_fungsi()



def pass_value():
    sparator(" // Referensi ass vs value // ")
    print('''
    Semua parameter (argumen) dalam bahasa python dilewati oleh referensi.
    Itu berarti jika kita mengubah apa yang membuat parameter mengacu
    pada suatu fungsi, Perubahan tersebut juga mencerminkan kembali
    fungsi panggilan.
    
    Contoh :

        #!/usr/bin/python3
        # mendefinisikan sebuah fungsi
        def changeme(mylist):
            "Ini mengubah daftar lulus ke fungsi ini"
            print("nilai didalam fungsi sebelum dirubah:", mylist)
            mylist[2] = 50
            print("Values inside the function after change:", mylist)
            return
            # sekarang kita isa memanggil fungsi changeme
            mylist = [10,20,30]
            changeme(mylist)
            print("Values outside the function:", mylist)

    ketika kode diatas dieksekusi akan menghasilkan :
    ''')

    #!/usr/bin/python3
    # mendefinisikan sebuah fungsi
    def changeme(mylist):
        "Ini mengubah daftar lulus ke fungsi ini"
        print("nilai didalam fungsi sebelum dirubah :", mylist)
        mylist[2] = 50
        print("nilai didalam fungsi setelah dirubah :", mylist)
        return
        # sekarang kita isa memanggil fungsi changeme
        mylist = [10,20,30]
        changeme(mylist)
        print("nilai diluar fungsi :", mylist)

    print('''
    Ada satu contoh lagi di mana argumen dilewati oleh referensi dan
    referensi ditimpa di dalam fungsi yang disebut
    
    Contoh :

        #!/usr/bin/python3
        def changeme(mylist):
            "Ini mengubah list melawati ke fungsi ini"
            mylist = [1,2,3,4]
            # Ini akan menetapkan referensi baru di myList
            print("Values inside the function :", mylist)
            return
            # Sekarang kita dapat memanggil fungsi changeme
            mylist = [10,20,30]
            changeme(mylist)
            print("nilai diluar fungsi :", mylist)
    
    parameter mylist dalam fungsi changeme adalah lokal walaupun
    mengubah mylist di dalam fungsi tersebut tidak memiliki efek kepada
    mylist.

    ketika kode dijalankan akan menghasilkan :
    ''')

    #!/usr/bin/python3
    def changeme(mylist):
        "Ini mengubah list melawati ke fungsi ini"
        mylist = [1,2,3,4]
        # Ini akan menetapkan referensi baru di myList
        print("Values inside the function :", mylist)
        return
        # Sekarang kita dapat memanggil fungsi changeme
        mylist = [10,20,30]
        changeme(mylist)
        print("nilai diluar fungsi :", mylist)



# Function Arguments
def function_argument():
    sparator(" // Function Argument // ")
    print('''
    kita bisa memangila sebuah fungsi dengan menggunakan mengikuti dari
    beberapa tipe argument formal.

        - fungsi yang menggunakan argument.
        - fungsi yang menggunakan keyword argument
        - fungsi yang menggunakan default argument
        - fungsi yang menggunakan variabel argument
    ''')



# Function Without Argument
def fungsi_tanpa_argument():
    sparator(" // Fungsi Tanpa Argument // ")
    print('''
    fungsi ini tidak memerlukan sebuah argument sebagai parameter ketika
    memanggilnya. argument adalah sebuah parameter yang dimasukan didalam
    tanda kurung setelah nama fungsi. dan caramemanggilnya hanya dengan
    mengeikan nama fungsi dan diikuti tanda kurung contohnya "nama_fungsi()"

    Contoh :

        def tanpa_argument():
            print("Ini adalah fungsi tanpa argument")

        tanapa_argument()
    
    ketika kode dijalankan akan menghasilkan :
    ''')

    print('''
    mendefinisikan sebuah fungsi yang diberinama "tanpa_argument"
    karena tidak memerlukan argumen maka ketika saat membuat
    sebuah fungsi, tanda kurungnya kosong.

    dan cara memangilnya juga hanya dengan menuliskan nama funsinya
    dan tanda kurung dikosongkan/tanpa diisi apapun.
    ''')

    def tanpa_argument():
        print("Ini adalah fungsi tanpa argument")

    tanpa_argument()
            


# Function With Argument
def fungsi_dengan_argument():
    sparator(" // Function Argument // ")
    print('''
    fungsi yang membutuhkan argument yang melewati sebuah fungsi dengan
    berdasarkan urutan posisi argument. untuk memangil fungsi printme()
    kita kita membutuhkan argumen, jika tidak diberikan sebuah argumen
    maka akan memunculkan syntax error pada layar.

    Contoh :

        #!/usr/bin/python3
        def printme(str):
            print('''
            # fungsi ini membutuhkan sebuah argumen yang memiliki
            # tipe data string. jika diberikan arguman maka akan
            # memunculkan syntax error.
            ''')
            # mencetak string yang dilewati fungsi ini
            print(str)
            return
            # lalu kita panggil fungsi printme()

    ketika kode dijalankan akan menghasilkan :

        Traceback(most recent call last):
            File "test.py", line 11, in<module>
                printme()
        
        TypeError: printme() missing 1 required positional argument:'str'

    hal ini terjadi karena kita tidak memberikan sebuah argumen
    "str" pada saat memanggil fungsi printme().
    jika kita memanggilnya dengan memberikan argumen maka tidak akan
    terjasi error. cara memanggil fungsi yang membutuhkan argumentt adalah

    contoh:

        printme("argument yang bertipe data string")
    ''')



# Function With Keyword Argument
def fungsi_dengan_keyword_argument():
    sparator(" // Fungsi Dengan Keyword Argument // ")
    print('''
    keyword argument terkait dengan cara sebuah fungsi dipanggil.
    ketika kita menggunakan keyword argument dalam pemanggilan fungsi,
    pemanggil mengidentifikasi argumen dengan nama parameter.
    
    Contoh :

        #!/usr/bin/python3
        def printme(str):
            print(str)
            return

        printme(str = "My string")

    contoh selanjutnya akan memnerikan sebuah gambaran yang jelas
    bahwa urutan dari sebuah parameter tidak menjadi masalah
    tetapi harus bergubungan antara argument dengan isi argument.

        #!/usr/bin/python3
        def printinfo(name, age):
            print("Name:", name)
            print("Age", age)
            return

        printinfo(age = 50, name = "miki")

    ketika kode dijalankan akan menghasilkan :
    ''')

    def printme(str):
        print(str)
        return
    printme(str = "My string")

    def printinfo(name, age):
        print("Name:", name)
        print("Age", age)
        return
    printinfo(age = 50, name = "miki")



# Function With Default Argument
def fungsi_dengan_default_argument():
    sparator(" // Fungsi Dengan Default Argument // ")
    print('''
    defult argument adalah sebuah argument yang menberikan nilai default.
    jika saat pemanggilan fungi dan argument sebagai parameter pada fungsi
    tidak diisi maka nilai default telah ditentukan pada saat membuat fungsi.

    Contoh :

        def printinfo(name, age = 35):
            print("Name:", name)
            print("Age ",age)
            return
            # Sekarang kita dapat memanggil fungsi printinfo
        printinfo(age = 50 ,name = "miki")
        # argumen diisi dengan lengkap maka nilai default akan digantilan
        printinfo(name = "miki")
        # argument hanya diisi dengan satu parameter maka nilai default
        # yang akan digunakan

    ketika kode dijalankan akan menghasilkan :
    ''')

    def printinfo(name, age = 35):
        print("Name:", name)
        print("Age ",age)
        return
        # Sekarang kita dapat memanggil fungsi printinfo
    printinfo(age = 50 ,name = "miki")
    # argumen diisi dengan lengkap maka nilai default akan digantilan
    printinfo(name = "miki")
    # argument hanya diisi dengan satu parameter maka nilai default
    # yang akan digunakan



# Function With Variable-length Argument
def fungsi_dengan_argumen_variabel():
    sparator("// Funsi Dengan Variable-length Argument // ")
    print('''
    kita mungkin membutuhkan untuk menjalankan sebuah fungsi dengan menggulakan
    banyak argument lalu menentukannya ketika mendefinisikan sebuah fungsi
    argumen ini disebut sebagai argument dengan variabel yang panjang
    dan tidak diberikan nama dalam mendefinisikan sebuah fungsi.

    Sintaks :

        def functionname([formal_args,]*var_args_tuple):
            "function_docstring"
            function_suite
            return [expression]

    sebuah tanda astrisk (*) ditampatkan sebelum nama variabel yang berlaku
    untuk semua nilai argument variabel non-kata kunci.
    Tuple ini tetap kosong jika tidak ada argumen tambahan yang ditentukan
    selama memanggil fungsi.

    Contoh :

        def printinfo(arg1, *vartuple):
            print("Output is:")
            print(arg1)
            for var in vartuple:
                print(var)
            return
            # Now you can call printinfo function
        printinfo(10)
        printinfo(70,60,50)

    ketika kode dijalankan akan menghasilkan :    
    ''')

    def printinfo(arg1, *vartuple):
        print("Output is:")
        print(arg1)
        for var in vartuple:
            print(var)
        return
        # Now you can call printinfo function
    printinfo(10)
    printinfo(70,60,50)



# Anonimous Function
def fungsi_anonim():
    sparator(" // Fungsi Anonim // ")
    print('''
    fungsi ini disebut sebagai fungsi anonom karena tidak dideklarasikan
    dalam gaya standar dalam meggnakan keyword def. kita bisa menggunakan
    keyword lamda untuk membuat fungsi anonim
    
        - Lambda dapat mengambil sejumlah argumen tetapi hanya mengembalikan
        satu nilai dalam bentuk ekspresi. Mereka tidak dapat mengandung
        perintah atau beberapa ekspresi.

        - Fungsi anonim tidak dapat dipanggil secara langsung untuk dicetak
        karena lambda memerlukan ekspresi.

        - Fungsi lambda memiliki namespace lokal mereka sendiri dan tidak dapat
        mengakses variabel selain dari daftar parameter mereka dan yang ada
        di namespace global.

        - Meskipun tampak bahwa lambda adalah versi satu baris dari suatu fungsi,
        mereka tidak setara dengan pernyataan inline di C atau C ++,
        yang tujuannya adalah untuk menumpuk fungsi lewat alokasi,
        selama doa untuk alasan kinerja

    Sintaks :

        lambda[arg1 [,arg2,.....argn]]:expression

    Contoh :

        sum = lambda arg1,arg2: arg1 + arg2
        # Now you can call sum as a function
        print("Value of total :", sum(10,20))
        print("Value of total :", sum(20,20))

    ketika kode dijalankan akan menghasilkan :
    ''')

    sum = lambda arg1, arg2: arg1 + arg2
    # Now you can call sum as a function
    print("Value of total :", sum(10,20))
    print("Value of total :", sum(20,20))



# Return Statement
def return_statement():
    sparator(" // Return Statement // ")
    print('''
    return statement [expression] tanda keluar dari suatu fungsi,
    secara opsional meneruskan ekspresi ke pemanggil.
    return statement tanpa argumen sama dengan return None.

    Contoh :

        sum = lambda arg1, arg2: arg1 + arg2
        # Now you can call sum as a function
        print("Value of total :", sum(10,20))
        print("Value of total :", sum(20,20))

    contoh yang diberikan tidak mengembalikan nilai apa pun.

        def sum(arg1, arg2):
            # Tambahkan parameter dan kembalikan.
            total = arg1 + arg2
            print("Inside the function :", total)
            return total
        # Sekarang kita dapat memanggil fungsi SUM
        total = sum(10, 20)
        print("Outside the function :", total)

    ketika kode dijalankan akan menghasilkan :
    ''')

    def sum(arg1, arg2):
        # Tambahkan parameter dan kembalikan.
        total = arg1 + arg2
        print("Inside the function :", total)
        return total
    # Sekarang kita dapat memanggil fungsi SUM
    total = sum(10, 20)
    print("Outside the function :", total)



# Scope Variabel
def scope_variabel():
    sparator(" // Scope Variabel // ")
    print('''
    Semua variabel dalam suatu program mungkin tidak dapat diakses
    Di semua lokasi dalam program itu. Ini tergantung di mana
    Anda telah menyatakan variabel.Ruang lingkup variabel menentukan
    Bagian dari program di mana Anda dapat mengakses variabel tertentu.
    Ada dua lingkasan dasar variabel dalam Python

        - Global variables
        - Local variables
    
    Global vs Local variabel

    Variabel yang didefinisikan di dalam body fungsi memiliki ruang
    lingkup lokal, dan yang didefinisikan di luar memiliki ruang lingkup global.
    Ini berarti bahwa variabel lokal hanya dapat diakses di dalam fungsi
    di mana mereka dinyatakan, di mana variabel global dapat diakses
    sepanjang tubuh program dengan semua fungsi. Saat kita memanggil fungsi,
    variabel-variabel yang dinyatakan di dalamnya dibawa ke ruang lingkup.

    Contoh :

        total = 0
        # Ini adalah variabel global.
        def sum(arg1, arg2):
            # Tambahkan parameter dan kembalikan.
            total = arg1 + arg2
            # Di sini total variabel lokal.
            print("Inside the function local total :", total)
            return total
        # sekarang kita bisa memanggila fungsi sum
        sum(10,20)
        print("Outside the function global total :",total)
    
    ketika kode dijalankan akan menghailkan :
    ''')

    total = 0
    # Ini adalah variabel global.
    def sum(arg1, arg2):
        # Tambahkan parameter dan kembalikan.
        total = arg1 + arg2
        # Di sini total variabel lokal.
        print("Inside the function local total :", total)
        return total
    # sekarang kita bisa memanggila fungsi sum
    sum(10,20)
    print("Outside the function global total :",total)



########################################################################

# Function
overview()
pass_value()
function_argument()
fungsi_tanpa_argument()
fungsi_dengan_argument()
fungsi_dengan_keyword_argument()
fungsi_dengan_default_argument()
fungsi_dengan_argumen_variabel()
fungsi_anonim()
return_statement()
scope_variabel()

########################################################################
