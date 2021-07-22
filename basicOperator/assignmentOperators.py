#         // Assignment Operators/Operator Penugasan //

def penugasan():
    print(
        """
        #=====================================================================================#
        #                                                                                     #
        #                                                                                     #
        #                   " Assignment Operators/Operator Penugasan "                       #
        #                                                                                     #
        #                                                                                     #
        #           Bahasa Python mendukung tipe operator berikut                             #
        #                                                                                     #
        #                                                                                     #
        #       Asumsikan variabel a memiliki nilai 10 dan variabel b memiliki nilai 20       #
        #                                                                                     #
        #       [1]  =    (Menetapkan nilai dari operan sisi kanan ke operan sisi kiri)       #
        #                  Contoh : c = a + b memasukan nilai dari a + b ke c                 #
        #                                                                                     #
        #       [2]  +=   (Ini menambahkan operan kanan ke operan kiri dan menetapkan         #
        #                  hasilnya ke operan kiri)                                           #
        #                  Contoh : c += a sama seperti  c = c + a                            #
        #                                                                                     #
        #       [3]  *=   (Ini mengalikan operan kanan dengan operan kiri                     #
        #                  dan menetapkan hasil ke operan kiri)                               #
        #                  Contoh : c *= a sama seperti c = c * a                             #
        #                                                                                     #
        #       [4]  /=   (Ini membagi operan kiri dengan operan kanan                        #
        #                  dan menetapkan hasilnya ke operan kiri)                            #
        #                  Contoh : c /= a atau c = c/ac. /= a atau c = c/a                   #
        #                                                                                     #
        #       [5]  %=   (Dibutuhkan modulus menggunakan dua operan                          #
        #                  dan menetapkan hasilnya ke operan kiri)                            #
        #                  Contoh : c %= a sama seperti c = c % a                             #
        #                                                                                     #
        #       [6]  **=  (Melakukan penghitungan eksponensial (daya) pada operator           #
        #                  dan menetapkan nilai ke operan kiri)                               #
        #                  Contoh : c **= a sama seperti c = c ** a                           #
        #                                                                                     #
        #       [7]  //=  (Ini melakukan pembagian lantai pada operator                       #
        #                  dan menetapkan nilai ke operan kiri)                               #
        #                  Contoh : c //= a sama seperti c = c // a                           #
        #                                                                                     #
        #                                                                                     #
        #    [00]   Back                                                                      #
        #    [99]   Exit                                                                      #
        #                                                                                     #
        #                                                                                     #
        #=====================================================================================#
        """
    )

    # =
    # Menetapkan nilai dari operan sisi kanan ke operan sisi kiri 	
    # c = a + b menugaskan nilai untuk a + b kedalam variabel c
def equal(a):
    print(
    "=" * 20, "Equal", "=" * 20,
    """
    Menetapkan nilai dari operan sisi kanan
    ke operan sisi kiri

    """
    )
    var = a
    print(">>>  ", a)
    print("\n", "=" * 50)
    return var
# equal("kontol")

    # += Add AND
    # Ini menambahkan operan kanan ke operan kiri dan menetapkan hasilnya ke operan kiri
    # c += a setara dengan c = c + a
def tambahAnd(a, b):
    print(
    "=" * 20, "Add AND", "=" * 20,
    """
    menambahkan operan kanan ke operan kiri
    dan menetapkan hasilnya ke operan kiri
    """
    )
    a += b
    print(">>>  ", a)
    print("\n", "=" * 50)
    return a
# tambahAnd(10, 3)

    # -= Subtract AND
    # Ini mengurangi operan kanan dari operan kiri dan menetapkan hasilnya ke operan kiri
    # c -= a setara dengan c = c - a
def kurangAnd(a, b):
    print(
    "=" * 20, "Subtract AND", "=" * 20,
    """
    mengurangi operan kanan dari operan kiri
    dan menetapkan hasilnya ke operan kiri
    """
    )
    a -= b
    print(">>>  ", a)
    print("\n", "=" * 50)
    return a
# kurangAnd(100, 13)

    # *= Multiply AND
    # Ini mengalikan operan kanan dengan operan kiri dan menetapkan hasil ke operan kiri
    # c *= a setara dengan c = c * a
def kaliAnd(a, b):
    print(
    "=" * 20, "Multiply AND", "=" * 20,
    """
    mengalikan operan kanan dari operan kiri
    dan menetapkan hasilnya ke operan kiri
    """
    )
    a *= b
    print(">>>  ", a)
    print("\n", "=" * 50)
    return a
# kaliAnd(23, 7)

    # /= Divide AND
    # Ini membagi operan kiri dengan operan kanan dan menetapkan hasilnya ke operan kiri
    # c /= a setara dengan c = c / a
def bagiAnd(a, b):
    print(
    "=" * 20, "Divide AND", "=" * 20,
    """
    membagi operan kanan dari operan kiri
    dan menetapkan hasilnya ke operan kiri
    """
    )
    a /= b
    print(">>>  ", a)
    print("\n", "=" * 50)
    return a
# bagiAnd(97, 5)

    # **= Exponent AND
    # Melakukan penghitungan eksponensial (daya/pangkat kuadrat) pada operator dan menetapkan nilai ke operan kiri
    # c **= a setara dengan c = c ** a
def kuadratAnd(a, b):
    print(
    "=" * 20, "Exponent AND", "=" * 20,
    """
    Melakukan penghitungan eksponensial (daya/pangkat kuadrat)
    pada operator dan menetapkan nilai ke operan kiri
    """
    )
    a **= b
    print(">>>  ", a)
    print("\n", "=" * 50)
    return a
# kuadratAnd(2, 5)

    # %= Modulus AND
    # Dibutuhkan modulus menggunakan dua operan dan menetapkan hasilnya ke operan kiri
    # c %= a setara dengan c = c % a
def modulusAnd(a, b):
    print(
    "=" * 20, "Modulus AND", "=" * 20,
    """
    modulus menggunakan dua operan
    dan menetapkan hasilnya ke operan kiri
    """
    )
    a %= b
    print(">>>  ", a)
    print("\n", "=" * 50)
    return a
# modulusAnd(10, 3)

    # //= Floor Division
    # Ini melakukan pembagian lantai pada operator dan menetapkan nilai ke operan kiri
    # c //= a is setara dengan c = c // a
def divisionAnd(a, b):
    print(
    "=" * 20, "Floor Division", "=" * 20,
    """
    Ini melakukan pembagian lantai pada operator
    dan menetapkan nilai ke operan kiri
    """
    )
    a //= b
    print(">>>  ", a)
    print("\n", "=" * 50)
    return a
#divisionAnd(10, 3)