def sparator(arg = "#"):
    print("\n" * 3)
    print("#".center(59, "#"))
    print(arg.center(59, "#"))
    print("#".center(59, "#"))

def overview():
    sparator(" // Overview // ")
    print('''
    Tuple adalah sequence/urutan objek python immutable/abadi (tidak dapat diubah).
    Tuples adalah urutan, seperti list. Perbedaan utama mengenai tupel dan list adalah
    bahwa tupel tidak dapat diubah tidak seperti list. tuples sibungkus
    dengan menggunakan tanda kurung, sedangkan daftar menggunakan kurung persegi.

    Membuat tuple sesederhana menempatkan nilai yang dipisahkan koma yang berbeda. 
    Secara opsional, Anda dapat menempatkan nilai-nilai yang dipisahkan koma
    ini antara tanda kurung juga.
    
    Contoh :

        tup1 = ('physics','chemistry',1997,2000)
        tup2 = (1,2,3,4,5)
        tup3 ="a","b","c","d"

    Tuple kosong ditulis dengan dua tanda kurung yang tidak mengandung apa-apa.

        tup1 = ()

    untuk membuat tuple yang hanya memiliki satu nilai, kita harus memasukan sebuah koma 
    walapun kita hanya memiliki satu nilai.

        tup1 = (50, )

    seperti indeks pada string, tuple indeks dimulai dari 0. 
    tuple bisa diiris/slice, digabungkan/concatinated, dll.
    ''')



# Accessing Values in Tuples
def accsesing_tuple():
    sparator(" // Accessing Values in Tuples // ")
    print('''
    Untuk mengakses nilai dalam tuple, dengan cara menggunakan
    tanda kurung siku untuk mengiris berdasarkan indeks yang tesedia
    dalam indeks tersebut.

    Contoh :

        #!/usr/bin/python3
        tup1 = ('physics','chemistry',1997,2000)
        tup2 =(1,2,3,4,5,6,7)
        print("tup1[0]: ",tup1[0])
        print("tup2[1:5]: ",tup2[1:5])

    Ketika kode diatas dieksekusi akan menghasilkan :
    ''')

    #!/usr/bin/python3
    tup1 = ('physics','chemistry',1997,2000)
    tup2 =(1,2,3,4,5,6,7)
    print("tup1[0]: ",tup1[0])
    print("tup2[1:5]: ",tup2[1:5])



# Updating Tuples
def updating_tuple():
    sparator(" // Updating Tuple // ")
    print('''
    Tuple adalah tipe data yang immutable, artinya kita tidak bisa
    memperbaharui atau mengganti nilai dari elemen tuple.
    kita bisa mengambil bagian dari nilai tuple untuk membuat tuple baru.

    Contoh :

        #!/usr/bin/python3
        tup1 = (12,34.56)
        tup2 = ('abc','xyz')
        
        # Following action is not valid for tuples
        # tup1[0] = 100;
        
        # So let's create a new tuple as follows
        tup3 = tup1 + tup2
        print(tup3)

    Ketika kode diatas dieksekusi akan menghasilkan :
    ''')

    #!/usr/bin/python3
    tup1 = (12,34.56)
    tup2 = ('abc','xyz')
    
    # Following action is not valid for tuples
    # tup1[0] = 100;
    
    # So let's create a new tuple as follows
    tup3 = tup1 + tup2
    print(tup3)



# Delete Tuple Elements
def deleting_tuple():
    sparator(" // Deleting Tuple // ")
    print('''
    Menghapus bagian tuple sangat tidak mungkin, tapi secara eksplisit
    kita bisa menghapus seluruh tuple dengan menggunakan del statement.

    Contoh :

        #!/usr/bin/python3
        tup = ('physics','chemistry',1997,2000)
        print(tup)
        del tup
        print("After deleting tup : ")
        print(tup)

    Ketika kode diatas dieksekusi akan menghasilkan : error
    Catatan: Pengecualian/exception ditampilkan. Karena tup after del,
    tuple tidak ada lagi.
    ''')

    #!/usr/bin/python3
    tup = ('physics','chemistry',1997,2000)
    print(tup)
    try:
        del tup
        print("After deleting tup : ")
        print(tup)
    except:
        pass



# Basic Tuples Operations
def tuple_operation():
    sparator(" // Basic Tuple Operation // ")
    print('''
    Tuple mendukung + dan * operator sama seperti string.
    maksudnya adalah menggabungkan/concatination dan pengulangan/repetition
    kecuali menghasilkan tuple baru, bukan string.


    Python Expression           Results                         Description

    len((1, 2, 3))              3                               Length

    (1, 2, 3) + (4, 5, 6)       (1, 2, 3, 4, 5, 6)              Concatenation

    ('Hi!',) * 4                ('Hi!', 'Hi!', 'Hi!', 'Hi!')    Repetition

    3 in (1, 2, 3)              True                            Membership

    for x in (1,2,3):           
        print (x, end=' ')      1 2 3                           Iteration
    ''')



# Indexing, Slicing, and Matrixes
def tuple_indexing_slicing():
    sparator(" // Indexing, Slicing and Matrixes // ")
    print('''
    Indexing, Slicing, and Matrixes

    Karena tupel adalah urutan/aequence, pengindeksan dan mengiris 
    dengan cara yang sama untuk tupel seperti yang mereka lakukan untuk string,

    Dengan asumsi input berikut-

    T = ('C++','Java','Python')

    Python Expression   Results                 Description
    T[2]                'Python'                Offsets start at zero
    T[-2]               'Java'                  Negative: count from the right
    T[1:]               ('Java', 'Python')      Slicing fetches sections    
    ''')



