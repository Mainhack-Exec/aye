import os

print("Welcome to Ftp Tools Hunter")
print("Silakan Pilih Menu:")
print("1. Ftp Hunter")
print("2. Split Ftp")
print("3. Cek Ftp")

def screen_clear():
    os.system('cls')
# Input pilihan pengguna
pilihan = input("Masukan Pilih dengan Angka 1, 2, atau 3: ")

# Cek input pengguna dan jalankan file yang sesuai
if pilihan == "1":
    os.system("python script/ftphunter.py")
elif pilihan == "2":
    os.system("python script/ftpsplit.py")
elif pilihan == "3":
    os.system("python script/checkftp.py")
else:
    print("Pilihan tidak valid. Silakan masukkan angka 1, 2, atau 3.")
