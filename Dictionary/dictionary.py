# Python Dictionary
def sparator(arg = "#"):
    print("\n" * 3)
    print("#".center(59, "#"))
    print(arg.center(59, "#"))
    print("#".center(59, "#"))



# Dictionary
def overview():
    sparator(" // Dictionary // ")
    print('''
    Dalam dictionary key dan value dipisahkan dengan tanda titik dua ( : ) 
    jika pasangan key dan value pada dictionary lebih dari dua item dipisah 
    dengan tanda koma dan semua item tersebut dibungkus oleh tanda 
    kurung kurawal ( {} ). membuat dictionary kosong tanpa item apapun 
    didalamnya dapat dibuat dengan menuliskan tanda kurung kurawal ( {} ) 

    key pada dictionary harus unik tapi value nya bisa tipe data jenis apapun 
    dan key nya harus tipe data yang immutable/tetap seperti string, number 
    atau tuple.
	''')



# Accessing Values in Dictionary
def accsessing_dictionary():
    sparator(" // Accessing Values in Dictionary // ")
    print('''
    Untuk mengakses nilai pada dictionary element, yaitu dengan menulis 
    tanda kurung siku dan didalamnya tulis key atau value yang diinginkan.

    Contoh :

        #!/usr/bin/python3
        dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
        print("dict['Name']: ", dict['Name'])
        print("dict['Age']: ", dict['Age']) 
        
    Ketika kode dijalankan akan menghasilkan :
	''')
	
	#!/usr/bin/python3
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    print("dict['Name']: ", dict['Name'])
    print("dict['Age']: ", dict['Age'])
    
    print('''
    jika kita mencoba untuk mengakses data item dengan sebuah key yang 
    bukan bagian dari dictionary, kita akan mendapatkan pesan error.	

    Contoh:
        
        #!/usr/bin/python3  
        dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}; 
        
        print("dict['Alice']: ", dict['Alice'] )
        
    ketika kode dijalankan akan menghasilkan : error
	''')
    
    try:
		#!/usr/bin/python3
        dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
        print("dict['Alice']: ", dict['Alice'])
    except KeyError:
        print('''
	dict['Zara']: 
	Traceback (most recent call last):   
		File "test.py", line 4, in <module>     
			print "dict['Alice']: ", dict['Alice']; 
	KeyError: 'Alice' 
		''')



# Updating Dictionary
def updating_dictionary():
	sparator(" // Updating Dictionary //")
	print('''
    kita bisa memperbaharui dictionary dengan menambahkan entry baru 
    atau pasangan key-value untuk memodifikasi atau menghapus entry 
    yang sudah ada seperti contoh dibawah.

    Contoh:
        
        #!/usr/bin/python3  
        dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'} 
        dict['Age'] = 8;	# update existing entry 
        dict['School'] = "DPS School"	# Add new entry 
        print("dict['Age']: ", dict['Age']) 
        print("dict['School']: ", dict['School']) 
        
    ketika kode dijalankan akan menghasilkan :
	''')
	
	#!/usr/bin/python3  
	dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'} 
	dict['Age'] = 8;	# update existing entry 
	dict['School'] = "DPS School"	# Add new entry 
	print("dict['Age']: ", dict['Age']) 
	print("dict['School']: ", dict['School']) 



