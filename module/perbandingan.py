  
  
#         // Comparison (Relational) Operators/Operator Perbandingan //

# Operator ini membandingkan nilai di kedua sisinya dan memutuskan hubungan di antara mereka.
# Mereka juga disebut operator relasional.


# Asumsikan variabel a memegang nilai 10 dan variabel b memegang nilai 20

    # == (sama sengan)
    # Jika nilai dua operan sama, maka kondisinya menjadi true.
    # (a == b) is not true.
def sd(a, b):
    print("Operator Perbandingan Sama Dengan")
    print("=" * 50)
    if a == b:
        print(a, "sama dengan", b)
    else:
        print(a, "tidak sama dengan", b)


    # != (tidak sama dengan)
    # Jika nilai dari dua operan tidak sama, maka kondisi menjadi true.
    # (a != b) is true.
def tsd(a, b):
    if a != b:
        print(True)
    else:
        print(False)


    # > (lebih besar dari)
    # Jika nilai operan kiri lebih besar dari nilai operan kanan, maka kondisi menjadi true.
    # (a > b) is not true.
def lbd(a, b):
    if a > b:
        print(True)
    else:
        print(False)


    # < (lebih kurang dari)
    # Jika nilai operan kiri kurang dari nilai operan kanan, maka kondisi menjadi true.
    # (a < b) is true.
def lkd(a, b):
    if a < b:
        print(True)
    else:
        print(False)


    # >= (lebih besar dari atau sama dengan)
    # Jika nilai operan kiri lebih besar dari atau sama dengan nilai operan kanan, maka kondisi menjadi true.
    # (a >= b) is not true.
def lbdasd(a, b):
    if a >= b:
        print(True)
    else:
        print(False)


    # <= (lebih kurang dari atau sama dengan)
    # Jika nilai operan kiri kurang dari atau sama dengan nilai operan kanan, maka kondisi menjadi true.
    # (a <= b) is true.
def lkdasd(a, b):
    if a <= b:
        print(True)
    else:
        print(False)


    # <> (tidak sama dengan)
    # jika nilai dari kedua operan tidak sama, maka kondisi menjadi true.
    # (a <> b) is true. operator ini sejenis dengan operator !=.
# def tsd2(a, b):
#     if a <> b:
#         print(True)
#     else:
#         print(False)
    
    sd(10, 20)