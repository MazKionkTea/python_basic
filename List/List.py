def sparator(arg = "#"):
    print("\n" * 3)
    print("#".center(59, "#"))
    print(arg.center(59, "#"))
    print("#".center(59, "#"))



def overview():
	sparator(" // List // ")
	print('''
    Struktur data yang paling mendasar di Python adalah urutannya/sequence. 
    Setiap elemen urutan diberi nomor/ posisinya atau indeksnya. 
    Indeks pertama adalah nol, indeks kedua adalah satu, dan seterusnya.

    Python memiliki enam jenis built-in method sequence/urutan, 
    dan yang paling umum adalah daftar/list dan tuple, 
    yang akan kita lihat dalam tutorial ini.

    Ada beberapa hal yang bisa Anda lakukan dengan semua jenis urutan. 
    Operasi ini meliputi pengindeksan (indexing), pengiris (slice), 
    penambahan (adding), perkalikan (multiplying), dan periksa 
    keanggotaan (membership). Selain itu, 
    Python memiliki fungsi built-in untuk menemukan panjang urutan 
    dan untuk menemukan elemen terbesar dan terkecil.
	''')



def pythonList():
	sparator(" // Python Lists // ")
	print('''
    List/Daftar ini adalah tipe data versatile/paling serbaguna 
    yang tersedia di Python, yang dapat ditulis sebagai daftar nilai 
    yang dipisahkan oleh tanda koma nilainya (item) dimasukan 
    dalam braket persegi. Hal yang penting tentang list adalah 
    item/value dalam list tidak perlu menggunakan jenis tipe data yang sama.

    Membuat daftar sama sederhana seperti memasukkan nilai yang 
    dipisahkan koma yang dimasukan kedalam  tanda kurung square. Misalnya-

        list1 = ['physics', 'chemistry', 1997, 2000];
        list2 = [1, 2, 3, 4, 5 ];
        list3 = ["a", "b", "c", "d"];

    Mirip dengan tipe data string, daftar indeks mulai dari 0, 
    dan daftar bisa diiris, digabungkan dan sebagainya.
	''')



def accsessing_list():
	sparator(" // Accessing Values in Lists // ")
	print('''
    Untuk mengakses nilai dalam list, gunakan tanda kurung square 
    untuk diiris beserta indeksnya atau indeks untuk mendapatkan 
    nilai yang tersedia pada indeks itu. Misalnya-

        #!/usr/bin/python3
        list1 = ['physics', 'chemistry', 1997, 2000]
        list2 = [1, 2, 3, 4, 5, 6, 7 ]

        print ("list1[0]: ", list1[0])
        print ("list2[1:5]: ", list2[1:5])

    Bila kode di atas dieksekusi, ia menghasilkan hasil berikut :
	''')

	#!/usr/bin/python3
    	list1 = ['physics', 'chemistry', 1997, 2000]
    	list2 = [1, 2, 3, 4, 5, 6, 7 ]

    	print ("list1[0]: ", list1[0])
    	print ("list2[1:5]: ", list2[1:5])



def updating_list():
    sparator(" // Updating Lists // ")
    print('''
    Kita dapat memperbarui elemen tunggal atau beberapa elemen list 
    dari dengan memberi irisan di sisi kiri operator penugasan, 
    dan Kita dapat menambahkan ke elemen dalam list dengan menggunakan 
    method Append(). Sebagai contoh :

        #!/usr/bin/python3
        list = ['physics', 'chemistry', 1997, 2000]
        print ("Value available at index 2 : ", list[2])
        list[2] = 2001
        print ("New value available at index 2 : ", list[2])

    Catatan: Metode Append () dibahas di bagian selanjutnya.
    Bila kode di atas dieksekusi, ia menghasilkan berikut :
	''')

	#!/usr/bin/python3
    list = ['physics', 'chemistry', 1997, 2000]
    print ("Value available at index 2 : ", list[2])
    list[2] = 2001
    print ("New value available at index 2 : ", list[2])



