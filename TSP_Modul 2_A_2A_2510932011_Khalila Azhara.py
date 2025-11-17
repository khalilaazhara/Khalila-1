input("Nama anda :")
NIM = input("Nim anda :")
input("Kelompok anda :")
input("Nama asisten pembimbing :")

ABC = int(NIM[6:9])
D = int(NIM[9:])
total_belanja = ABC * 1000

#harga diskon
silver = total_belanja * 5/100
gold = total_belanja * 10/100
platinum = total_belanja * 15/100

if 1<=D<=4:
    Harga_belanja = total_belanja - silver 
    member = "Silver"
    diskon = silver
     
elif 5<=D<=7:
    Harga_belanja = total_belanja - gold
    member = "Gold"
    diskon = gold
    
elif 8<=D<=9:
    Harga_belanja = total_belanja - platinum
    member = "platinum"
    diskon = platinum
    
else:
    member = "non membership"
    diskon = "Tidak Ada Diskon"

print("pilih metode pembayaran")
print("A = Tunai")
print("B = Qris")
print("C = Debit")

Tunai = Harga_belanja
Qris = Harga_belanja + 2500
Debit = Harga_belanja + 5000

Metod = input("Metode Pembayaran :")
if Metod == "A":
   Total_akhir = Tunai
   Metodepembayaran = "Tunai"
elif Metod == "B":
    Total_akhir = Qris
    Metodepembayaran = "Qris"
elif Metod == "C":
    Total_akhir = Debit
    Metodepembayaran = "Debit"
else:
    Print("Metode Pembayaran Tidak Valid")

print("Jenis Member :", member)
print("Harga Sebelum Diskon:", total_belanja)
print("Jumlah Diskon :", diskon)
print("Metode Pembayaran :",Metodepembayaran)
print("Harga Belanja:", Total_akhir)