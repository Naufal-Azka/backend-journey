nama = input("nama: ")
phone_num = input("num phone: ")

result = len(nama)
result = nama.find(" ") # ASCENT
result = nama.rfind(" ") # DESCENT
result = nama.capitalize()
result = nama.upper() # UPPERCASE
result = nama.lower() # LOWERCASE
result = nama.isdigit() # return true / false jika angka doang
result = nama.isalpha() # return true / false jika huruf doang
result = phone_num.count("-")
result = phone_num.replace("-", "")

print(result)
print(help(str))