# Delete Dictionary Elements
def deleting_element():
	sparator(" // Delete Dictionary Elements // ")
	print('''
    kita bisa menghapus elemen dictionary yang terpisah atau menghapus 
    seluruh isi dari dictionary bahkan menghapus seluruh dictionary dengan 
    satu perintah. dengan menggunakan del statement.

    Contoh :
        
        #!/usr/bin/python3  
        dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}  
        
        del dict['Name'] # remove entry with key 'Name' 
        dict.clear()     # remove all entries in dict 
        del dict			# delete entire dictionary  
        
        print("dict['Age']: ", dict['Age']) 
        print("dict['School']: ", dict['School']) 
        
    ketika kode dijalankan akan menghasilkan : 
	''')
	
	try:
		#!/usr/bin/python3  
		dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}  
	
		del dict['Name'] # remove entry with key 'Name' 
		dict.clear()     # remove all entries in dict 
		del dict			# delete entire dictionary  
	
		print("dict['Age']: ", dict['Age']) 
		print("dict['School']: ", dict['School']) 
	except UnboundLocalError:
		print('''
    pesan error akan muncul karean kita sudah menggunakan del statement 
    untuk menghapus dictionary (del dict).

        UnboundLocalError atau TypeError
		''')



# Properties of Dictionary Keys
def dictionary_key_properties():
	sparator(" // Properties of Dictionary Keys // ")
	print('''
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
        print("dict['Name']: ", dict['Name']) 
        
    ketika kode dijalankan akan menghasilkan :
	''')
	
	#!/usr/bin/python3  
	dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'} 
	print("dict['Name']: ", dict['Name']) 

	print('''
    - (b) 
    Key harus immutable/tidak berubah. Ini berarti kita bisa menggunakan
    string, number atau tuples sebagai key dictinary tapi seperti ['Key'] tidak
    diperbolehkan.

    Contoh :
        
        #!/usr/bin/python3  
        dict = {['Name']: 'Zara', 'Age': 7}  
        print("dict['Name']: ", dict['Name'])
        
    ketika kode dijalankan akan menghasilkan : error
	''')
	
	try :
		#!/usr/bin/python3  
		dict = {['Name']: 'Zara', 'Age': 7}  
		print("dict['Name']: ", dict['Name'])
	except TypeError:
		print("TypeError: unhashable type 'list'")



# Built-in Dictionary Functions & Methods
def dict_len():
    sparator(" // Dictionary len() Method // ")
    print('''
    Deskripsi :

        Memberikan panjang total dictionary. Ini akan sama dengan jumlah item dalam dictionary.

    Sintaks :

        len(dict)

    Parameter :

        dict (dictionary, yang panjangnya perlu dihitung.)

    Contoh :

        #!/usr/bin/python3
        dict = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
        print("Length : %d" % len (dict))

    ketika kode dijalankan akan menghasilkan :
    ''')

    #!/usr/bin/python3
    dict = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
    print("Length : %d" % len (dict))



def dict_str():
    sparator(" // Dictionary str() Method // ")
    print('''
    Deskripsi :

        menghasilkan representasi/gambaran string yang dapat dicetak dari dictionary.

    Sintaks :

        str(dict)

    Parameter :

        dict (dictionari yang akan dicetak sebagai string)

    Contoh :

        #!/usr/bin/python3
        dict = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
        print("Equivalent String : %s" % str (dict))

    ketika kode dijalankan akan menghasilkan :
    ''')

    #!/usr/bin/python3
    dict = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
    print("Equivalent String : %s" % str (dict))



def dict_type():
    sparator(" // Dictionary type() Method // ")
    print('''
    Deskripsi :

        Mengembalikan nilai lewat variabel. jika melewati variabel maka
        akan mengmbalikan nilai sebagai sebuah tipe dictionary
    
    Sintaks :

        type(dict)

    Parameter :

        dict (tipe data dictionary)

    Contoh :

        #!/usr/bin/python3
        dict = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
        print("Variable Type : %s" %  type (dict))

    ketika kode dijalankan akan menghasilkan :
    ''')

    #!/usr/bin/python3
    dict = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
    print("Variable Type : %s" %  type (dict))



