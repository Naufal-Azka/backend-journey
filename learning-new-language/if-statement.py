# kalo int
age = int(input("umur? "))

if age >= 18:
    print("lolos.")
elif age < 0:
    print("belum regis njir")
else:
    print("nggak.")


# kalo string
respon = input("mau makanan (y/n): ")

if respon == "y":
    print("buat loe")
else:
    print("y.")


# kondisi spesial
nama = input("namamu: ")

if nama == "":
    print("kosong")
else:
    print(nama)


# boolean
online = True

if online:
    print("online")
else:
    print("ofline")