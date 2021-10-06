from time import sleep
import helper
import variabel

helper.clear()
def variabel_progrem():
    while True:
        helper.clear()
        variabel.variabel_menu()
        helper.option_back_exit()
        in_var_prog = input(">>> ").lower()
        if in_var_prog == "0":
            helper.clear()
            helper.sparator(" // Variabel // ")
            sleep(3)
            print("In Process... {O_*} ")
            sleep(3)
            helper.clear()
            variabel.variabel_menu()
        elif in_var_prog == "x":
            helper.clear_exit()
        elif in_var_prog == "1":
            helper.clear()
            variabel.overview_variabel()
            helper.option_back_exit()
            in_var_overv = input(">>> ").lower()
            if in_var_overv == "0":
                helper.clear()
                variabel.variabel_menu()
            elif in_var_overv == "x":
                helper.clear_exit()
            else:
                helper.force_close_program()
        elif in_var_prog == "2":
            helper.clear()
            variabel.nilai_variabel()
            helper.option_back_exit()
            in_var_overv = input(">>> ").lower()
            if in_var_overv == "0":
                helper.clear()
                variabel.variabel_menu()
            elif in_var_overv == "x":
                helper.clear_exit()
            else:
                helper.force_close_program()
        elif in_var_prog == "3":
            helper.clear()
            variabel.multiple_assignment()
            helper.option_back_exit()
            in_var_mulass = input(">>> ").lower()
            if in_var_mulass == "0":
                helper.clear()
                variabel.variabel_menu()
            elif in_var_mulass == "x":
                helper.clear_exit()
            else:
                helper.force_close_program()
        elif in_var_prog == "4":
            helper.clear()
            variabel.tipe_data()
            helper.option_back_exit()
            in_var_tipdat = input(">>> ").lower()
            if in_var_tipdat == "0":
                helper.clear()
                variabel.variabel_menu()
            elif in_var_tipdat == "x":
                helper.clear_exit()
            else:
                helper.force_close_program()
        elif in_var_prog == "5":
            helper.clear()
            variabel.Python_number()
            helper.option_back_exit()
            in_var_num = input(">>> ").lower()
            if in_var_num == "0":
                helper.clear()
                variabel.variabel_menu()
            elif in_var_num == "x":
                helper.clear_exit()
            else:
                helper.force_close_program()
        elif in_var_prog == "6":
            helper.clear()
            variabel.python_string()
            helper.option_back_exit()
            in_var_str = input(">>> ").lower()
            if in_var_str == "0":
                helper.clear()
                variabel.variabel_menu()
            elif in_var_str == "x":
                helper.clear_exit()
            else:
                helper.force_close_program()
        elif in_var_prog == "7":
            helper.clear()
            variabel.python_list()
            helper.option_back_exit()
            in_var_lis = input(">>> ").lower()
            if in_var_lis == "0":
                helper.clear()
                variabel.variabel_menu()
            elif in_var_lis == "x":
                helper.clear_exit()
            else:
                helper.force_close_program()
        elif in_var_prog == "8":
            helper.clear()
            variabel.python_tuple()
            helper.option_back_exit()
            in_var_tup = input(">>> ").lower()
            if in_var_tup == "0":
                helper.clear()
                variabel.variabel_menu()
            elif in_var_tup == "x":
                helper.clear_exit()
            else:
                helper.force_close_program()
        elif in_var_prog == "9":
            helper.clear()
            variabel.python_dictionary()
            helper.option_back_exit()
            in_var_dic = input(">>> ").lower()
            if in_var_dic == "0":
                helper.clear()
                variabel.variabel_menu()
            elif in_var_dic == "x":
                helper.clear_exit()
            else:
                helper.force_close_program()
        elif in_var_prog == "10":
            helper.clear()
            variabel.konversi_tipe_data()
            helper.option_back_exit()
            in_var_ktd = input(">>> ").lower()
            if in_var_ktd == "0":
                helper.clear()
                variabel.variabel_menu()
            elif in_var_ktd == "x":
                helper.clear_exit()
            else:
                helper.force_close_program()
        else:
            helper.force_close_program()


variabel_progrem()