def dict_clear():
    sparator(" // Dictionary dict.clear() Method // ")
    print('''
    Deskripsi :

        menghapus semua item/elemen dari dictionary
    
    Sintaks :

        dictionary.clear()

    Parameter :

        -

    Contoh :

        #!/usr/bin/python3
        dict = {'Name': 'Zara', 'Age': 7}
        print("Start Len : %d" % len(dict))
        dict.clear()
        print("End Len : %d" % len(dict))        
        
        car = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }

        car.clear()
        print(car)

    ketika kode dijalankan akan menghasilkan :
    ''')

    #!/usr/bin/python3
    dict = {'Name': 'Zara', 'Age': 7}
    print("Start Len : %d" % len(dict))
    dict.clear()
    print("End Len : %d" % len(dict))        
    
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    car.clear()
    print(car)



def dict_copy():
    sparator(" // Dictionary dict.copy() Method // ")
    print('''
    Deskripsi :

        mengembalikan nilai salinan dictionary yang ditentukan.

    Sintaks :

        dictionary.copy()

    Parameter :

        -

    Contoh :

        #!/usr/bin/python3
        dict1 = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
        dict2 = dict1.copy()
        print ("New Dictionary : ",dict2)

        car = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }

        x = car.copy()
        print(x)

    ketika kode dijalankan akan menghasilkan :
    ''')

    #!/usr/bin/python3
    dict1 = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
    dict2 = dict1.copy()
    print ("New Dictionary : ",dict2)

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    x = car.copy()
    print(x)



def dict_fromkeys():
    sparator(" // Dictionary dict.fromkeys() Method // ")
    print('''
    Deskripsi :

        
        mengembalikan nilai dictionary dengan key dan value yang ditentukan.
    
    Sintaks :

        dict.fromkeys(seq[, value]))
        atau
        dict.fromkey(key, value)

    Parameter :

        seq (Ini adalah daftar nilai yang akan digunakan untuk persiapan dictionary key)
        key (dibutuhkan. Iterable/bisa diubah untuk menentukan dictionary key yang baru)
        value (Opsional. Nilai untuk semua key. Nilai default adalah none)

    Contoh :

        #!/usr/bin/python3
        seq = ('name', 'age', 'sex')
        dict = dict.fromkeys(seq)
        print("New Dictionary : %s" %  str(dict))
        dict = dict.fromkeys(seq, 10)
        print("New Dictionary : %s" %  str(dict))
        
        # membuat dictionary dengan 3 keys yang memiliki nilai 0
        x = ('key1', 'key2', 'key3')
        y = 0
        thisdict = dict.fromkeys(x, y)
        print(thisdict)

        # sama seperti contoh diatas, tetapi tanpa menentukan nilainya.
        x = ('key1', 'key2', 'key3')
        thisdict = dict.fromkeys(x)
        print(thisdict)

    ketika kode dijalankan akan menghasilkan :
    ''')

    #!/usr/bin/python3
    one = ('name', 'age', 'sex')
    two = dict.fromkeys(one)
    print("New Dictionary : %s" %  str(two))
    three = dict.fromkeys(two, 10)
    print("New Dictionary : %s" %  str(three))
    
    # membuat dictionary dengan 3 keys yang memiliki nilai 0
    x = ('key1', 'key2', 'key3')
    y = 0
    thisdict = dict.fromkeys(x, y)
    print(thisdict)

    # sama seperti contoh diatas, tetapi tanpa menentukan nilainya.
    x = ('key1', 'key2', 'key3')
    thisdict = dict.fromkeys(x)
    print(thisdict)



