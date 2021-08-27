def sparator(arg = "#"):
    print("\n", "#".center(59, "#"))
    print(arg.center(59, "#"))
    print("#".center(59, "#"), "\n")
    
def overview():
	sparator(" // String //")
	print(
	"""
string adalah tipe data yang paling populer dalam bahasa 
python. kita dapat membuatnya dengan mudah dengan 
menempatkan karakter/kata/kalimat yang diapit oleh dua 
tanda petik. bisa menggunakan tanda petik satu (' ') ataupun 
tanda petik dua (" "). contoh :

semua yang diapit oleh dua tanda petik akan dianggap 
sebagai tipe data string.

python tidak bisa mendukung sebuah tipe karakter.
untuk mengakses substring, sengan cara mengguakan tanda 
kurung kotak ( [ ] ) untuk memisahkan antara index substring.

contoh :
	
	#!/usr/bin/python3
	variabelString1 = 'This is a variable with String data type value'
	variabelString2 = "This is a variable with String data type value to"
	
	print("variabel_string1[0] :", variabel_string1[0])
	print("variabel_string2[1:5] :", variabel_string2[1:5])

ketika kode diekdekusi akan menampilkan :
	"""
	)
	
	#!/usr/bin/python3
	variabel_string1 = 'This is a variable with String data type value'
	variabel_string2 = "This is a variable with String data type value to"
	
	print("variabel_string1[0] :", variabel_string1[0])
	print("variabel_string2[1:5] :", variabel_string2[1:5])



def updating_string():
    sparator(" // Updating String // ")
    print(
    """
kita bisa mengupdate string yang sudah ada dengan 
menugaskan kembali sebuah variabel ke sting yang lain. 
nilai yang baru akan terkait dengan nilai sebelumnya atau 
untuk mengubah string yang benar-benar berbeda untuk 
disatukan sebagai kesatuan.

contoh :
	
	variabel_string1 = 'This is a variable with String data type value'
	variabel_string2 = "This is a variable with String data type value to"

    print(variabelString1, ", and", variabelString2)

atau

	var1 = 'Hello World!'
	print ("Updated String :-", var1[:6] + 'Python')

ketika kode diekdekusi akan menampilkan :
    """
    )
    
    variabel_string1 = 'This is a variable with String data type value'
    variabel_string2 = "This is a variable with String data type value to"
    
    print(variabel_string1, ", and", variabel_string2)
    
    var1 = 'Hello World!'
    print ("Updated String :-", var1[:6] + 'Python')
    print("bukan lagi Hello World!")



def escape_character():
    sparator(" // Escape Character // ")
    print(
    """
mengikuti daftar dari escape character atau karakter yang 
tidak akan ditampilkan pada layar bisa diwakili dengan 
menggunakan tanda backslash notation (\). 

escape character akan ditafsirkan dengan menggunakan 
tanda petik satu atau tanda petik dua.

- Backslash notation
- Hexadecimal character
- Description

\a
0x07
Bell or alert

\b
0x08
Backspace

\cx
null
Control-x

\C-x
null
Control-x

\e
0x1b
Escape

\f
0x0c
Formfeed

\M-\C-x
null
Meta-Control-x

\n
0x0a
Newline

\nnn
null
Octal notation, where n is in the range 0.7

\r
0x0d
Carriage return

\s
0x20
Space

\t
0x09
Tab
    """
    )
    


