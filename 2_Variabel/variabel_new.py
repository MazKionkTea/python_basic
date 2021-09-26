########################################################################

#!/usr/bin/env python
# encoding: utf-8
"""
variabel.py

Created by MazKionkTea on 9/13/21.
Copyright (c) 2021 Copyright Holder. All rights reserved.
"""

########################################################################

def sparator(arg):
    ''' sparator '''
    print("#".center(72, "#"))
    print(arg.center(72, "#"))
    print("#".center(72, "#"))
sparator(" // Variabel // ")

variabel1 = '''
########################################################################

- Variabel

    variabel berfungsi untuk memesan runag pada memori yang bisa diisi
    dengan suatu nilai dan bisa dipakai secara berulang berulang.

    yang berarti saat kita membuat sebuah variabel, kita sudah memesan
    sebagian kecil ruang memori untuk dipakai dan diisi dengan
    sebuah nilai untuk kita pakai kembali.

########################################################################
'''

variabel2 = '''
########################################################################

- Menetapkan Nilai Kedalam Variabel

    tidak ada pernyataan eksplisit untuk membuat sebuah variabel,
    Deklarasi terjadi secara otomatis ketika kita menetapkan nilai
    untuk variabel. Tanda sama dengan (=) digunakan untuk
    menetapkan nilai dalam sebuah variabel.

    cara membuat variabel sangatlah mudah, hanya perlu mengetikan
    nama variabel diikuti tanda sama dengan dan nilai variabelnya.

    nilai variabel bisa diisi dengan nilai integer(bilangan bulat
    atau desimal), karakter, string, list, tuple dan dictionary.

    Contoh :

        name = "Hama Wereng"    # string
        tinggi = 157            # integer
        berat = 57,8            # float

        print (nama)
        print (tinggi)
        print (berat)

    ketika kode program dijalankan akan menghasilkan :

########################################################################
'''

variabel3 = '''
########################################################################

- Multiple Asignment

    python bisa menetapkan nilai tunggal untuk beberapa variabel.

    Contoh :

        a = b = c = 1

    disini, objek integer dibuat dengan nilai 1, dan semua variabel
    memiliki alokasi memory yang sama. kita juga bisa menetapkan
    beberapa objek untuk tiap variabel.

    contoh :

        a, b, c = 1, 2, "Ucup"

    Di sini, dua integer objek dengan nilai 1 dan 2 dimasukan ke variabel
    a dan b masing-masing, dan satu objek string dengan nilai "Ucup" 
    ditetapkan untuk variabel c. sama saja seperti :

        a = 1
        b = 2
        c = "Ucup"

    hanya saja penulisan yang sebelumnya dibuat dalam satu line.

########################################################################
'''

variabel4 = '''
########################################################################

- Tipe Data

    Data yang disimpan dalam memori dapat beragam jenis. Misalnya, 
    usia seseorang disimpan sebagai nilai numerik dan 
    alamatnya disimpan sebagai karakter alfanumerik. 
    Python memiliki beragam jenis data standar yang digunakan 
    untuk menentukan kemungkinan pengoperasian python 
    dan metode penyimpanan.

    Python memiliki lima standar tipe data :

         Numbers
         String
         List
         Tuple
         Dictionary

########################################################################
'''

variabel5 = '''
########################################################################

- Tipe Data Number

    tipe data number menyimpan nilai numerik. object number dibuat
    ketika kita menetapkan sebuah nilai. 

    Contoh :

        var1 = 1
        var2 = 10

    kita bisa menghapus yang mengacu kepada suatu object dengan
    menggunakan del statement. sintak untuk pernyataan del yaitu sbb :

        del var1, var2, var3....,

    Kita bisa menghapus satu objek tunggal atau beberapa objek dengan
    menggunakan pernyataan del (del statement). 

    Contoh :

        del var del var_a, var_b

    python mendukung tiga tipe numerik yang berbeda

        - int
        - float
        - complex

    dibawah ini adalah beberapa tipe number

        int			float			complex

        10			0.0			    3.14j
        100			15.20			45.j
        -786		-21.9			9.322e-36j
        080			32.3+e18		.876j
        -0480		-90.			-.6545+0j
        -0x260		-32.54e100		3e+26j
        0x69		70.2-E12		3.56e-7j

########################################################################
'''

variabel6 = '''
########################################################################

- Tipe Data String

    string dalam python diidentifikasi sebagai gabungan karakter
    yang diapit oleh tanda kutip (kutip satu atau kutip dua).
    subset dari string (beberapa bagian karakter dari sebuah string) 
    bisa diambil/dipisahkan dengan menggunakan operator irisan/slice
    ([ ] dan [ : ]) dengan indeks yang dimulai dari 0 (nol).

    tanda plus (+) adalah penggabungan/concatination sting operator dan
    tanda bintang/asterisk (*) adalah pengulangan/repetition operator.

    contoh :

        str ='Hello World!'
        print(str)	    # Prints semua string
        print(str[0])	# Prints karakter pertama string
        print(str[2:5])	# Prints karakter dimulai dari ke 3 sampai ke 5
        print(str[2:])	# Prints string dimulai dari karakter ke 3
        print(str*2)	# Prints string dua kali
        print(str + "TEST")	# Prints penggabungan 2 string

    ketika kode dijalankan akan menghasilkan :

########################################################################
'''

