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

def sparator(arg):
    print("#".center(72, "#"))
    print(arg.center(72, "#"))
    print("#".center(72, "#"))
sparator(" // Basic Operator // ")

########################################################################

aritmatic = '''
########################################################################

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

########################################################################
'''

# •	Arithmetic Operators/Operator Aritmatika

def aritmatika():
    ''' Operator Aritmatika '''
    print(aritmatic)

# Addition/penjumlahan
def tambah(a, b):
    ''' Penjumlahan '''
    c = a + b
    return c
# tambah(10, 3)

# Subtraction/pengurangan
def kurang(a, b):
    ''' Pengurangan '''
    c = a - b
    return c
# kurang(15, 2)

# Multiplication/perkalian
def kali(a, b):
    ''' Perkalian '''
    c = a * b
    return c
# kali(5, 5)

# Division/pembagian
def bagi(a, b):
    ''' Pembagian '''
    c = a / b
    return c
# bagi(10, 3)

# Exponent/Pangkat Kuadrat
def kuadrat(a, b):
    ''' Pangkat Kuadrat '''
    c = a ** b
    return c
# kuadrat(2, 5)

# jika sisa pembagian 1 = ganjil
# jika sisa pembagian 0 = genap
def modulus(a, b):
    ''' Modulus/SisaBagi Hasil '''
    c = a % b
    return c 
# modulus(13, 3)

# Pembagian operan di mana hasilnya adalah quotient
# # di mana digit setelah koma desimal dihapus
def division(a, b):
    ''' Floor Division '''
    # 9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0
    c = a // b
    return c
# division(16, 3)

########################################################################

# aritmatika()
# tambah()
# kurang()
# kali()
# bagi()
# kuadrat()
# modulus()
# division()

########################################################################