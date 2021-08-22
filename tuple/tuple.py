def sparator(str):
    print("\n", str.center(59, "#"), "\n")
sparator(" // test // ")

def overview1():
    sparator(" // Overview // ")
    print(
"""
Tuple adalah sequence/urutan objek python immutable/abadi (tidak dapat diubah). Tuples adalah urutan, seperti list.
Perbedaan utama mengenai tupel dan list adalah bahwa tupel tidak dapat diubah tidak seperti list. 
tuples sibungkus dengan menggunakan tanda kurung, sedangkan daftar menggunakan kurung persegi.

Membuat tuple sesederhana menempatkan nilai yang dipisahkan koma yang berbeda. 
Secara opsional, Anda dapat menempatkan nilai-nilai yang dipisahkan koma ini antara tanda kurung juga.
Sebagai contoh-

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

"""
    )

# overview1()



def accsesingTuple():
    sparator(" // Accessing Values in Tuples // ")
    print(
# Accessing Values in Tuples
"""
Mengakses nilai dalam tupel

Untuk mengakses nilai dalam tuple, dengan cara menggunakan tanda kurung siku untuk mengiris 
berdasarkan indeks  yang tesedia dalam indeks tersebut.

Contoh :

    #!/usr/bin/python3
    tup1 = ('physics','chemistry',1997,2000)
    tup2 =(1,2,3,4,5,6,7)
    print("tup1[0]: ",tup1[0])
    print("tup2[1:5]: ",tup2[1:5])

Ketika kode diatas dieksekusi akan menghasilkan :
"""
    )

    #!/usr/bin/python3
    tup1 = ('physics','chemistry',1997,2000)
    tup2 =(1,2,3,4,5,6,7)
    print("tup1[0]: ",tup1[0])
    print("tup2[1:5]: ",tup2[1:5])

#accsesingTuple()



def updatingTuple():
    sparator(" // Updating Tuple // ")
    print(
# Updating Tuples
"""
Memperbarui Tuples.

Tuple adalah tipe data yang immutable, artinya kita tidak bisa memperbaharui atau mengganti nilai dari elemen tuple.
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
"""
    )

    #!/usr/bin/python3
    tup1 = (12,34.56)
    tup2 = ('abc','xyz')
    
    # Following action is not valid for tuples
    # tup1[0] = 100;
    
    # So let's create a new tuple as follows
    tup3 = tup1 + tup2
    print(tup3)

#updatingTuple()



def delTuple():
    sparator(" // Deleting Tuple // ")
    print(
# Delete Tuple Elements
"""
Menghapus elemen tuple

Menghapus bagian tuple sangat tidak mungkin, tapi secara eksplisit kita bisa menghapus seluruh tuple 
dengan menggunakan del statement.

Contoh :

    #!/usr/bin/python3
    tup = ('physics','chemistry',1997,2000)
    print(tup)
    del tup
    print("After deleting tup : ")
    print(tup)

Ketika kode diatas dieksekusi akan menghasilkan : error
Catatan: Pengecualian/exception ditampilkan. Karena tup after del, tuple tidak ada lagi.
"""
    )

    #!/usr/bin/python3
    tup = ('physics','chemistry',1997,2000)
    print(tup)
    try:
        del tup
        print("After deleting tup : ")
        print(tup)
    except:
        pass

#delTuple()



# Basic Tuples Operations
"""
Operasi tupel dasar

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
"""




# Indexing, Slicing, and Matrixes
"""
Indexing, Slicing, and Matrixes

Karena tupel adalah urutan/aequence, pengindeksan dan mengiris 
dengan cara yang sama untuk tupel seperti yang mereka lakukan untuk string,

Dengan asumsi input berikut-

T = ('C++','Java','Python')

Python Expression           Results                         Description
T[2]                        'Python'                        Offsets start at zero
T[-2]                       'Java'                          Negative: count from the right
T[1:]                       ('Java', 'Python')              Slicing fetches sections

"""



# No Enclosing Delimiters
"""
Tidak ada pembatas yang melampirkan 
adalah satu set beberapa objek, yang dipisahkan koma,
Ditulis tanpa mengidentifikasi simbol, I.E., tanda kurung siku untuk list,
tanda kurung untuk tupel, dll., Default untuk tupel, seperti yang ditunjukkan dalam contoh pendek ini.
"""

# Built-in Tuple Functions

# cmp(tuple1, tuple2)
# Tidak lagi tersedia di Python 3. 

# len(tuple)
# Memberikan panjang total tuple.

# max(tuple)
# Mengembalikan nilai item dari tuple dengan nilai maksimal.

# min(tuple)
# Mengembalikan nilai item dari tuple dengan nilai minimum.

# tuple(seq)
# Mengubah list menjadi tuple.


# Tuple len() Method

# Description
# The len()method returns the number of elements in the tuple.

# Syntax
# Following is the syntax for len() method-len(tuple)

# Parameters
# tuple-This is a tuple for which number of elements to be counted.
