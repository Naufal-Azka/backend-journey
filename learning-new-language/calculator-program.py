# Python calculator

operator = input("masukkan operator (+ - * /): ")
num1 = float(input("angka pertama: "))
num2 = float(input("angka kedua: "))

if operator == "+":
    result = round(num1 + num2, 2)
    print(result)
elif operator == "-":
    result = round(num1 - num2, 2)
    print(result)
elif operator == "*":
    result = round(num1 * num2, 2)
    print(result)
elif operator == "/":
    result = round(num1 / num2, 2)
    print(result)
else:
    print(f"{operator} nggak ada woi")