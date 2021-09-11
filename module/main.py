def sparator(arg):
	print("\n" * 3)
	print("#".center(59, "#")
	print(arg.center(59, "#")
	print("#".center(59, "#")



def overview():
	sparator(" // Module // ")
	print('''
	Modul berguna untuk memecah kode python kedalam beberapa file
	dalam folder yang sama.
			
	cara memanggil/menggunakan import modul
			
		"import nama_modul"
			
	Contoh :
			
		misalkan dalam satu folder kita memiliki dua file python,
		file pertama main.py dan file yang kedua aritmatika.py
			
		dalam file main.py kita tuliskan import airtmatika
		"import aritmatika" artinya kita talah memanggil
		sebuah file python yang memiliki nama aritmatika.py
		sebagai sebuah modul.
			
		memanggil modul aritmatika mengimport file aritmatika.py
		yang masih satu folder dengan file main.py tanpa
		menambahkan ekstensi (.py). didalam file aritmatika
		memiliki beberapa fungsi matematika dasar seperti
		penjumlahan, pengurangan, perkalian, pembagian, dll.
	
	cara menggunakan/memanggil modul "nama_modul.sub_modul"
	sebagai contoh : aritmatika.tambah(10, 3)
	ini artinya kita memanggil kode yang ada didalam 
	file aritmatika bisa berupa fungsi, variabel, tipe data dll.
	dengan menggunakan "import aritmatika" secara tidak langsung
	kita telah memanggil seluruh isi kode yang ada didalam 
	file aritmatika.
	
	kita juga bisa mengubah nama modul yang akan kita import
	sebagai contoh kita akan mengubah nama aritmatika 
	menjadi matematika, kita hanya perlu menggunakan perintah
	"import aritmatika as matematika" dan cara memanggilnya
	kita cukup mengetikkan kode "matematika.tambah(10, 3)"

	"from aritmatika import tambah"
	perintah diatas adalah cara memanggil modul secara spesifik.
	contoh penggunaanya : tambah(10, 3)
	
	"from aritmatika import tambah as t"
	perintah diatas adalah cara memanggil modul secara spesifik 
	dan mengganti nama modulnya.
	contoh penggunaanya : t(10, 3)
	
	"from aritmatika import *"
	cara daiatas adaalh cara memanggil semua kode yang ada 
	didalam satu file yang sama
	''')



def package():
	sparator(" // Package // ")
	print('''
	Package adalah sebuah kumpulan modul-modul

	contoh :

		kita memiliki satu buah folder yang memiliki beberapa modul
		foldernya module dan memiliki tiga buah modul/file python
		yang berektensi .py yaitu aritmatika.py, penugasan.py,
		dan perbandingan.py

		dari keterangan diatas, kita bisa menggabungkan modul-modul
		tersebut menjadi sebuah package. caranya cukup mudah,
		kita hanya perlu menambah satu buah file baru yang diberi nama
		__init__.py

		jadi dalam folder tersebut kita memiliki empat buah file

			module
				aritmatika.py
				penugasan.py
				perbandingan.py
				__init__.py

		penggunaanya sama dengan cara kita mengimport dan memanggil
		modul. sebagai contoh kita akan mengakses modul aritmatika
		yang ada didalam folder module.
		pertama kita import terlebih dahulu modul-modulnya kadalam
		file __init__.py

	untuk mengakses/mengimport modulnya cukup dengan cara :
	
		"import folder_modul" atau
		"from folder_modul import nama_modul" atau
		"from folder_modul import sub_modul" atau
		"from .nama_modul import sub_modul"
		
	tanda titik (.) artinya folder utama dari kumpulan modul
	kita juga bisa mengganti nama modulnya seperti sebelumnya.
	ini terjadi karena ada file __init__.py didalam folder modul
	
	ini juga berguna jika kita memiliki lebih banyak modul
	dan berada didalam folder yang berbeda. 
	sebagai contoh stukturnya sebagai berikut :

		package_modu_l
			folder_modil_1
				nama_modul_1.py
				nama_modul_2.py
				nama_modul_3.py
				__init__.py
			folder_modul_2
				nama_modul_1.py
				nama_modul_2.py
				nama_modul_3.py
				__init__.py
			folder_modul_3
				nama_modul_1.py
				nama_modul2.py
				nama_modul3.py
				__init__.py
	
	import aritmatika (mengimport medul aritmatika)
	from aritmatika import tambah as t
	atau mengimport file aritmatika.py sebagai sebuah modul 
	dan secara otomatis python akan menambahkan sebuah folder baru 
	"__Pycache__" saat modul dijalankan
	from perbandingan import sd as samaDengan
	''')



def __main__():
	sparator(" // __main__ // ")
	print('''
	apa itu __main__ ?
	__main__ berguna utuk mengidentifikasi apakah kita menjalankan 
	program cecara langsung pada file python yang utama atau 
	apakah kita menjalankan program atau dari file python yang lain

	sebagai contoh, jika kita ingin mengecek apakah kita berada 
	didalam program utama atau bukan, cara pengcekanya sbb:

	contoh :

		setelah kita mengimport sebuah modul dan
		pada program saat ini kita tuliskan kode

		"print(__name__)"

	lalu dijalankan secara lngsung pada file ini,
	maka hasil yanga kan ditampikan adalah 

		__main__

	itu artinya kita berada difile utama. 
	tetapi jika pada saat program dijalankan dan
	hasil yang ditampilkan adalah nama filenya, 
	maka kita tidak sedang berada didalam file utama.
	cara lain untuk mengacek dengan kode yang lain

		def check_main():
			print("ini adalah fiie", __name__)

		if __name__ == "__main__":
			check_main()
	''')



########################################################################

# Module
overview()
package()
__main__()

########################################################################