def string_special_operator():
    sparator(" // String Special Operator // ")
    print(
    """
asumsikan variabel a hadalah 'Hello' 
and variabel b adalah 'Python'.


Operator : 
	+ (Concatenation/menggabungkan)
Deskripsi :
	Menambahkan nilai di kedua sisi operator
Contoh :
	a + b akan menghasilkan HelloPython



Operator :
	* (Repetition/pengulangan)
Description :
	menggabungkan beberapa salinan dari string yang sama
	(membuat string baru)
Example :
	a * 2 akan menghasilkan HelloHello


Operator :
	[] (Slice/iris)
Description :
	memberi karakter dari indeks yang diberikan
Example :
	a[1]  akan menghasilkan karakter e



Operator :
	* (Range Slice/mengiris urutan)
Description :
	 menghasilkan urutan karakter yang diiris 
Example :
	a[1:4] akan menghasilkan ell



Operator :
	* (Repetition/pengulangan)
Description :
	menggabungkan beberapa salinan dari string yang sama
	(membuat string baru)
Example :
	
	a * 2 akan menghasilkan HelloHello



Operator :
	* (Repetition/pengulangan)
Description :
	menggabungkan beberapa salinan dari string yang sama
	(membuat string baru)
Example :
	a * 2 akan menghasilkan HelloHello



Operator :
	* (Repetition/pengulangan)
Description :
	menggabungkan beberapa salinan dari string yang sama
	(membuat string baru)
Example :
	a * 2 akan menghasilkan HelloHello



Operator :
	* (Repetition/pengulangan)
Description :
	menggabungkan beberapa salinan dari string yang sama
	(membuat string baru)
Example :
	a * 2 akan menghasilkan HelloHello
    """
    )


# 5
# stringSpecialOperator()

def stringFormattingOperator():
    sparator("String Foramatting Operator")
    print(
    """
    salah satu fitur terbaik dari string format yaitu operator %.
    operator ini sangat unik untuk tipe data string dan membuat 
    fungsi print() menjadi sangat efektif.
    contohnya :

        #!/usr/bin/python3
        print("my name is %s and weight is %d kg!" % ("zara, 21"))

        ketika kode dieksekusi akan menampilkan :
        (my name is zara and weight is 21 kg!)

    dibawah ini adal h daftar simbol yang bisa digunakan oleh %.


    Format Symbol       Conversion

    %c                  character
    %s                  string conversion via str() prior to formatting
    %i                  signed decimal integer
    %d                  signed decimal integer
    %u                  unsigned decimal integer
    %o                  octal integer
    %x                  hexadecimal integer (lowercase letters)
    %X                  hexadecimal integer (UPPERcase letters)
    %e                  exponential notation (with lowercase 'e')
    %E                  exponential notation (with UPPERcase 'E')
    %f                  floating point real number
    %g                  the shorter of %f and %e
    %G                  the shorter of %f and %E

    Simbol dan fungsionalitas lain yang didukung muncul di tabel berikut.

    Symbol              Functionality

    *                   argument specifies width or precision
    -                   left justification
    +                   display the sign
    <sp>                leave a blank space before a positive number
    #                   add the octal leading zero ( '0' ) or hexadecimal leading '0x' or '0X', depending on whether 'x' or 'X' were used.
    0                   pad from left with zeros (instead of spaces)
    %                   '%%' leaves you with a single literal '%'
    (var)               mapping variable (dictionary arguments)
    m.n.                m is the minimum total width and n is the number of digits todisplay after the decimal point (if appl.)
    """
    )

# string concatination
def stringConcatination():
    myString = input("Please input some text \
        >>> ")

    print("User was input " + myString)
    print("User was input {}".format(myString))
    print(f"User was input {myString}")

# 6
# stringFormattingOperator()
# stringConcatination()

