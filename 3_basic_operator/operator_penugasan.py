#!/usr/bin/env python
# encoding: utf-8
"""
operator_penugasan.py

Created by MazKionkTea on 9/27/21.
Copyright (c) 2021 Copyright Holder. All rights reserved.
"""

########################################################################

''' basic operator
    - aritmatika
    - penugasan
    - bitwise
    - perbandingan
    - identitas
    - logika
    - keanggotaan
    - precedence '''

########################################################################

import os
from time import sleep

########################################################################

def sparator(arg):
    print("#".center(72, "#"))
    print(arg.center(72, "#"))
    print("#".center(72, "#"))

def mini_sparator(arg):
    print(arg.center(72, "#"))

def bottom_sparator():
    print("#".center(72, "#"), "\n")

def clear():
    os.system("clear")

def clear_exit():
    os.system("clear")
    exit()

def force_close_program():
    print("input error... program akan ditutup...!!!")
    sleep(5)
    os.system("clear")
    exit()

def option_back_exit():
    ''' Option '''
    print("\n")
    print('''
    [0] Back
    [X] Exit
    ''')
    # opt = input(">>> ")
    # return opt

def option_program():
    clear()
    sparator(" // Operator Penugasan // ")
    print('''
    [0] Overview        [3] Subtract AND          [6] Modulus AND
    [1] Equal           [4] Multiply AND          [7] Exponent AND
    [2] Add AND         [5] Divide AND            [8] Floor Division
    ''')
    mini_sparator(" // pilihan Program // ")
    # opt = input(">>> ")
    # return opt

########################################################################


#         // Assignment Operators/Operator Penugasan //

penugasan = '''
########################################################################

                " Assignment Operators/Operator Penugasan "


    Bahasa Python mendukung tipe operator penugasan

    Asumsikan variabel a memiliki nilai 10
    dan variabel b memiliki nilai 20

    [1] Equal ( = )

        (Menetapkan nilai dari operan sisi kanan ke operan sisi kiri)
        Contoh : c = a + b memasukan nilai dari a + b ke c



    [2] Add AND ( += )
    
        (Menambahkan operan kanan ke operan kiri dan menetapkan
        hasilnya ke operan kiri)
        Contoh : c += a sama seperti  c = c + a



    [3] Subtract AND ( -= )

        (Mengurangi operan kanan dari operan kiri
        dan menetapkan hasilnya ke operan kiri)
        Contoh : c += a sama seperti  c = c + a



    [4] Multiply AND ( *= )
    
        (Mengalikan operan kanan dengan operan kiri
        dan menetapkan hasil ke operan kiri)
        Contoh : c *= a sama seperti c = c * a



    [5] Divide AND ( /= )
    
        (Membagi operan kiri dengan operan kanan
        dan menetapkan hasilnya ke operan kiri)
        Contoh : c /= a atau c = c/a



    [6] Modulus AND ( %= )
    
        (Dibutuhkan modulus menggunakan dua operan
        dan menetapkan hasilnya ke operan kiri)
        Contoh : c %= a sama seperti c = c % a



    [7] Exponent AND ( **= )
    
        (Melakukan penghitungan eksponensial (daya) pada operator
        dan menetapkan nilai ke operan kiri)
        Contoh : c **= a sama seperti c = c ** a



    [8] Floor Division ( //= )
    
        (Melakukan pembagian lantai pada operator
        dan menetapkan nilai ke operan kiri)
        Contoh : c //= a sama seperti c = c // a

########################################################################
'''



def overview():
    ''' Assignment Operators/Operator Penugasan '''
    os.system("clear")
    sparator(" // Operator Penugasan // ")
    print(penugasan)



def equal():
    ''' Equal/Sama dengan '''
    os.system("clear")
    mini_sparator(" // Operator Penugasan // ")
    print('''
>> Equal ( = )

    Menetapkan nilai dari operan sisi kanan ke operan sisi kiri
    Contoh : c = a + b memasukan nilai dari a + b ke c
    ''')
    bottom_sparator()
    a = int(input("Masukan nilai a (integer/angka) : "))
    print("nilai a =", a)
    print("\n")
    b = int(input("Masukan nilai b (integer/angka) : "))
    print("nilai b =", b)
    c = a + b
    print("\n","    c = a + b atau", c, "=", a, "+", b)



def tambahAnd():
    ''' Add AND '''
    os.system("clear")
    mini_sparator(" // Operator Penugasan // ")
    print('''
>> Add AND ( += )

    Menambahkan operan kanan ke operan kiri dan menetapkan
    hasilnya ke operan kiri
    Contoh : c += a sama seperti  c = c + a
    ''')
    bottom_sparator()
    c = int(input("Masukan nilai c (integer/angka) : "))
    print("nilai c =", c)
    print("\n")
    a = int(input("Masukan nilai a (integer/angka) : "))
    print("nilai a =", a)
    c += a
    print("\n","    c += a atau c = c + a", ">>>", c)



def kurangAnd():
    ''' Subtract AND '''
    os.system("clear")
    mini_sparator(" // Operator Penugasan // ")
    print('''
>> Subtract AND ( -= )

    mengurangi operan kanan dari operan kiri
    dan menetapkan hasilnya ke operan kiri
    Contoh : c -= a sama seperti  c = c - a
    ''')
    bottom_sparator()
    c = int(input("Masukan nilai c (integer/angka) : "))
    print("Nilai c =", c)
    print("\n")
    a = int(input("Masukan nilai a (integer/angka) : "))
    print("Nilai a =", a)
    c -= a
    print("\n",    "c -= a atau c = c - a", ">>>", c)