variabel7 = '''
########################################################################

- Tipe Data List

    tipe data list dalam python adalah tipe data yang paling sebaguna.
    untuk mengisi item pada list dengan menggunakan kurung siku ([]) 
    dan menggunakan koma (,) jika itemnya memiliki lebih dari satu nilai.

    list hamir sama dengan tipe data array pada pemrograman yang lain 
    seperti bahasa pemrograman C atau bahasa pemrograman yang lain. 
    yang memnedakannya adalah list bisa diisi dengan tipe data berbeda.

    nilai yang terkandung dalam list bisa diakses dengan menggunakan 
    operator slice/irisan ([ ] dan [ : ]) dengan indeks dimulai dengan 
    indeks 0 sebagai awal seperti tipe data string.

    Contoh :

        list1 = ['abc', 123, 1.23, 'Ucup', 12.3]
        list2 = [321, 'Nurdin']
        print(list1)         	# Prints semua elemen list
        print(list1[0])       	# Prints elemen pertama dari list
        print(list1[1:3])    	# Prints elemen mulai dari ke 2 - 3 
        print(list1[2:])     	# Prints element mulai dari elemen ke 3
        print(list2 * 2)    	# Prints list dua kali
        print(list1 + list2)    # Prints gabungan dua lists
        
    ketika kode dijalankan akan menghasilkan :

########################################################################
'''

variabel8 = '''
########################################################################

- Tipe Data Tuple

    Tuple adalah tipe data urutan lain yang sama seperti list. tuple 
    bisa di isi dengan beberapa nilai tipe data dan dipisah dengan koma 
    yang diapit oleh tanda kurung ( () ) yang berbeda dengan list
    yang diapit dengan tanda kurung siku/kotak ( [] ).

    yang paling membedakan dari list dan tuple adalah isi dari sebuah list 
    bisa dimodifikasi/diubah, sedangkan pada tuple isinya tidak bisa diubah 
    sama sekali (read-only).

    Contoh :
        
        tuple1 = ('abc', 123 , 1.23, 'Ucup', 12.3) 
        tuple2 = (321, 'Kosim') 
        print(tuple1)           # Prints semua isi tuple 
        print(tuple1[0])        # Prints elemen pertama dari tuple 
        print(tuple1[1:3])      # Prints elemen mulai dari ke 2 - 3  
        print(tuple1[2:])       # Prints elemen mulai dari elemen ke 3 
        print(tuple2 * 2)       # Prints tuple dua kali
        print(tuple1 + tuple2)  # Prints gabungan dua tuple 
        
    ketika kode dijalankan akan menghasilkan :

########################################################################
'''

variabel8_1 = '''
########################################################################

    kode dibawah adalah kode tidak valid dalam tuple, karena kita
    mencoba untuk merubah nilai tuple. sama kasusnya seperti pada list 
	
        tuple = ('abc', 123 , 1.23, 'john', 12.3) 
        list = ['abc', 123 , 1.23, 'john', 12.3] 
        tuple[2] = 1000    # Invalid syntax tuple 
        list[2] = 1000     # Valid syntax list 
	
    ketika kode diatas akan menghasilkan : error

########################################################################
'''

variabel9 = '''
########################################################################

- Tipe Data Dictionary

    Python dictionary adalah semacam tipe hash-table (tabel campuran). 
    tipe data ini bekerja seperti assosiative array atau hashes/campuran 
    yang dapat ditemukan pada bahasa pemrograman perl yang memiliki 
    key-value pair (pasangan kata kunci dan nilai). dictionary key hampir 
    bisa diisi dengan tipe data apapun. tetapi biasanya diisi dengan tipe 
    data number dan string. nilai dari dictionary bisa dapat diubah-ubah. 
    dictionary diapit dengan tanda kurung kurawal ( {} ) dan cara mengisi 
    dan mengakses nilainya dengan menggunakan tanda kurung siku ( [] ) 

    Contoh :

        dict1 = {} 
        dict1['tamvan'] = "aku orang tamvan" 
        dict1[2] = "indeks ke dua" 
        dict2 = {'nama':'michael','code':1234, 'pekerjaan':'gali kubur'} 
        print(dict1['tamvan'])    # Prints nilai untuk key 'tamvan' 
        print(dict1[2])           # Prints nilai untuk key 2
        print(dict2)              # Prints semua isi dari dictionary 
        print(dict2.keys())       # Prints semua keys (kata kunci)
        print(dict2.values())     # Prints semua values (nilai)

    Ketika kode dijalankan akan menghasilkan :

########################################################################
'''