def tripleQuotes():
    sparator("Triple Quotes")
    print(
    """
    python triple quote mengijinkan string multi lines
    termasuk baris baru, tab dan karakter spesiala yang lain.

    sintaks untuk triple quotes bisa menggunakan tanda petik satu
    atau menggunakan tanda petik dua. contoh :
    """
    )

    print(
    '''
    #!/usr/bin/python3

    para_str = """
    this is a long string that is made up ofseveral lines and
    non-printable characters such asTAB ( \t ) and they will
    show up that way when displayed.NEWLINEs within 
    the string, whether explicitly given likethis within
    the brackets [ \n ], or just a NEWLINE withinthe 
    variable assignment will also show up.
    """
    '''
    )

    #!/usr/bin/python3

    para_str = """
    this is a long string that is made up ofseveral lines and
    non-printable characters such asTAB ( \t ) and they will
    show up that way when displayed.NEWLINEs within 
    the string, whether explicitly given likethis within
    the brackets [ \n ], or just a NEWLINE withinthe 
    variable assignment will also show up.
    """

    print(
        "ketika kode dieksekusi akan menamilkan :"
    )
    print(para_str)

    """
    this is a long string that is made up of
    several lines and non-printable characters such as
    AB (    ) and they will show up that way when displayed.
    NEWLINEs within the string, whether explicitly given like
    this within the brackets [
    ], or just a NEWLINE within
    the variable assignment will also show up.
    """
    
    print(
    """
    raw string tidak memperlakukan backslash sebagai spesial 
    karakter selamanya. setiapak karakter yang dimasukan kedalam 
    raw string tetap seperti apa yang telah ditulis.

    #!/usr/bin/python3
    print("c:\\nowhere")

    ketika kode diatas dieksekusi akan menghasilkan

    c:\nowhere

    sekarang coba kita gunakan sebagai raw string. dengan 
    menempatkan expresion dalam r'expresion'

    #!/usr/bin/python3
    print(r"c:\\nowhere")

    ketika kode dieksekusi akan menampilkan :

    c:\\nowhere

    dalam python, semua string akan diwakili unicode.
    """
    )

# 7
# tripleQuotes()

def unicodeString():
    sparator("Unicode String")
    print(
    """    
    dalam pythhon3 semua string diwakili/mewakili unicode,
    dalam python2 disimpan secara internal seperti 8 bit ASCII, 
    karenanya itu dibutuhkan untuk menempel "u" untuk membuat 
    unicode. hal tersebut sudah tidak diperlukan lagi.
    """
    )

# 8
# unicodeString()

def builtInMethod():
    sparator("Built-in String Method")
    print(
    """
    Bult-in String Method
    python memiliki Bit-in Method untuk memanipukasi string.

    String capitalize() Method.
        mengubah karakter pertama dari sebuah string menjadi 
        huruf kapital. tanpa perlu memasukan parameter/argument.

        sintaks :
            str.capitalize()

        contoh :
            str = "first character will be capital"
            print("str.capitalize() :", str.capitalize())
        
        maka hasil yang akan ditamilkan adalah :
        
            First character will be capital
    

    String center() Method
        sebuah string akan ditempatkan ditengah yang diapit 
        oleh sebuah karakter tanpa spasi.

        sintaks :
            center(width, fillchar) atau 
            center(width[, fillchar])

        parameter :
        - width (total semua karakter termasuk 
          karakter yang mengapit string tersebut)
        - fillchar (karakter yang akan dijadikan sebagai 
          pengapit string dan tidak lebih dari satu karakter atau spasi)
    
        contoh :

        contoh = " this string is enclosed by characters (Q) "
        print(contoh.center(70, 'Q'))

        maka hasil yang akan ditamilkan adalah :

            QQQQQQQ this string is enclosed by characters (Q) QQQQQQQQ
    
        total dar karakter dari contoh diatas adalah 70 karakter termasuk spasi.
        jika parameter width kurang dari total karakter, maka paremeter 
        fillchar tidak akan ditampilkan. jika fillchar dari contoh 
        diatas diisi dengan angka 10 maka yang akan ditampilkan 
        hanya stringnya saja karena jumlah dari karakter string 
        melebihi parameter fillchar. 

        String count() Method
            menghitung jumlah sebuah karakter atau kata dalam string 
            atau substring, jika kenggunakan metode pengindeksan, 
            diperlukan parameter indeks awal dan indeks akhir.
            
            sintaks :
                count(string) atau
                str.count(sub, start = 0, end = len(string))
                paraneter :
                - sub (subsstring yang akan dihitung dalam sebuah string)
                - start (indeks awal yang akan dihitung jika tidak dimulai dari indeks 0)
                - end (indeks akhir yang akan dihitung)
            
            contoh :

                txt = "counting an apples, how many apple words in this string?"
                print(txt.count("apple"))

                blok kode diatas menghitung berapa banyak kata apple
                dalam sebuah variabel string txt tersebut.
                jika dijalankan akan menampilkan 

                    2
        
    """
    )




