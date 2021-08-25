def sparator(arg):
	print("\n", arg.center(59, "#"), "\n")

def overview():
	sparator(" // Variable // ")
	print(
	"""
variable berfungsi untuk memesan runag pada memori
yang bisa diisi dengan suatu nilai dan bisa dipakai
secara berulang berulang.

yang berarti saat kita membuat sebuah variabel,
kita sudah memesan sebagian kecil rung memori
untuk dipakai dan diisi dengan sebuah nilai
untuk kita pakai kembali
	"""
	)

overview()



# Assigning Values to Variables
def assigningVariable():
	sparator(" // menetapkan nilai variabel // ")
	print(
	"""
tidak ada pernyataan eksplisit untuk membuat
sebuah variabel,Deklarasi terjadi secara otomatis
ketika kita menetapkan nilai untuk variabel.
Tanda sama dengan (=) digunakan untuk
menetapkan nilai dalam sebuah variabel.

cara membuat variabel sangatlah mudah,
hanya perlu mengetikan nama variabel,
diikuti tanda sama dengan dan nilai variabelnya.

nilai variabel bisa diisi dengan nilai
integer(bilangan bulat atau desimal), karakter,
string, list, tuple dan dictionary.

Contoh :

	counter = 1000      integer
	miles = 100.0       float
	name = "john"       string

	print (counter)
	print (miles)
	print (name)

hasil yang akan tampil di layar adalah :
	"""
	)

	counter = 1000     # integer
	miles = 100.0      # float
	name = "john"      # string

	print (counter)
	print (miles)
	print (name)

assigningVariable()



# multiple asignment
def multipleAsignment():
	sparator(" // multiple asignment // ")
	print(
	"""
python memunginkan kita bisa menetapkan nilai
tunggal untuk beberapa variabel.

Contoh :

	a = b = c = 1

disini, objek integer dibuat dengan nilai 1,
dan semua tiga variabel ditugaskan kedalam
alokasi memory yang sama. kita juga bisa menetapkan
beberapa objek untuk tiap variabel.

contoh :

	a, b, c = 1, 2, "john"

Di sini, dua integer objek dengan nilai 1 dan 2 
ditugaskan untuk variabel a dan b masing-masing, 
dan satu objek string dengan nilai "john" 
ditetapkan untuk variabel c.
	"""
	)

multipleAsignment()



# Standard Data Types
def dataType():
	sparator(" // Standard Data Types // ")
	print(
	"""
Data yang disimpan dalam memori dapat beragam jenis. Misalnya, 
usia seseorang disimpan sebagai nilai numerik dan 
alamatnya disimpan sebagai karakter alfanumerik. 
Python memiliki beragam jenis data standar yang digunakan 
untuk menentukan kemungkinan pengoperasian python 
dan metode penyimpanan.

Python memiliki lima tipe data standar

	 Numbers
	 String
	 List
	 Tuple
	 Dictionary

	"""
	)

dataType()



# Python Numbers
def PythonNumber():
	sparator(" // Python Numbers // ")
	print(
	"""
tipe data number menyimpan nilai numerik. 
object number dibuat ketika kita menetapkan sebuah nilai. 

Contoh :

	var1 = 1
	var2 = 10

kita bisa menghapus yang mengacu kepada
suatu object dengan menggunakan del statement. 
sintak untuk pernyataan del yaitu sbb :

	del var1[,var2[,var3[....,varN]]]]

Kita bisa menghapus satu objek tunggal atau 
beberapa objek dengan menggunakan pernyataan del. 

Contoh :

	del var del var_a, var_b

python mendukung tiga tipe numerik yang berbeda

	- int
	- float
	- complex

dibawah ini adalah beberapa tipe number

	int			float			complex

	10			0.0			3.14j
	100			15.20			45.j
	-786			-21.9			9.322e-36j
	080			32.3+e18		.876j
	-0480			-90.			-.6545+0j
	-0x260			-32.54e100		3e+26j
	0x69			70.2-E12		3.56e-7j
	"""
	)

PythonNumber()



# Python Strings
def pythonString():
	sparator(" // Python String // ")
	print(
	"""
string dalam python diidentifilasi sebagai gabungan karakter
yang diapit oleh tanda kutip (kutip satu atau kutip dua).
subset dari sebuah string (beberapa bagian karakter dari sebuah string) 
bisa diambil/dipisahkan dengan menggunakan operator irisan/slice ([ ] dan [ : ]) 
dengan indeks yang dimulai dari 0 (nol) sebagai awal dari indeks.

tanda plus (+) adalah penggabungan/concatination sting operator 
dan tanda bintang/asterisk (*) adalah pengulangan/repetition operator.open

contoh :

	#!/usr/bin/python3
	str ='Hello World!'
	print(str)	# Prints complete string
	print(str[0])	# Prints first character of the string
	print(str[2:5])	# Prints characters starting from 3rd to 5th
	print(str[2:])	# Prints string starting from 3rd character
	print(str *2)	# Prints string two times
	print(str +"TEST")	# Prints concatenated string

ketika kode dieksekusi akan menghasilkan :
	"""
	)

	#!/usr/bin/python3
	str ='Hello World!'
	print(str)	# Prints complete string
	print(str[0])	# Prints first character of the string
	print(str[2:5])	# Prints characters starting from 3rd to 5th
	print(str[2:])	# Prints string starting from 3rd character
	print(str *2)	# Prints string two times
	print(str +"TEST")	# Prints concatenated string