def dict_get():
    sparator(" // Dictionary dict.get() Method // ")
    print('''
    Deskripsi :

        
        mengembalikan nilai dari item dengan key yang spesifik
    
    Sintaks :

        dictionary.get(keyname, value)

    Parameter :

        keyname (dibutuhkan, keyname dari item yang nilainya akan kita ambil)
        value (optional, mengemalikan nilainya.
        jika nilai spesifik key tidak ada, nilai defaultnya adalah none)
        
    Contoh :

        #!/usr/bin/python3
        dict = {'Name': 'Zara', 'Age': 27}
        print("Value : %s" %  dict.get('Age'))
        print("Value : %s" %  dict.get('Sex', "NA"))

        # mendapatkan niai dari meodel item
        car = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }

        x = car.get("model")
        print(x)

        # mencoba mengembalikan nilai yang itemnya tidak ada
        car = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }
        
        x = car.get("price", 15000)
        print(x)

    ketika kode dijalankan akan menghasilkan :
    ''')

    #!/usr/bin/python3
    dict = {'Name': 'Zara', 'Age': 27}
    print("Value : %s" %  dict.get('Age'))
    print("Value : %s" %  dict.get('Sex', "NA"))

    # mendapatkan niai dari meodel item
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    x = car.get("model")
    print(x)

    # mencoba mengembalikan nilai yang itemnya tidak ada
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    
    x = car.get("price", 15000)
    print(x)



def dict_items():
    sparator(" // Dictionary dict.items() Method // ")
    print('''
    Deskripsi :

        Objek tampilan berisi pasangan key-value dictionary, sebagai tupel dalam list.

    Sintaks :

        dictionary.items()

    Parameter :

        -

    Contoh :

        #!/usr/bin/python3
        dict = {'Name': 'Zara', 'Age': 7}
        print("Value : %s" %  dict.items())
        
        # mengenbalikan nilai dictionary dengan pasangan key dan value
        car = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }
        
        x = car.items()
        print(x)

        # ketika sebuah item dalam dictionary nilainya diganti,
        # objek yang dirubah akan diperbaharui.
        car = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }
        
        x = car.items()
        car["year"] = 2018
        print(x)

    ketika kode dijalankan akan menghasilkan :
    ''')

    #!/usr/bin/python3
    dict = {'Name': 'Zara', 'Age': 7}
    print("Value : %s" %  dict.items())
    
    # mengenbalikan nilai dictionary dengan pasangan key dan value
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    
    x = car.items()
    print(x)

    # ketika sebuah item dalam dictionary nilainya diganti,
    # objek yang dirubah akan diperbaharui.
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    
    x = car.items()
    car["year"] = 2018
    print(x)



def dict_keys():
    sparator(" // Dictionary dict.keys() Method // ")
    print('''
    Deskripsi :
    Sintaks :
    Parameter :
    Contoh :
    ketika kode dijalankan akan menghasilkan :
    ''')



def dict_pop():
    sparator(" // Dictionary dict.pop() Method // ")
    print('''
    Deskripsi :
    Sintaks :
    Parameter :
    Contoh :
    ketika kode dijalankan akan menghasilkan :
    ''')



def dict_popitem():
    sparator(" // Dictionary dict.popitem() Method // ")
    print('''
    Deskripsi :
    Sintaks :
    Parameter :
    Contoh :
    ketika kode dijalankan akan menghasilkan :
    ''')



def dict_setdefault():
    sparator(" // Dictionary dict.setdefault() Method // ")
    print('''
    Deskripsi :
    Sintaks :
    Parameter :
    Contoh :
    ketika kode dijalankan akan menghasilkan :
    ''')



def dict_updates():
    sparator(" // Dictionary dict.updates() Method // ")
    print('''
    Deskripsi :
    Sintaks :
    Parameter :
    Contoh :
    ketika kode dijalankan akan menghasilkan :
    ''')



def dict_values():
    sparator(" // Dictionary dict.values() Method // ")
    print('''
    Deskripsi :
    Sintaks :
    Parameter :
    Contoh :
    ketika kode dijalankan akan menghasilkan :
    ''')


########################################################################

# Python Dictionary
overview()
accsessing_dictionary()
updating_dictionary()
deleting_element()
dictionary_key_properties()

# Built-in Dictionary Functions & Methods
dict_len()
dict_str()
dict_type()
dict_clear()
dict_copy()
dict_fromkeys()
dict_get()
dict_items()
dict_keys()
dict_pop()
dict_popitem()
dict_setdefault()
dict_updates()
dict_values()

########################################################################
