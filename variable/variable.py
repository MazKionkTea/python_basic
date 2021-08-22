def sparator(arg):
	print("\n", arg.center(59, "#"), "\n")

def overview():
    	sparator(" // Variable // ")
	print("""
	variable berfungsi untuk memesan runag pada memori
	yang bisa diisi dengan suatu nilai dan bisa dipakai
	secara berulang berulang.

	yang berarti saat kita membuat sebuah variabel,
	kita sudah memesan sebagian kecil rung memori
	untuk dipakai dan diisi dengan sebuah nilai
	untuk kita pakai kembali
	""")

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

		int				float				complex
		
		10				0.0					3.14j
		100				15.20				45.j
		-786			-21.9				9.322e-36j
		080				32.3+e18			.876j
		-0480			-90.				-.6545+0j
		-0x260			-32.54e100			3e+26j
		0x69			70.2-E12			3.56e-7j
	"""
	)
