#!/usr/bin/env python
# encoding: utf-8
"""
file_name.py

Created by Author_Name on 10/4/21.
Copyright (c) 2021 Copyright Holder. All rights reserved.
"""

########################################################################

import os
import time
import helper
from variabel import variabel

########################################################################

def main_python_basic_program():
        helper.python_basic()
        option = input(">>> ").lower()
        if option == "x":
            helper.clear_exit()
        elif option == "1":
            print("in process...!!!")
        else:
            helper.force_close_program()



def start_variabel_progrem():
    helper.clear()
    def option_program():
            helper.back_exit()
            option = input(">>> ").lower()
            if option == "0":
                helper.clear()
                variabel.variabel_menu()
            elif option == "x":
                helper.clear_exit()
            else:
                helper.force_close_program()

    while True:
        helper.clear()
        variabel.variabel_menu()
        helper.back_exit()
        option = input(">>> ").lower()
        if option == "0":
            helper.clear()
            main_python_basic_program()
        elif option == "x":
            helper.clear_exit()
        elif option == "1":
            helper.clear()
            variabel.overview_variabel()
            option_program()
        elif option == "2":
            helper.clear()
            variabel.nilai_variabel()
            option_program()
        elif option == "3":
            helper.clear()
            variabel.multiple_assignment()
            option_program()
        elif option == "4":
            helper.clear()
            variabel.tipe_data()
            option_program()
        elif option == "5":
            helper.clear()
            variabel.Python_number()
            option_program()
        elif option == "6":
            helper.clear()
            variabel.python_string()
            option_program()
        elif option == "7":
            helper.clear()
            variabel.python_list()
            option_program()
        elif option == "8":
            helper.clear()
            variabel.python_tuple()
            option_program()
        elif option == "9":
            helper.clear()
            variabel.python_dictionary()
            option_program()
        elif option == "10":
            helper.clear()
            variabel.konversi_tipe_data()
            option_program()
        else:
            helper.force_close_program()

main_python_basic_program()
