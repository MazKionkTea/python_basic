#!/usr/bin/env python
# encoding: utf-8
"""
helper.py

Created by MazKionkTea on 9/27/21.
Copyright (c) 2021 Copyright Holder. All rights reserved.
"""

########################################################################

import os
from time import sleep

########################################################################

def header(arg):
    ''' Make a Title Header '''
    print("#".center(72, "#"))
    print(arg.center(72, "#"))
    print("#".center(72, "#"))

def title_sparator(arg):
    ''' Title and Sparator '''
    print(arg.center(72, "#"))

def mini_sparator():
    ''' One Line Sparator '''
    print("#".center(72, "#"))

def clear():
    ''' Clear Terminal Console '''
    os.system("clear")

def clear_exit():
    ''' Exit from program and
    Clear Terminal Console '''
    os.system("clear")
    exit()

def force_close_program():
    ''' Force Close Program
    if something didn't work '''
    print("input error... program akan ditutup...!!!")
    sleep(5)
    os.system("clear")
    exit()

def home_back_exit():
    ''' Option Home, Back and Exit
    from sub program '''

def back_exit():
    ''' Option Back or Exit
    from main program '''
    print('''
    [0] Back
    [X] Exit
    ''')
    print("Pilih Nomor Program")

def option_back_exit(program):
    option = input(">>> ")
    if option == "x":
        clear_exit()
    elif option == "0":
        clear()
        program
    else:
        force_close_program()

def python_basic():
    ''' Python Main Home
    Basic Program '''
    clear()
    header(" // Python Basic // ")
    print('''
    [1]     Basic Syntax
    [2]     Variable
    [3]     Basic Operator
    [4]     Data Type (Number, String, List, Tuple, Dictionary)
    [5]     Decision Making
    [6]     Loops
    [7]     Function
    [8]     Module
    [9]     Exception Handling
    [10]    Date & Time
    [11]    File I/O
    ''')
    mini_sparator()
    print('''
    [X] Exit
    ''')


def check_main():
    if __name__ == "__main__":
        print(__name__)