def kaliAnd():
    ''' Multiply AND '''
    os.system("clear")
    mini_sparator(" // Operator Penugasan // ")
    print('''
>> Multiply AND ( *= )

    Mengalikan operan kanan dengan operan kiri
    dan menetapkan hasil ke operan kiri
    Contoh : c *= a sama seperti c = c * a
    ''')
    bottom_sparator()
    c = int(input("Masukan nilai c (integer/angka) : "))
    print("Nilai c =", c)
    print("\n")
    a = int(input("Masukan nilai a (integer/angka) : "))
    print("Nilai a =", a)
    c *= a
    print("\n", "    c *= a atau c = c * a", ">>>", c)



def bagiAnd():
    ''' Divide AND '''
    os.system("clear")
    mini_sparator(" // Operator Penugasan // ")
    print('''
>> Divide AND ( /= )

    Membagi operan kiri dengan operan kanan
    dan menetapkan hasilnya ke operan kiri
    Contoh : c /= a atau c = c/a
    ''')
    bottom_sparator()
    c = int(input("Masukan nilai c (integer/angka) : "))
    print("Nilai c =", c)
    print("\n")
    a = int(input("Masukan nilai a (integer/angka) : "))
    print("Nilai a =", a)
    c /= a
    print("\n", "    c /= a atau c = c /- a", ">>>", c)



def modulusAnd():
    ''' Modulus AND '''
    os.system("clear")
    mini_sparator(" // Operator Penugasan // ")
    print('''
>> Modulus AND ( %= )

    Dibutuhkan modulus menggunakan dua operan
    dan menetapkan hasilnya ke operan kiri
    Contoh : c %= a sama seperti c = c % a
    ''')
    bottom_sparator()
    c = int(input("Masukan nilai c (integer/angka) : "))
    print("Nilai c =", c)
    print("\n")
    a = int(input("Masukan nilai a (integer/angka) : "))
    print("Nilai a =", a)
    c %= a
    print("\n", "   c %= a atau c = c % a", ">>>", c)



def kuadratAnd():
    ''' Exponent AND '''
    os.system("clear")
    mini_sparator(" // Operator Penugasan // ")
    print('''
>> Exponent AND ( **= )

    Melakukan penghitungan eksponensial (daya) pada operator
    dan menetapkan nilai ke operan kiri
    Contoh : c **= a sama seperti c = c ** a
    ''')
    bottom_sparator()
    c = int(input("Masukan nilai c (integer/angka) : "))
    print("Nilai c =", c)
    print("\n")
    a = int(input("Masukan nilai a (integer/angka) : "))
    print("Nilai a =", a)
    c **= a
    print("\n", "    c **= a atau c = c ** a", ">>>", c)



def divisionAnd():
    ''' Floor Division '''
    os.system("clear")
    mini_sparator(" // Operator Penugasan // ")
    print('''
>> Floor Division ( //= )

    Melakukan pembagian lantai pada operator
    dan menetapkan nilai ke operan kiri
    Contoh : c //= a sama seperti c = c // a
    ''')
    bottom_sparator()
    c = int(input("Masukan nilai c (integer/angka) : "))
    print("Nilai c =", c)
    print("\n")
    a = int(input("Masukan nilai a (integer/angka) : "))
    print("Nilai a =", a)
    c //= a
    print("\n", "    c //= a atau c = c // a", ">>>", c)




def operator_penugasan():
    os.system("clear")
    while True:
        option_program()
        def exit_():
            print("[X] exit")
        exit_()
        opt = input(">>> ").lower()
        if opt == "0":
            overview()
            option_back_exit()
            in_overview = input(">>> ").lower()
            if in_overview == "0":
                option_program()
            elif in_overview == "x":
                clear_exit()
            else:
                force_close_program()
        elif opt == "1":
            equal()
            option_back_exit()
            in_equal = input(">>> ").lower()
            if in_equal == "0":
                overview()
            elif in_equal == "x":
                clear_exit()
            else:
                force_close_program()
        elif opt == "2":
            tambahAnd()
            option_back_exit()
            in_ = input(">>> ").lower()
            if in_ == "0":
                overview()
            elif in_ == "x":
                clear_exit()
            else:
                force_close_program()
        elif opt == "3":
            kurangAnd()
            option_back_exit()
            in_ = input(">>> ").lower()
            if in_ == "0":
                overview()
            elif in_ == "x":
                clear_exit()
            else:
                force_close_program()
        elif opt == "4":
            kaliAnd()
            option_back_exit()
            in_ = input(">>> ").lower()
            if in_ == "0":
                overview()
            elif in_ == "x":
                clear_exit()
            else:
                force_close_program()
        elif opt == "5":
            bagiAnd()
            option_back_exit()
            in_ = input(">>> ").lower()
            if in_ == "0":
                overview()
            elif in_ == "x":
                clear_exit()
            else:
                force_close_program()
        elif opt == "6":
            modulusAnd()
            option_back_exit()
            in_ = input(">>> ").lower()
            if in_ == "0":
                overview()
            elif in_ == "x":
                clear_exit()
            else:
                force_close_program()
        elif opt == "7":
            kuadratAnd()
            option_back_exit()
            in_ = input(">>> ").lower()
            if in_ == "0":
                overview()
            elif in_ == "x":
                clear_exit()
            else:
                force_close_program()
        elif opt == "8":
            divisionAnd()
            option_back_exit()
            in_ = input(">>> ").lower()
            if in_ == "0":
                overview()
            elif in_ == "x":
                clear_exit()
            else:
                force_close_program()
        elif opt == "x":
            clear_exit()
        else:
            print("in process")
            force_close_program()



########################################################################

# overview()
# equal()
# tambahAnd()
# kurangAnd()
# kaliAnd()
# bagiAnd()
# modulusAnd()
# kuadratAnd()
# divisionAnd()
# clear_screen()
operator_penugasan()

########################################################################