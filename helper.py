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

def sparator(arg):
    print("#".center(72, "#"))
    print(arg.center(72, "#"))
    print("#".center(72, "#"))

def title_sparator(arg):
    print(arg.center(72, "#"))

def mini_sparator():
    # print("\n")
    print("#".center(72, "#"))
    # print("\n")

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
    print('''
    [0] Back
    [X] Exit
    ''')
    print("Pilih Nomor Program")

def test_init():
    print("ini dari file init...")

def check_main():
    if __name__ == "__main__":
        print(__name__)
