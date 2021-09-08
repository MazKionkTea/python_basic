def functionname(parameters):
    "function_docstring"
    # function_suite
    return # [expression]

def printme(str):
    "This prints a passed string into this function"
    print(str)
    return

#!/usr/bin/python3
# Function definition is here
def printme(str):
    "This prints a passed string into this function"
    print(str)
    return
# Now you can call printme function
printme("This is first call to the user defined function!")
printme("Again second call to the same function")

#!/usr/bin/python3
# Function definition is here
def changeme(mylist):
    "This changes a passed list into this function"
    print("Values inside the function before change: ", mylist)
    mylist[2]=50
    print("Values inside the function after change: ", mylist)
    return
# Now you can call changeme function
mylist = [10,20,30]
changeme([10,20,30])
print("Values outside the function: ", mylist)

#!/usr/bin/python3
# Function definition is here
def changeme(mylist):
    "This changes a passed list into this function"
    mylist = [1,2,3,4]
    # This would assi new reference in mylist print ("Values inside the function: ", mylist)
    return
# Now you can call changeme function
mylist = [10,20,30]
changeme(mylist)
print("Values outside the function: ", mylist)

#!/usr/bin/python3
# Function definition is here
def printme(str):
    "This prints a passed string into this function"
    print(str)
    return
# Now you can call printme function
printme("kontol")

#!/usr/bin/python3
# Function definition is here
def printme(str):
    "This prints a passed string into this function"
    print(str)
    return
# Now you can call printme function
printme(str = "My string")

#!/usr/bin/python3
# Function definition is here
def printinfo(name, age):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)
    return
# Now you can call printinfo function
printinfo(age=50, name="miki")

#!/usr/bin/python3
# Function definition is here
def printinfo(name, age = 35):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)
    return
# Now you can call printinfo function
printinfo(age=50, name="miki")
printinfo(name="miki")


"""
def functionname([formal_args,] *var_args_tuple ):
    "function_docstring"
    function_suite
    return [expression]
"""

#!/usr/bin/python3
# Function definition is here
def printinfo(arg1, *vartuple):
    "This prints a variable passed arguments"
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return
# Now you can call printinfo function
printinfo(10)
printinfo(70, 60, 50)

""" lambda [arg1 [,arg2,	argn]]:expression """

#!/usr/bin/python3
# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2
# Now you can call sum as a function
print("Value of total : ", sum(10, 20))
print("Value of total : ", sum(20, 20))

#!/usr/bin/python3
# Function definition is here
def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    print("Inside the function : ", total)
    return total
# Now you can call sum function
total = sum(10, 20)
print("Outside the function : ", total)

#!/usr/bin/python3
total = 0           # This is global variable.
# Function definition is here
def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2;    # Here total is local variable.
    print("Inside the function local total : ", total)
    return total
# Now you can call sum function
sum(10, 20)
print("Outside the function global total : ", total)


print(
"""
				// Fungsi //


Fungsi adalah sebuah blok kode yang teratur, dan bisa dipakai secara berulang kali.

menggunakan Fungsi dalam python menjadikan aplikasi kita lebih teratur. python menyediakan kita built-in fungsi seperti perintah print() dan lain-lain adalah yang bisa dipanggil atau dieksekusi berulang kali.

tapi kita juga bisa membuat fungsi kita sendiri yang didefinisikan/ditetapkan oleh kita sendiri.
"""
			)

print(
"""
	// Mendefinisikan sebuah Fungsi //

kita bisa mendefinisikan sebuah fungsi berdasarkan jenis fungsi itu sendiri. ada beberapa aturan jika ingin membuat sebuah fungsi dalam python

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
	
	contoh sintaks
	
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
	
	def printme( str ):
		"tulisan ini dilewati dalam fungsi ini"
		print (str)
		return
	
	berdasarkan contoh di atas, fungsi ini mengabil
	string parameter sebagai input dan akan dicetak
	dilayar setelah fungsinya di panggil.
	
	
	// memanggil fungsi //

mendefinisikan fungsi melalui nama, secara spesifik parameter tersebut dimasukan kedalam fungsi dan stuktur blok kode. dan cara mengeksekusi/memanggil fungsi tersebut dengan cara mengetikan nama dari fungsi tersebut. dari contoh fungsi di atas, kita cukup mengetikan printme(). karena fungsi di atas memiliki parameter str, berarti kita harus memasukan parameter string didalam tanda kurung tersebut. dan cara pemanggilannya printme("wkwkwkwk")


	// Pass by Reference vs Value //

semua parameter (argumen) dalam bahasa python

  
All parameters (arguments) in the Python language are passed by reference. It means if you change what a parameter refers to within a function, the change also reflects back in the calling function. For example- 


"""
			)

def printme( str ):
		"tulisan ini dilewati dalam fungsi ini"
		print(str)
		return

printme(str(input()))


def changeme( mylist ):
	"This changes a passed list into this function"
	print ("Values inside the function before change: ", mylist)
	mylist[2]=50
	print("Values inside the function after change: ", mylist)
	return
	# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print("Values outside the function: ", mylist) 
