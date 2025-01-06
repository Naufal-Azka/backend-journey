# input balikin data dalam bentuk string
nama = input("nama: ")
umur = int(input("umur: ")) + 1

print(f"halo {nama}!")
print("congratulations repeat year")
print(f"umur loe {umur}\n")


# hitung luas persegi panjang
panjang = float(input("Panjang Persegi Panjang: "))
lebar = float(input("Lebar Persegi Panjang: "))

print(f"Luas Persegi Panjang tersebut adalah {panjang * lebar}cm²\n")


# kasir njir
barang = input("nama barang: ")
harga = float(input("harga barang: "))
jumlah = int(input("jumlah barang: "))

print(f"anda membeli {jumlah} x {barang}")
print(f"dengan total: ${harga * jumlah}")