# No Enclosing Delimiters
def enclosing_delimiters():
    sparator(" // No Enclosing Delimiter // ")
    print('''
    Tidak ada pembatas yang melampirkan 
    adalah satu set beberapa objek, yang dipisahkan koma,
    Ditulis tanpa mengidentifikasi simbol, I.E., tanda kurung siku untuk list,
    tanda kurung untuk tupel, dll., Default untuk tupel,
    seperti yang ditunjukkan dalam contoh pendek ini.    
    ''')



# Built-in Tuple Functions

# cmp(tuple1, tuple2)
# Tidak lagi tersedia di Python 3. 

# len(tuple)
# Memberikan panjang total tuple.
def tuple_len():
    sparator(" // Tuple len() Method // ")
    print('''
    Deskripsi :

        Menampilkan panjang total dari sebuah tuple

    sintaks :

        len(tuple)

    parameter ;

        tuple (tipe data tuple yang akan dihitung)

    Contoh :

        #!/usr/bin/python3
        tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc')
        print("First tuple length : ", len(tuple1))
        print("Second tuple length : ", len(tuple2))

    ketika kode dieksekusi akan menghasilkan :
    ''')
    
    #!/usr/bin/python3
    tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc')
    print("First tuple length : ", len(tuple1))
    print("Second tuple length : ", len(tuple2))



# max(tuple)
# Mengembalikan nilai item dari tuple dengan nilai maksimal.
def tuple_max():
    sparator(" // Tuple max() Method // ")
    print('''
    Deskripsi :

        Mengembalikan nilai maksimal dari sebuah elemen

    sintaks :

        max(tuple)

    parameter ;

        tuple (tipe data tuple yang akan dihitung)

    Contoh :

        #!/usr/bin/python3
        tuple1, tuple2 = ('maths', 'che', 'phy', 'bio'), (456, 700, 200)
        print("Max value element : ", max(tuple1))
        print("Max value element : ", max(tuple2))

    ketika kode dieksekusi akan menghasilkan :
    ''')

    #!/usr/bin/python3
    tuple1, tuple2 = ('maths', 'che', 'phy', 'bio'), (456, 700, 200)
    print("Max value element : ", max(tuple1))
    print("Max value element : ", max(tuple2))



# min(tuple)
# Mengembalikan nilai item dari tuple dengan nilai minimum.
def tuple_min():
    sparator(" // Tuple min() Method // ")
    print('''
    Deskripsi :

        Mengembalikan nilai minimal dari sebuah elemen

    sintaks :

        min(tuple)

    parameter ;

        tuple (tipe data tuple yang akan dihitung)

    Contoh :

        #!/usr/bin/python3
        tuple1, tuple2 = ('maths', 'che', 'phy', 'bio'), (456, 700, 200)
        print("min value element : ", min(tuple1))
        print("min valueelement : ", min(tuple2))

    ketika kode dieksekusi akan menghasilkan :
    ''')

    #!/usr/bin/python3
    tuple1, tuple2 = ('maths', 'che', 'phy', 'bio'), (456, 700, 200)
    print("min value element : ", min(tuple1))
    print("min valueelement : ", min(tuple2))



# tuple(seq)
# Mengubah list menjadi tuple.
def tuple_tuple():
    sparator(" // Tuple tuple() Method // ")
    print('''
    Deskripsi :

        Mengubah list menjadi tuple.

    sintaks :

        tuple(seq)

    parameter ;

        seq (daftar urutan yang akan diubah menjadi tuple)

    Contoh :

        #!/usr/bin/python3
        list1 = ['maths', 'che', 'phy', 'bio']
        tuple1 = tuple(list1)
        print("tuple elements : ", tuple1)

    ketika kode dieksekusi akan menghasilkan :
    ''')



def tuple_count():
    sparator(" // Tuple count() Method // ")
    print('''
    Deskripsi :

        mengembalikan berapa kali nilai tertentu muncul dalam tupel

    sintaks :

        tuple.count(value)

    parameter ;

        value (dibutuhkan. Item yang akan dicari)

    Contoh :

        thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
        x = thistuple.count(5)
        print(x)

    ketika kode dieksekusi akan menghasilkan :
    ''')

    thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
    x = thistuple.count(5)
    print(x)



def tuple_index():
    sparator(" // Tuple index() Method // ")
    print('''
    Deskripsi :

        menemukan kemunculan pertama dari nilai yang ditentukan.
        memunculkan exception jika nilainya tidak ditemukan.

    sintaks :

        tuple.index(value)

    parameter ;

        value (dibutuhkan. Item yang akan dicari)

    Contoh :

        thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
        x = thistuple.index(8)
        print(x)

    ketika kode dieksekusi akan menghasilkan :
    ''')

    thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
    x = thistuple.index(8)
    print(x)



########################################################################

# Python Tuple
overview()
accsesing_tuple()
updating_tuple()
deleting_tuple()
tuple_operation()
tuple_indexing_slicing()
enclosing_delimiters()

# Built-in Method
tuple_len()
tuple_max()
tuple_min()
tuple_tuple()
tuple_count()
tuple_index()

########################################################################