def deleting_list():
    sparator(" // Delete List Elements // ")
    print('''
    Untuk menghapus elemen list, Kita dapat menggunakan 
    statement/pernyataan DEL (del) jika Kita tahu persis 
    elemen mana yang akan dihapus. Kita dapat menggunakan 
    metode Remove() jika Kita tidak tahu persis 
    item mana yang akan dihapus. Misalnya :

        #!/usr/bin/python3
        list = ['physics', 'chemistry', 1997, 2000]
        print (list)
        del list[2]
        print ("After deleting value at index 2 : ", list)

    Bila kode di atas dieksekusi, ia menghasilkan berikut :
    CATATAN: remove() Metode dibahas di bagian selanjutnya.
	''')

	#!/usr/bin/python3
    list = ['physics', 'chemistry', 1997, 2000]
    print (list)
    del list[2]
    print ("After deleting value at index 2 : ", list)



def list_operation():
    sparator(" // Basic List Operations // ")
    print('''
    List merespons operator + dan * seperti string; 
    Mereka berarti perpecahan dan pengulangan di sini juga, 
    kecuali hasilnya adalah list baru, bukan string. 

    Sebenarnya, list menanggapi semua operasi urutan umum 
    yang kami gunakan pada senar di bab sebelumnya.

    Python Expression    	Results    			Description
    len([1, 2, 3])    		3    				Length
    [1, 2, 3] + [4, 5, 6]    	[1, 2, 3, 4, 5, 6]   	 	Concatenation
    ['Hi!'] * 4    		['Hi!', 'Hi!', 'Hi!', 'Hi!']    Repetition
    3 in [1, 2, 3]    		True   				Membership
    for x in [1,2,3]:
        print (x,end=' ')   	1 2 3    			Iteration
	''')
  


def built_in_method():
    sparator(" // Indexing, Slicing and Matrixes // ")
    print('''
    Karena list adalah urutan, pengindeksan dan irisan kerja sama 
    jalan untuk list seperti yang dilakukan pada string.

    Dengan asumsi input berikut :

    L=['C++'', 'Java', 'Python']

    Python Expression    Results    Description
    L[2]    'Python'    Offsets start at zero
    L[-2]    'Java'    Negative: count from the right
    L[1:]    ['Java', 'Python']    Slicing fetches sections


        // Built-in List Functions & Methods //

    [ 1 ] cmp(list1, list2)
    Tidak lagi tersedia di Python 3.

    [ 2 ] len(list) ]
    Memberikan panjang total dari sebuah daftar.

    [ 3 ] max(list)
    Mengembalikan item dengan nilai maksimal dari sebuah list.

    [ 4 ] min(list)
    Mengembalikan item dengan nilai minimal dari sebuah list.

    [ 5 ] list(seq)
    Mengkonversi tuple ke dalam list.



    [ 1 ] list.append(obj)
    Menambahkan objek kedalam list.

    [ 2 ] list.count(obj)
    Menghitung jumlah berapa kali obj terjadi dalam list.

    [ 3 ] list.extend(seq)
    Menambahkan seq/urutan kedalam list.

    [ 4 ] list.index(obj)
    Mengembalikan indeks terendah dalam daftar yang ditunjukkan oleh Obj

    [ 5 ] list.insert(index, obj)
    Menyisipkan Objek ke dalam list di Index pengganti.

    [ 6 ] list.pop(obj=list[-1])
    Menghilangkan dan mengembalikan objek terakhir dari list.

    [ 7 ] list.remove(obj)
    Menghilangkan objek dari list

    [ 8 ]list.reverse()
    Membalikan objek list dari tempatnya.

    [ 9 ] list.sort([func])
    Mengurutkan  objek dalam list, gunakan fungsi komparasi func  jika diberikan.
	''')



def sparator(arg = "#"):
    print("\n" * 3)
    print("#".center(59, "#"))
    print(arg.center(59, "#"))
    print("#".center(59, "#"))



