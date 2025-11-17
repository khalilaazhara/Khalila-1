nama = input("Masukkan nama: ")
nim = input("Masukkan nim: ")
print(" ")
print("Pin anda adalah 4 digit terakhir nim.")

percobaan=0
kesempatan=3

pin_input = pin = int(nim[6:])

Login_berhasil = False

while percobaan < kesempatan:
    if pin_input == pin == int(input("Masukkan PIN anda: ")):
        Login_berhasil = True
        break
    else:
        percobaan+=1
        sisa_percobaan=kesempatan-percobaan
        if sisa_percobaan > 0:
              print("PIN anda salah, sisa percobaan anda tinggal", sisa_percobaan, "kali.")
        else:
             print("Batas percobaan sudah habis.")


if Login_berhasil:
     print(" ")
     print("Selamat datang di website nonton yuk")
     print(" ")

     while True:
        print("=== Pilihan Film ===")
        print("1. Horror : 10000")
        print("2. comedy: 11000")
        print("3. romance: 30000")
        print("4. sad: 14000")
        pilihan = input("Pilih Genre: ")
        if pilihan == "1":
            jumlahtiket = int(input("Jumlah tiket: "))
            Harga= jumlahtiket*10000
            print("total harga:", Harga,"rupiah")
        elif pilihan == "2":
            jumlahtiket = int(input("Jumlah tiket: "))
            Harga= jumlahtiket*11000
            print("total harga:", Harga,"rupiah")
        elif pilihan == "3":
            jumlahtiket = int(input("Jumlah tiket: "))
            Harga= jumlahtiket*30000
            print("total harga:", Harga,"rupiah")
        elif pilihan == "4":
            jumlahtiket = int(input("Jumlah tiket: "))
            Harga= jumlahtiket*14000
            print("total harga:", Harga,"rupiah")
        else:
            print("Pilihan tak tersedia, coba lagi.")
            continue
        lagi = input("Apakah anda ingin melakukan transaksi lagi? (ya/tidak): ").lower()
        if lagi == "ya":
            continue
        elif lagi == "tidak":
            print("Terima Kasih Sudah Melakukan Transaksi!")
        else:
            print("Pilihan Tidak Valid")
        break
    