pythonString()



# Python Lists
def pythonList():
	sparator(" // Python List // ")
	print(
	"""
tipe data list dalam python adalah tipe data yang paling sebaguna.
untuk mengisi item pada list hanya dengan menggunakan kurung siku ([]) 
dan menggunakan koma (,) jika itemnya memiliki lebih dari satu nilai.

list hamir sama dengan tipe data array pada bahas pemrograman yang lain 
seperti bahasa pemrograman C atau bahasa pemrograman yang lain. 
yang memnedakannya adalah bahwa list bisa diisi dengan tipe data yang berbeda. 

nilai yang terkandung dalam list bisa diakses dengan menggunakan 
operator slice/irisan ([ ] dan [ : ]) dengan indeks yang dimulai dengan 
indeks 0 sebagai awal. tanda plus (+) berfungsi untuk menggabungkan/concatination 
dan tanda bintang/asterisk (*) berfungsi untuk pengulangan/repetition operator.

Contoh :

	#!/usr/bin/python3
	list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
	tinylist = [123, 'john']
	print (list)         	# Prints complete list
	print (list[0])       	# Prints first element of the list
	print (list[1:3])    	# Prints elements starting from 2nd till 3rd 
	print (list[2:])     	# Prints elements starting from 3rd element
	print (tinylist * 2)  	# Prints list two times
	print (list + tinylist) # Prints concatenated lists
	
ketika kode dijalankan akan menghasilkan :
	"""
	)

	#!/usr/bin/python3
	list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
	tinylist = [123, 'john']
	print (list)         	# Prints complete list
	print (list[0])       	# Prints first element of the list
	print (list[1:3])    	# Prints elements starting from 2nd till 3rd 
	print (list[2:])     	# Prints elements starting from 3rd element
	print (tinylist * 2)  	# Prints list two times
	print (list + tinylist) # Prints concatenated lists

pythonList()

def sparator(arg):
	print("\n", arg.center(59, "#"), "\n")

# Python Tuple
def pythonTuple():
	sparator(" // Python Tuple // ")
	print(
	"""
Tuple adalah tipe data urutan tang lain yang sama seperti list. tuple 
bisa di isi dengan beberapa nilai tipe data yang dipisahkan oleh koma 
yang diapit oleh tanda kurung ( () ) yan berbeda dengan list yang diapit 
dengan tanda kurung siku/kotak ( [] ).

yang paling membedakan dari list dan tuple adalah isi dari sebuah list 
bisa dimodifikasi/diubah, sedangkan pada tuple isinya tidak bisa diubah 
sama sekali (read-only).

Contoh :
	
	#!/usr/bin/python3 
	tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  ) 
	tinytuple = (123, 'john') 
	print (tuple)           # Prints complete tuple 
	print (tuple[0])        # Prints first element of the tuple 
	print (tuple[1:3])      # Prints elements starting from 2nd till 3rd  
	print (tuple[2:])       # Prints elements starting from 3rd element 
	print (tinytuple * 2)   # Prints tuple two times 
	print (tuple + tinytuple) # Prints concatenated tuple 
	
ketika kode diatas dieksekusi akan menghasilkan :
	"""
	)
	
	#!/usr/bin/python3 
	tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  ) 
	tinytuple = (123, 'john') 
	print (tuple)           # Prints complete tuple 
	print (tuple[0])        # Prints first element of the tuple 
	print (tuple[1:3])      # Prints elements starting from 2nd till 3rd  
	print (tuple[2:])       # Prints elements starting from 3rd element 
	print (tinytuple * 2)   # Prints tuple two times 
	print (tuple + tinytuple) # Prints concatenated tuple 
	
	print(
	"""
	kode dibawah adalah kode tidak valid dalam tuple, karena kita 
	mencoba untuk merubah nilai tuple. sama kasusnya seperti pada list 
	
	#!/usr/bin/python3 
	tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  ) 
	list = [ 'abcd', 786 , 2.23, 'john', 70.2  ] 
	tuple[2] = 1000    # Invalid syntax with tuple 
	list[2] = 1000     # Valid syntax with list 
	
ketika kode diatas akan menghasilkan : error
	"""
	)
	
	try:
		#!/usr/bin/python3 
		tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  ) 
		list = [ 'abcd', 786 , 2.23, 'john', 70.2  ] 
		tuple[2] = 1000    # Invalid syntax with tuple 
		list[2] = 1000     # Valid syntax with list 
	except TypeError:
		print("TypeError: 'tuple' object does not support item assingment")
		
pythonTuple()