list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]



# Basic list
def basic_list():
    sparator("// Basic List //")
    list1 = ['physics', 'chemistry', 1997, 2000]
    list2 = [1, 2, 3, 4, 5 ]
    list3 = ["a", "b", "c", "d"]
    
    print(f"{list1}, \n, {list2}, \n, {list3}")
    print(list1, list2, list3)



# Accessing Values in Lists
def accsessing_value():
    sparator("// Accessing Value //")
    #!/usr/bin/python3
    list1 = ['physics', 'chemistry', 1997, 2000]
    list2 = [1, 2, 3, 4, 5, 6, 7 ]
    
    print ("list1[0]: ", list1[0])
    print ("list2[1:5]: ", list2[1:5])



# Updating list
def updating_list():
    sparator("// Updating List //")
    #!/usr/bin/python3
    list = ['physics', 'chemistry', 1997, 2000]
    print ("Value available at index 2 : ", list[2])
    list[2] = 2001
    print ("New value available at index 2 : ", list[2])



# Delete List Elements
def deleting_list():
	sparator(" // Deleting List//")
	#!/usr/bin/python3
	list = ['physics', 'chemistry', 1997, 2000]
	print (list)
	del list[2]
	print ("After deleting value at index 2 : ", list)



# Basic list operator
def list_length():
	sparator(" // Length // ")
	list = [1, 2, 3]
	print(len(list))
	# printning length of a list



# List Concatination
def list_concatination():
	sparator(" // Concatination List // ")
	list1 = [1, 2 ,3]
	list2 = [4, 5, 6]
	concate = list1 + list2
	print(concate)
	# concatination list1 & list2-



# List Repetition
def list_repetition():
	sparator(" // Repetition // ")
	list = ["Hi !"]
	repetition = list * 4
	print(repetition)
	# repetition a list with multiply oprator



# List Membership
def list_membership():
	sparator(" // Membership // ")
	list = [1, 2, 3]
	if 3 in list:
		print(True)
	else:
		print(False)
	# check Membership of a list with decicion making



# List Iteration
def list_iteration():
	sparator(" // Iteration // ")
	list = [1, 2, 3]
	for x in list:
		print(x)
	# 1 2 3 Iteration a list with loop



# Indexing, Slicing and Matrixes
def indexing_slice():
	sparator( " // Indexing, Slice & Matrix // ")
	L = ["C++",  "Java", "Python"]
	offset = L [2]
	# Offsets start at zero
	negative = L[-2]
	# Negative: count from the right
	slice = L[1:]
	#Slicing fetches sections
	print(f"\n Offset = {offset} \n Negative = {negative} \n Slica = {slice}")






# Built-in List Functions & Methods 

# cmp(list1, list2)
# Tidak lagi tersedia di Python 3.

#	len(list)
# Memberikan panjang total dari sebuah daftar.
def list_len():
	sparator(" // Built-in len() Method // ")
	print('''
    Deskripsi :
    
        Metode len() mengembalikan jumlah elemen dalam daftar.

    Sintaks :
    
        len(list)

    Parameter :
    
        list (adalah daftar/jumlah elemen yang akan dihitung).

    Contoh :

        #!/usr/bin/python3
        list1 = ['physics', 'chemistry', 'maths']
        print (len(list1))
        list2=list(range(5))
        # creates list of numbers between 0-4 print
        (len(list2))
    
    ketika kode dieksekusi akan menghasilkan :
	''')
	
	#!/usr/bin/python3
	list1 = ['physics', 'chemistry', 'maths']
	print (len(list1))
	list2=list(range(5))
	# creates list of numbers between 0-4 
	print(len(list2))



