pilihan = "y"
while pilihan == "y":
    print("""
    +-------------------------------+
               KOPI KOPO
    +-------------------------------+
    A. ES Kopi Susu   : Rp 11.000,-
    B. ES Kopi Coklat : Rp 12.000,-
    C. Capuccino Panas: Rp 11.000,-
    D. Ice Americano  : Rp 14.000,-
    +-------------------------------+
    Note :
        Silahkan Dipesan Sesuai Ruls
    """)
    pesan = str(input("Input a,b,c Atau d Dibawah \n"
                      "Silahkan Input : "))
    jumlahpesan = int(input("Masukan Jumlah Pesanan : "))
    if pesan == "a":
        listnama = "ES Kopi Susu"
        harga = (11000 * jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga = int(harga - diskon + ppn)
        else:
            diskon = (0)
            totalharga = int(harga + ppn)
    elif pesan == "b":
        listnama = "ES Kopi Coklat"
        harga = (12000 * jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga = int(harga - diskon + ppn)
        else:
            diskon = (0)
            totalharga = int(harga + ppn)
    elif pesan == "c":
        listnama = "Capuccino Panas"
        harga = int(11000 * jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        totalharga = int(harga + ppn)
    elif pesan == "c":
        listnama = "Ice Americano"
        harga = int(14000 * jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        totalharga = int(harga + ppn)
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan = input("Menu Tidak Tersedia Silahkan Kembali Dengan Menginputkan Y/N : ")

        print("+-------------------------------+")
        print("            KOPI KOPO\n"
              "Jln Sadang No.43 Margahayu Tengah")
        print("+-------------------------------+")
        print("Menu           : ", listnama)
        print("Jumlah Pesanan : ", jumlahpesan)
        print("Harga          : ", harga)
        print("Diskon         : ", diskon)
        print("PPN            : ", ppn)
        print("+-------------------------------+")
        print("Jumlah Bayar   : ", totalharga)
        print("+-------------------------------+")
        pilihan = input("Bila Ingin Pesan Kembali Input Y/N : ")
