#!/usr/bin/env python
# encoding: utf-8
"""
basic_operator.py

Created by MazKionkTea on 10/9/21.
Copyright (c) 2021 Copyright Holder. All rights reserved.
"""

########################################################################

import sys
from time import sleep
from ...python_basic.basic_operator import init_cek
from helper import clear, header
import operator_aritmatika

########################################################################

sys.path
header(" // Basic Operator // ")

overview_basic_operator = '''
- Tipe Operator Yang Didukung Dalam Bahasa Pemrograman Python

    [1]   Arithmetic Operators/Operator Aritmatika
    [2]   Comparison (Relational) Operators/Operator Perbandingan
    [3]   Assignment Operators/Operator Penugasan
    [4]   Logical Operators/Operator Logika
    [5]   Membership Operators/Operator Keanggotaan
    [6]   Identity Operators/Operator Identitas
    [7]   Bitwise Operators/Operator Bitwise
'''
def basic_operator():
    clear()
    print(overview_basic_operator)

init_cek()
sleep(5)
clear()

def check_main():
	if __name__ == '__main__':
		print(__name__)