# max(list)
# Mengembalikan item dengan nilai maksimal dari sebuah list.
def list_max():
	sparator(" // Built-in max() Method // ")
	print('''
    Deskripsi :

        Method max() mengembalikan nilai maksimum/tertinggi dari sebuah list 
        entah itu jumlah string, angka, dll.

    Sintaks :
        
        max(list)

    Parameter :
        
        list (adalah daftar/jumlah elemen yang akan dihitung)

    Contoh :
        
        #!/usr/bin/python3
        list1, list2 = ['C++','Java', 'Python'], [456, 700, 200]
        print ("Max value element : ", max(list1))
        print ("Max value element : ", max(list2))
        
    ketika program dijalankan akan menghasilkan :
	''')
	
	#!/usr/bin/python3
	list1, list2 = ['C++','Java', 'Python'], [456, 700, 200]
	print ("Max value element : ", max(list1))
	print ("Max value element : ", max(list2))



# min(list)
# Mengembalikan item dengan nilai minimum dari sebuah list.
def list_min():
	sparator(" // Built-in min() Method // ")
	print(
	"""
    Deskripsi :
    
        Method min() mengembalikan nilai minimum/terendah dari sebuah list 
        entah itu jumlah string, angka, dll.

    Sintaks :
        
        min(list)

    Parameter :
        
        list (adalah daftar/jumlah elemen yang akan dihitung)

    Contoh :
	
        #!/usr/bin/python3
        list1, list2 = ['C++','Java', 'Python'], [456, 700, 200]
        print ("Min value element : ", min(list1))
        print ("Min value element : ", min(list2))
	
    ketika program dijalankan akan menghasilkan :
	"""
	)
	
	#!/usr/bin/python3
	list1, list2 = ['C++','Java', 'Python'], [456, 700, 200]
	print ("Min value element : ", min(list1))
	print ("Min value element : ", min(list2))



# list(seq)
# Mengkonversi tuple ke dalam list.
def list_list():
	sparator(" // Built-in list() Method // ")
	print('''
    Deskripsi :
    
        Method list() mengambil jenis urutan dan mengubahnya menjadi list.
        Ini digunakan untuk mengubah tupel tertentu ke dalam list.

        Catatan: Tuple sangat mirip dengan list perbedaannya hanya
        nilai elemen dari tipe data tupel tidak dapat diubah dan
        elemen tuple diletakkan antara tanda kurung, bukan braket persegi.
        Fungsi ini juga mengubah karakter dalam string menjadi list.

    Sintaks :
        
        list(seq)

    Parameter :
        
        seq (adalah tuple atau string yang akan diubah menjadi list)
        Catatan : tipe datanya sebuah urutan (sequence)

    Contoh :
	
        #!/usr/bin/python3
        aTuple = (123, 'C++', 'Java', 'Python')
        list1 = list(aTuple)
        print ("List elements : ", list1)
        str="Hello World"
        list2=list(str)
        print ("List elements : ", list2) 
	
    ketika program dijalankan akan menghasilkan :

	''')
	
	#!/usr/bin/python3
	aTuple = (123, 'C++', 'Java', 'Python')
	list1 = list(aTuple)
	print ("List elements : ", list1)
	str="Hello World"
	list2=list(str)
	print ("List elements : ", list2) 



# list.append(obj)
# Menambahkan objek kedalam list.
def list_append():
	sparator(" // Built-in list.append() Method // ")
	print('''
    Deskripsi :

        Method Append() akan menambahkan obj sebelah kanan kedalam list yang ada.

    Sintaks :
        
        list.append(obj)

    Parameter :
        
        obj (objek yang akan ditambahkan dalam list).

    Contoh :
        
        #!/usr/bin/python3
        list1 = ['C++', 'Java', 'Python']
        list1.append('C#')
        print("updated list : ", list1) 
        
    ketika program dijalankan akan menghasilkan :
	''')
	
	#!/usr/bin/python3
	list1 = ['C++', 'Java', 'Python']
	list1.append('C#')
	print("updated list : ", list1) 



