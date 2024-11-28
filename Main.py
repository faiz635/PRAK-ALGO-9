# def write(jadi):
    
#     f = open("teks", "w")
    
#     f.write(jadi)
    
#     f.close()
    
# def main():
    
#     f = open("kepo.txt", "r")
#     if f.mode == "r":
#         contents = f.read()
#     print (contents)
    
# a = str(input("Nama: "))
# b = str(input("Umur: "))
# c = str(input("Alamat: "))
# d = str(input("Email: "))
# e = str(input("Dosen Wali: "))
# jadi = ("{}\n{}\n{}\n{}\n{}\n". format(a,b,c,d,e))

# print("\n")
# print("Loading. . . ")
# write(jadi)
# print("")
# main()

def buat_file(nama_file):
    open(nama_file, 'w').close()
    print(f"File '{nama_file}' dibuat.")

def baca_file(nama_file):
    with open(nama_file, 'r') as file:
        print(file.read())

def tambah_ke_file(nama_file, teks):
    with open(nama_file, 'a') as file:
        file.write(teks + '\n')
    print(f"Teks ditambahkan ke '{nama_file}'.")

while True:
    print("\n1. Membuat File\n2. Membaca File\n3. Menambahkan Teks\n4. Keluar")
    pilihan_ke= input("Pilih menu (1/2/3/4): ")
    
    if pilihan_ke == '1':
        buat_file(input("Nama file: "))
    elif pilihan_ke == '2':
        baca_file(input("Nama file: "))
    elif pilihan_ke == '3':
        tambah_ke_file(input("Nama file: "), input("Teks: "))
    elif pilihan_ke == '4':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak ada.")
