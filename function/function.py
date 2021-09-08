def sparator(arg = "#"):
    print("\n" * 3)
    print("#".center(59, "#"))
    print(arg.center(59, "#"))
    print("#".center(59, "#"))



def overview():
    sparator(" // Fungsi // ")
    print('''
    Fungsi adalah sebuah blok kode yang teratur, dan bisa dipakai
    secara berulang kali. menggunakan Fungsi dalam python menjadikan
    aplikasi kita lebih teratur. python menyediakan kita built-in fungsi
    seperti perintah print() dan lain-lain adalah yang bisa dipanggil
    atau dieksekusi berulang kali.

    tapi kita juga bisa membuat fungsi kita sendiri yang
    didefinisikan/ditetapkan oleh kita sendiri.
    ''')



    def mendefinisikan_fungsi():
        sparator(" // Mendefinisikan Sebuah Fungsi // ")
        print('''
        kita bisa mendefinisikan sebuah fungsi berdasarkan jenis fungsi itu sendiri.
        ada beberapa aturan jika ingin membuat sebuah fungsi dalam python

        > blok kode fungsi diawali dengan keyword def
        di'ikuti nama fungsi nya dilanjutkan dengan
        tanda kurung ( () ) diakhiri dengan titik dua (:)
        
        > apapun input parameter atau argumen harus
        ditempatkan didalam tanda kurung. kita juga bisa
        menentukan parameter didalam kurung tersebut.
        
        > statemen pertama dalam sebuah fungsi bisa
        saja opsional statement.
        
        > setiap kode fungsi dimulai dengan tanda titik
        dua (:) dan indentasi
        
        > statement dari return [expression] adalah akhir
        dari blok kode fungsi. sebagai pilihan, return
        expression/return statement tanpa argumen bisa
        dilewati, tetapi nilai dari return'nya bersifat none.
        
        Sintaks :
        
            def namaFungsi( parameter ):
                "function_docstring"
                function_suite
                return [expression]
                
                atau
                
            def namaFungsi(parameter):
                kondisi
                aksi
                return aksi
            
        secara default, parameter memiliki tingkah laku
        tergantun posisi dan didefinisikan dari fungsi tsb. 
        
        contoh:
        
            def printme(str):
                "tulisan ini dilewati dalam fungsi ini"
                print(str)
                return
            
            printme()
        
        berdasarkan contoh di atas, fungsi ini mengabil
        string parameter sebagai input dan akan dicetak
        dilayar setelah fungsinya di panggil.

        ketika kode dijalankan akan menampilkan :
        ''')

        def printme(str):
                print("tulisan ini dilewati dalam fungsi ini")
                print(str)
                return
            
        printme("ok")
        # karena contoh fungsi ini membutuhkan sebuah argumen/parameter
        # yang memiliki tipe data string (str) maka argumennya/parameter
        # harus diisi oleh string
    
    mendefinisikan_fungsi()



    def memangil_fungsi():
        sparator(" // Memangil Sebuah Fungsi // ")
        print('''
        mendefinisikan fungsi melalui nama, secara spesifik parameter tersebut
        dimasukan kedalam fungsi dan stuktur blok kode.
        dan cara mengeksekusi/memanggil fungsi tersebut dengan cara mengetikan
        nama dari fungsi tersebut. dari contoh fungsi di atas,
        kita cukup mengetikan printme(). karena fungsi di atas memiliki
        parameter str, berarti kita harus memasukan parameter string didalam
        tanda kurung tersebut. dan cara pemanggilannya printme("wkwkwkwk")
        ''')
    
    memangil_fungsi()