# list.count(obj)
# Menghitung jumlah berapa kali obj terjadi dalam list.
def list_count():
	sparator(" // Built-in list.count() Method // ")
	print('''
    Deskripsi :
    
        Method count() mengembalikan jumlah berapa banyak obj yang sama dalam list.
        obj bisa berupa string, number, karakter string, dll.

    Sintaks :
    
        list.count(obj)
        
    Parameter :
        
        obj (objek yang akan ditambahkan dalam list).
        
    Contoh :
        
        #!/usr/bin/python3
        aList = [123, 'xyz', 'zara', 'abc', 123]
        print ("Count for 123 : ", aList.count(123))
        print ("Count for zara : ", aList.count('zara')) 
        
    ketika program dijalankan akan menghasilkan :
	''')
	
	#!/usr/bin/python3
	aList = [123, 'xyz', 'zara', 'abc', 123]
	print ("Count for 123 : ", aList.count(123))
	print ("Count for zara : ", aList.count('zara')) 



# list.extend(seq)
# Menambahkan seq/urutan kedalam list.
def list_extend():
	sparator(" // Built-in list.extend() Method // ")
	print('''
    Deskripsi :
        
        Method extend() Menambahkan isi seq/urutan untuk list.

    Sintaks :
        
        list.extend(seq)

    Parameter :
        
        seq (urutan yang akan ditambahkan kedalam list)

    Contoh :
        
        #!/usr/bin/python3
        list1 = ['physics', 'chemistry', 'maths']
        list2=list(range(5))
        #creates list of numbers between 0-4
        list1.extend('Extended List :', list2)
        print (list1) 
        
    ketika program dijalankan akan menghasilkan :
	''')
	
	#/usr/bin/python3
	list1 = ['physics', 'chemistry', 'maths']
	list2 = list(range(5))
	#creates list of numbers between 0-4
	list1.extend(list2)
	print ('Extended List :', list1) 



# list.index(obj)
# Mengembalikan indeks terendah dalam daftar yang ditunjukkan oleh Obj
def list_index():
	sparator(" // Built-in list.index() Method // ")
	print('''
    Deskripsi :
    
        Method index() Mengembalikan indeks terendah dalam daftar
        yang ditunjukkan oleh Obj

    Sintaks :
        
        list.index(obj)

    Parameter :
        
        obj (objek yang bisa ditemukan.)

    Contoh :
        
        #!/usr/bin/python3
        list1 = ['physics', 'chemistry', 'maths']
        print ('Index of chemistry', list1.index('chemistry'))
        print ('Index of C#', list1.index('C#')) 
        
    ketika program dijalankan akan menghasilkan :
	''')
	
	#!/usr/bin/python3
	list1 = ['physics', 'chemistry', 'maths', 'C#']
	print ('Index of chemistry', list1.index('chemistry'))
	print ('Index of C#', list1.index('C#'))



# list.insert(index, obj)
# Menyisipkan Objek ke dalam list di Index pengganti.
def list_insert():
	sparator(" // Built-in list.insert() Method // ")
	print('''
    Deskripsi :
    
        Method insert() Mengembalikan indeks terendah dalam daftar
        yang ditunjukkan oleh Obj

    Sintaks :
        
        list.insert(index, obj)

    Parameter :
        
        Index (ini adalah indeks dimana objek Obj perlu dimasukkan).
        obj (objek yang dimasukkan ke dalam list untuk diisi.)

    Contoh :
        
        #!/usr/bin/python3
        list1 = ['physics', 'chemistry', 'maths']
        list1.insert(1, 'Biology')
        print ('Final list : ', list1) 
        
    ketika program dijalankan akan menghasilkan :
	''')
	
	#!/usr/bin/python3
	list1 = ['physics', 'chemistry', 'maths']
	list1.insert(1, 'Biology')
	print ('Final list : ', list1) 



