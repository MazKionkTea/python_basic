# •	Arithmetic Operators/Operator Aritmatika

# Addition/penjumlahan
def tambah(a, b):
    c = a + b
    print(
    "=" * 20, "Penjumlahan", "=" * 20,
    """
    """
    )
    print(">>>  ", a, "+", b, "=", c)
    print("\n", "=" * 50)
    return c
# tambah(10, 3)

# Subtraction/pengurangan
def kurang(a, b):
    c = a - b
    print(
    "=" * 20, "Pengurangan", "=" * 20,
    """
    """
    )
    print(">>>  ", a, "-", b, "=", c)
    print("\n", "=" * 50)
    return c
# kurang(15, 2)

# Multiplication/perkalian
def kali(a, b):
    c = a * b
    print(
    "=" * 20, "Perkalian", "=" * 20,
    """
    """
    )
    print(">>>  ", a, "x", b, "=", c)
    print("\n", "=" * 50)
    return c
# kali(5, 5)

# Division/pembagian
def bagi(a, b):
    c = a / b
    print(
    "=" * 20, "Pembagian", "=" * 20,
    """
    """
    )
    print(">>>  ", a, "/", b, "=", c)
    print("\n", "=" * 50)
    return c
# bagi(10, 3)

# Exponent/Pangkat Kuadrat
def kuadrat(a, b):
    c = a ** b
    print(
    "=" * 20, "Pangkat Kuadrat", "=" * 20,
    """
    """
    )
    print(">>>  ", a, "**", b, "=", c)
    print("\n", "=" * 50)
    return c
# kuadrat(2, 5)

# Modulus/SisaBagi Hasil
# jika sisa pembagian 1 = ganjil
# jika sisa pembagian 0 = genap
def modulus(a, b):
    c = a % b
    print(
    "=" * 20, "Modulus", "=" * 20,
    """
    """
    )
    print(">>>  ", a, "%", b, "=", c)
    print("\n", "=" * 50)
    return c 
# modulus(13, 3)

# floorDivision
# Pembagian operan di mana hasilnya adalah quotient
# # di mana digit setelah koma desimal dihapus
def division(a, b):
    # 9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0
    c = a // b
    print(
    "=" * 20, "Floor Division", "=" * 20,
    """
    """
    )
    print(">>>  ", a, "//", b, "=", c)
    print("\n", "=" * 50)
    return c
# division(16, 3)