unit = input("(c/f): ")
temp = float(input("enter temperature: "))

if unit == "c":
    temp = round((9 * temp) / 5 + 32, 2)
    print(f"{temp}°F")
elif unit == "f":
    temp = round((temp - 32) * 5 / 9, 2)
    print(f"{temp}°C")
else:
    print("unit nggak valid")