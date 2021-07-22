def checkMain():
    print("ini adalah fiie", __name__)

if __name__ == "__main__":
    checkMain()



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

checkMain()