variabel10 = '''
########################################################################

- Konversi Tipe Data

Terkadang kita butuh untuk bisa mengubah nilai atau tipe data menjadi 
tipe data yang lain. python memungkinkan kita untuk bisa merubah 
nilai atau tipe data menjadi tipe data yang lain dengan menggunakan 
built-in function yang telah disediakan oleh bahasa pemrograman ini.

Function
Description 

int(x [,base])
Converts x to an integer. The base specifies the base if x is a string. 

float(x)
Converts x to a floating-point number.

complex(real [,imag])
Creates a complex number.

str(x)
Converts object x to a string representation.

repr(x)
Converts object x to an expression string.

eval(str)
Evaluates a string and returns an object.

tuple(s)
Converts s to a tuple.

list(s)
Converts s to a list.

set(s)
Converts s to a set.

dict(d)
Creates a dictionary. d must be a sequence of (key,value) tuples.

frozenset(s)
Converts s to a frozen set.

chr(x)
Converts an integer to a character.

unichr(x)
Converts an integer to a Unicode character.

ord(x)
Converts a single character to its integer value.

hex(x)
Converts an integer to a hexadecimal string.

oct(x)
Converts an integer to an octal string.

########################################################################
'''



########################################################################

def overview():
    ''' overview '''
    print(variabel1)

def nilai_variabel():
    ''' Assigning Values to Variables '''
    print(variabel2)
    nama = "Hama Wereng"    # string
    tinggi = 157            # integer
    berat = 57,8            # float

    print(nama)
    print(tinggi)
    print(berat)

def multiple_assignment():
	''' multiple asignment '''
	print(variabel3)

def tipe_data():
	''' Standard Data Types '''
	print(variabel4)

def Python_number():
	''' Python Numbers '''
	print(variabel5)

def python_string():
	''' Python Strings '''
	print(variabel6)

	str ='Hello World!'
	print(str)	    # Prints semua string
	print(str[0])	# Prints karakter pertama string
	print(str[2:5])	# Prints karakter dimulai dari ke 3 sampai ke 5
	print(str[2:])	# Prints string dimulai dari karakter ke 3
	print(str*2)	# Prints string dua kali
	print(str + "TEST")	# Prints penggabungan 2 string

def python_list():
    ''' Python List '''
    print(variabel7)
    list1 = ['abc', 123 , 1.23, 'Ucup', 12.3]
    list2 = [321, 'Nurdin']
    print(list1)         	# Prints semua elemen list
    print(list1[0])       	# Prints elemen pertama dari list
    print(list1[1:3])    	# Prints elemen mulai dari ke 2 - 3 
    print(list1[2:])     	# Prints element mulai dari elemen ke 3
    print(list2 * 2)  	    # Prints list dua kali
    print(list1 + list2)    # Prints gabungan dua lists

def python_tuple():
    ''' Python Tuple '''
    print(variabel8)

    tuple1 = ('abc', 123 , 1.23, 'Ucup', 12.3) 
    tuple2 = (321, 'Kosim') 
    print(tuple1)           # Prints semua isi tuple 
    print(tuple1[0])        # Prints elemen pertama dari tuple 
    print(tuple1[1:3])      # Prints elemen mulai dari ke 2 - 3  
    print(tuple1[2:])       # Prints elemen mulai dari elemen ke 3 
    print(tuple2 * 2)       # Prints tuple dua kali
    print(tuple1 + tuple2)  # Prints gabungan dua tuple
    
    print(variabel8_1)
    
    try:
        tuple = ('abc', 123 , 1.23, 'Ucup', 12.3)
        list = ['abc', 123 , 1.23, 'Ucup', 12.3]
        tuple[2] = 1000    # Invalid syntax tuple
        list[2] = 1000     # Valid syntax list
    except TypeError:
        print("TypeError: 'tuple' object does not support item assingment")

def python_dictionary():
    ''' Python Dictionary '''
    print(variabel9)
    dict1 = {}
    dict1['tamvan'] = "aku orang tamvan" 
    dict1[2] = "indeks ke dua" 
    dict2 = {'nama':'michael','code':1234, 'pekerjaan':'gali kubur'} 
    print(dict1['tamvan'])       # Prints nilai untuk key 'tamvan' 
    print(dict1[2])           # Prints nilai untuk key 2
    print(dict2)              # Prints semua isi dari dictionary 
    print(dict2.keys())       # Prints semua keys (kata kunci)
    print(dict2.values())     # Prints semua values (nilai)

def konversi_tipe_data():
	''' Data Type Conversion '''
	print(variabel10)



########################################################################

# overview()
# nilai_variabel()
# multiple_assignment()
# tipe_data()
# Python_number()
# python_string()
# python_list()
# python_tuple()
# python_dictionary()
# konversi_tipe_data()

########################################################################

if __name__ == '__main__':
	print(__name__)