# capital()
# center()
# count()

capitalize()
# Mengubah karakter pertama menjadi huruf besar

casefold()
# Mengubah string menjadi huruf kecil

center()
# Mengembalikan string yang berpusat

count()
# Mengembalikan berapa kali nilai yang ditentukan terjadi pada string

encode()
# Mengembalikan versi string yang dikodekan

endswith()
# Mengembalikan boolean true jika string berakhir dengan nilai yang ditentukan

expandtabs()
# Mengatur ukuran tab string

find()
# Mencari string untuk nilai yang ditentukan dan mengembalikan posisi di mana ditemukan

format()
# Format nilai yang ditentukan dalam string

format_map()
# Format nilai yang ditentukan dalam string

index()
# Mencari string untuk nilai yang ditentukan dan mengembalikan posisi di mana ditemukan

istitle() 	        
# kembalikan nilai True jika the string follows the rules of a title

isidentifier()	    
# kembalikan nilai True jika the string is an identifier

isalnum()	        
# kembalikan nilai True jika Semua karakter dalam string adalah alphanumeric

isalpha()	        
# kembalikan nilai True jika Semua karakter dalam string adalah dalam alfabet

isascii()	        
# kembalikan nilai True jika Semua karakter dalam string adalah Karakter ASCII

isdecimal()	        
# kembalikan nilai True jika Semua karakter dalam string adalah desimal.

isdigit()	        
# kembalikan nilai True jika Semua karakter dalam string adalah digit

islower()	        
# kembalikan nilai True jika Semua karakter dalam string adalah huruf kecil.

isnumeric()	        
# kembalikan nilai True jika Semua karakter dalam string adalah numerik

isprintable()	    
# kembalikan nilai True jika Semua karakter dalam string adalah dapat dicetak

isspace()	        
# kembalikan nilai True jika Semua karakter dalam string adalah Whitespaces.

isupper()	        
# kembalikan nilai True jika Semua karakter dalam string adalah huruf besar

join()	            
# Bergabung dengan unsur-unsur dari ujung string

ljust()	            
# return a left justified version of the string

lower()	            
# Mengubah string menjadi huruf kecil

lstrip()	        
# kembalikan nilai versi trim kiri dari string

maketrans()	        
# kembalikan nilai tabel terjemahan yang akan digunakan dalam terjemahan

partition()	        
# kembalikan nilai tuple di mana string itu berpisah menjadi tiga bagian

replace()	        
# kembalikan nilai string di mana nilai yang ditentukan diganti dengan nilai yang ditentukan

rfind()	            
# Mencari string untuk nilai yang ditentukan dan kembalikan nilai posisi terakhir dari mana ditemukannya

rindex()	        
# Mencari string untuk nilai yang ditentukan dan kembalikan nilai posisi terakhir dari mana ditemukannya

rjust()	            
# kembalikan nilai a right justified version of the string

rpartition()	    
# kembalikan nilai tuple di mana string itu berpisah menjadi tiga bagian

rsplit()	        
# Membagi string pada pemisah yang ditentukan, dan kembalikan nilai list

rstrip()	        
# kembalikan nilai versi trim kanan dari string

split()	            
# Membagi string pada pemisah yang ditentukan, dan kembalikan nilai list

splitlines()	    
# Membagi string pada break line dan kembalikan nilai list

startswith()	    
# balikan nilai true jika String dimulai dengan nilai yang ditentukan

strip()	            
# kembalikan nilai versi string yang dipangkas

swapcase()	        
# Swaps kasus, huruf kecil menjadi huruf besar dan sebaliknya

title()	            
# Mengubah karakter pertama setiap kata ke huruf besar

translate()	        
# kembalikan nilai string yang diterjemahkan.

upper()	            
# Mengubah string menjadi huruf besar

zfill()	            
# Mengisi string dengan jumlah 0 nilai yang ditentukan di awal