# list.pop(obj=list[-1])
# Menghilangkan dan mengembalikan nilai objek terakhir dari list.
def list_pop():
    sparator(" // Built-in list.pop() Method // ")
    print('''
    Deskripsi :
    
        Menghilangkan dan mengembalikan nilai objek terakhir dari list.

    Sintaks :
        
        list.pop(obj=list[-1])
        list.pop(indeks obj)

    Parameter :
        
        obj (Ini adalah parameter opsional,
        indeks objek yang akan dihapus dari list.)

    Contoh :

        #!/usr/bin/python3
        list1 = ['physics', 'Biology', 'chemistry', 'maths']
        list1.pop()
        print ("list now : ", list1)
        list1.pop(1)
        print ("list now : ", list1)

    ketika program dijalankan akan menghasilkan :
	''')

	#!/usr/bin/python3
    list1 = ['physics', 'Biology', 'chemistry', 'maths']
    list1.pop()
    print ("list now : ", list1)
    list1.pop(1)
    print ("list now : ", list1)



# list.remove(obj)
# Menghilangkan objek dari list
def list_remove():
    sparator(" // Built-in list.remove() Method // ")
    print('''
    Deskripsi :
    
        Menghilangkan objek dari list

    Sintaks :
    
        list.remove(obj)

    Parameter :
    
        obj (objek yang akan dihilangkan dari list)

    Contoh :

        #!/usr/bin/python3
        list1 = ['physics', 'Biology', 'chemistry', 'maths']
        list1.remove('Biology')
        print ("list now : ", list1)
        list1.remove('maths')
        print ("list now : ", list1)

    ketika program dijalankan akan menghasilkan :
    ''')

	#!/usr/bin/python3
    list1 = ['physics', 'Biology', 'chemistry', 'maths']
    list1.remove('Biology')
    print ("list now : ", list1)
    list1.remove('maths')
    print ("list now : ", list1)



# list.reverse()
# Membalikan objek list dari tempatnya.
def list_reverse():
    sparator("// Built-in list.reverse() Method // ")
    print('''
    Deskripsi :
    
        Membalikan objek list dari indeks tempatnya.

    Sintaks :
        
        list.reverse()

    Parameter :
    
        -

    Contoh :

        #!/usr/bin/python3
        list1 = ['physics', 'Biology', 'chemistry', 'maths']
        list1.reverse()
        print ("list now : ", list1)

    ketika program dijalankan akan menghasilkan :
	''')

	#!/usr/bin/python3
    list1 = ['physics', 'Biology', 'chemistry', 'maths']
    list1.reverse()
    print ("list now : ", list1)



# list.sort([func])
# Mengurutkan  objek dalam list, gunakan fungsi komparasi func jika diperlukan.
def list_sort():
	sparator(" // Built-in list.sort() Method // ")
	print('''
    Deskripsi :
    
        Mengurutkan  objek dalam list

    Sintaks :
    
        list.sort([func])

    Parameter :

        -

    Contoh :

        #!/usr/bin/python3
        list1 = ['physics', 'Biology', 'chemistry', 'maths']
        list1.sort()
        print ("list now : ", list1)

    ketika program dijalankan akan menghasilkan :
	''')

	#!/usr/bin/python3
	list1 = ['physics', 'Biology', 'chemistry', 'maths']
	list1.sort()
	print ("list now : ", list1)


########################################################################

# Python List
overview()
pythonList()
accsessing_list()
updating_list()
deleting_list()
list_operation()
built_in_method()

# Basic Syntax
basic_list()
accsessing_value()
updating_list()
deleting_list()
list_length()
list_concatination()
list_repetition()
list_membership()
list_iteration()
indexing_slice()

# Built-in Method
list_len()      # [1]
list_max()      # [2]
list_min()      # [3]
list_list()     # [4]
list_append()   # [5]
list_count()    # [6]
list_extend()   # [7]
list_index()    # [8]
list_insert()   # [9]
list_pop()      # [10]
list_remove()   # [11]
list_reverse()  # [12]
list_sort()     # [13]

########################################################################
