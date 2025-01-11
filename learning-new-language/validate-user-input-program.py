# username < 12
# username not contain space
# username not contain digit

username = input("username: ")

if len(username) > 12:
    print("your username kelebihan 12 dan ada spasi")
elif not username.find(" ") == -1:
    print("your username ada spasi")
elif not username.isalpha():
    print("your username ada angka")
else:
    print(f"welcome {username}")