"""
decode(encoding='UTF-8',errors='strict')
    Decodes the string using thecodec registered 
    for encoding. encoding defaults to 
    the default string encoding.
    
encode(encoding='UTF-8',errors='strict')
    Returns  encoded  string  version  of  string;  
    on  error,  default  is  to  raise  a ValueError 
    unless errors is given with 'ignore' or 'replace'.
    
endswith(suffix, beg=0, end=len(string))
    Determines if string or a substring of string 
    (if starting index beg and ending index end are given) 
    ends with suffix; returns true if so and false otherwise.

expandtabs(tabsize=8)
    Expands tabs in string to multiple spaces; 
    defaults to 8 spaces per tab if tabsize not provided.
    
find(str, beg=0 end=len(string))
    Determine if str occurs in string or in a substring 
    of string if starting index beg and ending index end 
    are given returns index if found and -1 otherwise.
    
index(str, beg=0, end=len(string))
    Same as find(), but raises an exception if str not found.
    
isalnum()
    Returns  true  if  string  has  at  least  1  character 
    and  all  characters  are alphanumeric and false otherwise.
    
isalpha()
    Returns true if string has at least 1 character 
    and all characters are alphabetic and false otherwise.
    
isdigit()
    Returns true if the string contains only digits 
    and false otherwise.
    
islower()
    Returns true if string has at least 1 cased character 
    and all cased characters are in lowercase and false otherwise.
    
isnumeric()
    Returns  true  if  a  unicode  string  contains  only  
    numeric  characters  and  false otherwise.

isspace()
    Returns true if string contains only whitespace characters 
    and false otherwise.
    
istitle()
    Returns true if string is properly "titlecased" 
    and false otherwise.
    
isupper()
    Returns true if string has at least one cased character 
    and all cased characters are in uppercase and false otherwise.
    
join(seq)
    Merges (concatenates) the string representations 
    of elements in sequence seq into a string, 
    with separator string.
    
len(string)
    Returns the length of the string
    
ljust(width[, fillchar])
    Returns a space-padded string with the original string 
    left-justified to a total of width columns.
    
lower()
    Converts all uppercase letters in string to lowercase.
    
lstrip()
    Removes all leading whitespace in string.
    
maketrans()
    Returns a translation table to be used in translate function.

max(str)
    Returns the max alphabetical cha racter from the string str.
    
min(str)
    Returns the min alphabetical character from the string str.
    
replace(old, new [, max])
    Replaces all occurrences of old in string with new 
    or at most max occurrences if max given.
    
rfind(str, beg=0,end=len(string))
    Same as find(), but search backwards in string.
    
rindex( str, beg=0, end=len(string))
    Same as index(), but search backwards in string.
    
rjust(width,[, fillchar])
    Returns a space-padded string with 
    the original string right-justified to a total 
    of width columns.
    
rstrip()
    Removes all trailing whitespace of string.
    
split(str="", num=string.count(str))
    Splits string according to delimiter str 
    (space if not provided) and returns list of 
    substrings; split into at most num substrings if given.
    
splitlines( num=string.count('\n'))
    Splits  string  at  all  (or  num)  NEWLINEs  
    and  returns  a  list  of  each  line  with NEWLINEs removed.

startswith(str, beg=0,end=len(string))
    Determines if string or a substring of string 
    (if starting index beg and ending index  end  are  given)  
    starts  with  substring  str;  
    returns  true  if  so  and  false otherwise.
    
strip([chars])
    Performs both lstrip() and rstrip() on string
    
swapcase()
    Inverts case for all letters in string.
    
title()
    Returns "titlecased" version of string, that is, 
    all words begin with uppercase and the rest are lowercase.
    
translate(table, deletechars="")
    Translates string according to translation 
    table str(256 chars), removing those in the del string.
    
upper()
    Converts lowercase letters in string to uppercase.
    
zfill (width)
    Returns  original  string  leftpadded  with  
    zeros  to  a  total  of  width  characters; 
    intended for numbers, zfill() retains any 
    sign given (less one zero).
    
isdecimal()
    Returns  true  if  a  unicode  string  contains  only
    decimal  characters  and  false otherwise.
    
String capitalize() MethodIt returns a copy of the string with only its first character capitalized.

format()
"""




































