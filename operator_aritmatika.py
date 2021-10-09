#!/usr/bin/env python
# encoding: utf-8
"""
basic_operator.py

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

from os import initgroups
import helper

########################################################################

helper.sparator(" // Basic Operator // ")

operator_aritmatika = '''
            " Arithmetic Operators/Operator Aritmatika "               


    Bahasa Python mendukung tipe operator berikut

    Asumsikan variabel a memiliki nilai 10 dan variabel b memiliki nilai 21

    [1]  +   (Penjumlahan)          Contoh : a + b = 31
    [2]  -   (Pengurangan)          Contoh : a – b = -11
    [3]  *   (Perkalian)            Contoh : a * b = 210
    [4]  /   (Pembagian)            Contoh : b / a = 2.1
    [5]  **  (Perpangkatan)         Contoh : a**b =10 to the power 20
    [6]  %   (Modulus)              Contoh : b % a = 1
    [7]  //  (Floor Division)       Contoh : 9//2 = 4 and 9.0//2.0 = 4.0
'''

# •	Arithmetic Operators/Operator Aritmatika
def overview_aritmatika():
    ''' Operator Aritmatika '''
    helper.clear()
    helper.title_sparator(" // Basic Operator // ")
    print(operator_aritmatika)
    helper.mini_sparator
    helper.option_back_exit

# Addition/penjumlahan
def tambah():
    ''' Penjumlahan '''
    helper.clear()
    helper.title_sparator("// Penjumlahan //")
    a = input("Masukan nilai a (integer/angka) : ")
    print("Nilai a = ", a)
    b = input("Masukan nilai b (integer/angka) : ")
    print("Nilai b = ", b)
    c = a + b
    print("c = a + b")
    print(a + b)
    return c

# Subtraction/pengurangan
def kurang():
    ''' Pengurangan '''
    helper.clear()
    helper.title_sparator("// Pengurangan //")
    a = input("Masukan nilai a (integer/angka) : ")
    print("Nilai a = ", a)
    b = input("Masukan nilai b (integer/angka) : ")
    print("Nilai b = ", b)
    c = a - b
    print("c = a + b")
    print(a - b)
    return c

# Multiplication/perkalian
def kali():
    ''' Perkalian '''
    helper.clear()
    helper.title_sparator("// Perkalian //")
    a = input("Masukan nilai a (integer/angka) : ")
    print("Nilai a = ", a)
    b = input("Masukan nilai b (integer/angka) : ")
    print("Nilai b = ", b)
    print("c = a * b")
    c = a * b
    return c

# Division/pembagian
def bagi():
    ''' Pembagian '''
    helper.clear()
    helper.title_sparator("// Pembagian //")
    a = input("Masukan nilai a (integer/angka) : ")
    print("Nilai a = ", a)
    b = input("Masukan nilai b (integer/angka) : ")
    print("Nilai b = ", b)
    print("c = a / b")
    c = a / b
    return c

# Exponent/Pangkat Kuadrat
def kuadrat():
    ''' Pangkat Kuadrat '''
    helper.clear()
    helper.title_sparator("// Pangkat Kuadrat //")
    a = input("Masukan nilai a (integer/angka) : ")
    print("Nilai a = ", a)
    b = input("Masukan nilai b (integer/angka) : ")
    print("Nilai b = ", b)
    print("c = a ** b")
    c = a ** b
    return c
# kuadrat(2, 5)

# jika sisa pembagian 1 = ganjil
# jika sisa pembagian 0 = genap
def modulus():
    ''' Modulus/SisaBagi Hasil '''
    helper.clear()
    helper.title_sparator("// Modulus/SisaBagi Hasil //")
    a = input("Masukan nilai a (integer/angka) : ")
    print("Nilai a = ", a)
    b = input("Masukan nilai b (integer/angka) : ")
    print("Nilai b = ", b)
    print("c = a % b")
    c = a % b
    return c 
# modulus(13, 3)

# Pembagian operan di mana hasilnya adalah quotient
# # di mana digit setelah koma desimal dihapus
def division():
    ''' Floor Division '''
    helper.clear()
    helper.title_sparator("// Floor Division //")
    a = input("Masukan nilai a (integer/angka) : ")
    print("Nilai a = ", a)
    b = input("Masukan nilai b (integer/angka) : ")
    print("Nilai b = ", b)
    # 9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0
    print("c = a // b")
    c = a // b
    return c
# division(16, 3)

########################################################################
fungsi = ([
    overview_aritmatika(),
    tambah(),
    kurang(),
    kali(),
    bagi(),
    kuadrat(),
    modulus(),
    division()
])

print(type(fungsi))
########################################################################

# def start_operator_aritmatika():
#     while True:
#         helper.clear()
#         overview_aritmatika()
#         helper.option_back_exit()
#         option = input(">>> ").lower()
#         if option == "0":
#             helper.clear
#             overview_aritmatika()
#         elif option == "x":
#             helper.clear_exit
#         elif option == "1":
#             tambah()
#             helper.option_back_exit()
#             option = input(">>> ").lower()
#             if option == "0":
#                 helper.clear
#                 overview_aritmatika()
#             elif option == "x":
#                 helper.clear_exit
#             else:
#                 helper.force_close_program
#         else:
#             helper.force_close_program

# start_operator_aritmatika()

def pilih_program():
    option = input(">>> ").lower()
    if option == "0":
        helper.clear
        fungsi[0]
    elif option == "x":
        helper.clear_exit
    else:
        helper.force_close_program

# pilih_program()