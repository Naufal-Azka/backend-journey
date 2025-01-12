# nama
nama = input("nama: ")

while nama == "":
    print("isi woi nama loe")
    nama = input("nama: ")
else:
    print(f"hello {nama}")


# umur
age = int(input("umur loe: "))

while age < 0:
    print("umur nggak boleh minus")
    age = int(input("umur loe: "))

print(f"loe {age} tahun")


# logical operator
food = input("makanan favorit")

while not food == "q":
    print(f"kamu suka {food}")
    food = input("makanan favorit")

print("bye")


# OR logical operator
num = int(input("masukkan angka diantara 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} not valid")
    num = int(input("masukkan angka diantara 1 - 10: "))

print(f"angka kamu adalah {num}")