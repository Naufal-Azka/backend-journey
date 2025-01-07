# operasi matematika dasar
friends = 10

friends = friends + 1
friends += 1

friends = friends - 2
friends -= 2

friends = friends * 3
friends *= 3

friends = friends / 2
friends /= 2

friends = friends ** 2
friends **= 2

sisa = friends % 3


# arithmetics
phi = 3.14
x = 4
y = 5

result = round(phi)
result = abs(x)
result = pow(4, 3)
result = max(phi, x, y)
result = min(phi, x, y)


# Import lib untuk akar kuadrat, dll
import math

x = 9.9

print(math.pi)
print(math.e)
result = math.sqrt(x)
result = math.ceil(x)
result = math.floor(x)


# keliling lingkaran
# radius = float(input("panjang radius: "))
# keliling = 2 * math.pi * radius

# print(f"keliling lingkaran: {round(keliling, 2)}cm")


# Luas lingkaran
# radius = float(input("panjang radius: "))
# luas = math.pi * pow(radius, 2)

# print(f"luas lingkaran: {round(luas, 2)}cm^2")


# sisi miring segitiga
a = float(input("Panjang a: "))
b = float(input("Panjang b: "))
c = round(math.sqrt(pow(a, 2) + pow(b, 2)), 2) 

print(f"panjang sisi miring: {c}")