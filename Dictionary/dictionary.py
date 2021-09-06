def sparator(arg = "#"):
	print("\n" * 2, "#".center(59, "#"))
	print(arg.center(59, "#"))
	print("#".center(59, "#"), "\n")



# Dictionary
def overview():
	sparator(" // Dictionary // ")
	print(
	"""
Dalam dictionary key dan value dipisahkan dengan tanda titik dua ( : ) 
jika pasangan key dan value pada dictionary lebih dari dua item dipisah 
dengan tanda koma dan semua item tersebut dibungkus oleh tanda 
kurung kurawal ( {} ). membuat dictionary kosong tanpa item apapun 
didalamnya dapat dibuat dengan menuliskan tanda kurung kurawal ( {} ) 

key pada dictionary harus unik tapi value nya bisa tipe data jenis apapun 
dan key nya harus tipe data yang immutable/tetap seperti string, number 
atau tuple.
	"""
	)
	


# Accessing Values in Dictionary
def accsessingDictionary():
	sparator(" // Accessing Values in Dictionary // ")
	print(
	"""
Untuk mengakses nilai pada dictionary element, yaitu dengan menulis 
tanda kurung siku dan didalamnya tulis key atau value yang diinginkan.

Contoh :

	#!/usr/bin/python3
	dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
	print ("dict['Name']: ", dict['Name'])
	print ("dict['Age']: ", dict['Age']) 
	
Ketika kode dijalankan akan menghasilkan :
	"""
	)
	
	#!/usr/bin/python3
	dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
	print ("dict['Name']: ", dict['Name'])
	print ("dict['Age']: ", dict['Age']) 

	print(
	"""
jika kita mencoba untuk mengakses data item dengan sebuah key yang 
bukan bagian dari dictionary, kita akan mendapatkan pesan error.	

Contoh:
	
	
	#!/usr/bin/python3  
	dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}; 
	
	print ("dict['Alice']: ", dict['Alice'] )
	
ketika kode dijalankan akan menghasilkan : error
	"""
	)
	
	try:
		#!/usr/bin/python3  
		dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}; 
	
		print ("dict['Alice']: ", dict['Alice'] )
	except KeyError:
		print(
		"""
	dict['Zara']: 
	Traceback (most recent call last):   
		File "test.py", line 4, in <module>     
			print "dict['Alice']: ", dict['Alice']; 
	KeyError: 'Alice' 
		"""
		)



# Updating Dictionary
def updatingDictionary():
	sparator(" // Updating Dictionary //")
	print(
	"""
kita bisa memperbaharui dictionary dengan menambahkan entry baru 
atau pasangan key-value untuk memodifikasi atau menghapus entry 
yang sudah ada seperti contoh dibawah.

Contoh:
	
	#!/usr/bin/python3  
	dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'} 
	dict['Age'] = 8;	# update existing entry 
	dict['School'] = "DPS School"	# Add new entry 
	print ("dict['Age']: ", dict['Age']) 
	print ("dict['School']: ", dict['School']) 
	
ketika kode dijalankan akan menghasilkan :
	"""
	)
	
	#!/usr/bin/python3  
	dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'} 
	dict['Age'] = 8;	# update existing entry 
	dict['School'] = "DPS School"	# Add new entry 
	print ("dict['Age']: ", dict['Age']) 
	print ("dict['School']: ", dict['School']) 



# Delete Dictionary Elements
def deletingElement():
	sparator(" // Delete Dictionary Elements // ")
	print(
	"""
kita bisa menghapus elemen dictionary yang terpisah atau menghapus 
seluruh isi dari dictionary bahkan menghapus seluruh dictionary dengan 
satu perintah. dengan menggunakan del statement.

Contoh :
	
	#!/usr/bin/python3  
	dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}  
	
	del dict['Name'] # remove entry with key 'Name' 
	dict.clear()     # remove all entries in dict 
	del dict			# delete entire dictionary  
	
	print ("dict['Age']: ", dict['Age']) 
	print ("dict['School']: ", dict['School']) 
	
ketika kode dijalankan akan menghasilkan : 
	"""
	)
	
	try:
		#!/usr/bin/python3  
		dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}  
	
		del dict['Name'] # remove entry with key 'Name' 
		dict.clear()     # remove all entries in dict 
		del dict			# delete entire dictionary  
	
		print ("dict['Age']: ", dict['Age']) 
		print ("dict['School']: ", dict['School']) 
	except UnboundLocalError:
		print(
		"""
pesan error akan muncul karean kita sudah menggunakan del statement 
untuk menghapus dictionary (del dict).

	UnboundLocalError atau TypeError
		"""
		)



# Properties of Dictionary Keys
def dictionaryKeyProperties():
	sparator(" // Properties of Dictionary Keys // ")
	print(
	"""
nilai dari dictionary tidak ada batasan dan mereka adalah objek python 
yang bisa berubah-ubah entah itu objek standar atau objek yang 
ditentukan oleh user. namun tidak untu key, ada dua poin penting yang harus di ingat tentang dictionary key.

- (a)
tidak boleh lebih dari satu entry per key. tetapi membuat key yang sama
diperbolehkan. saat key yang sama bertemu ketika di akses/ditugaskan 
key yang terakhir akan menimpa key yang sebelumnya 
(seperti assignment pada variabel).

Contoh :
	
	#!/usr/bin/python3  
	dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'} 
	print ("dict['Name']: ", dict['Name']) 
	
ketika kode dijalankan akan menghasilkan :

	"""
	)
	
	#!/usr/bin/python3  
	dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'} 
	print ("dict['Name']: ", dict['Name']) 

	print(
	"""
- (b) 
Key harus immutable/tidak berubah. Ini berarti kita bisa menggunakan
string, number atau tuples sebagai key dictinary tapi seperti ['Key'] tidak
diperbolehkan.

Contoh :
	
	#!/usr/bin/python3  
	dict = {['Name']: 'Zara', 'Age': 7}  
	print ("dict['Name']: ", dict['Name'])
	
ketika kode dijalankan akan menghasilkan : error
	"""
	)
	
	try :
		#!/usr/bin/python3  
		dict = {['Name']: 'Zara', 'Age': 7}  
		print ("dict['Name']: ", dict['Name'])
	except TypeError:
		print("TypeError: unhashable type 'list'")

	
#overview()
#accsessingDictionary()
#updatingDictionary()
#deletingElement()
dictionaryKeyProperties()
