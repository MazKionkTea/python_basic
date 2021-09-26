#!/usr/bin/env python
# encoding: utf-8
"""
variabel.py

Created by Author_Name on 9/13/21.
Copyright (c) 2021 Copyright Holder. All rights reserved.
"""

########################################################################

import os

########################################################################


def sparator(arg):
    ''' sparator '''
    print("#".center(72, "#"))
    print(arg.center(72, "#"))
    print("#".center(72, "#"))
    print("\n")
sparator(" // Variabel // ")

variabel = open("2_Variabel/variabel.txt", "r")

def overview():
    ''' overview '''
    print(variabel.read(401))

def nilai_variabel():
    ''' Assigning Values to Variables '''
    variabel.read(220)

    nama = "Hama Wereng"    # string
    tinggi = 157            # integer
    berat = 57,8            # float

    print(nama)
    print(tinggi)
    print(berat)




########################################################################

# overview()
nilai_variabel()

########################################################################

if __name__ == '__main__':
	print(__name__)