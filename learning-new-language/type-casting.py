# mengubah tipe data y.

nama = "nopal"
umur = 25
kkm = 3.2
is_student = True

# untuk mengambil tipe data
print(type(nama))

kkm = int(kkm)
print(kkm)

umur = float(umur)
print(umur)

age = str(umur)
age += "1"
print(age)

# kalo string nya isi walaupun hanya spasi = TRUE, kalo kosong = FALSE
nama = bool(nama)
print(nama)