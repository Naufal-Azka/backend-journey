principle = 0
rate = 0
time= 0

while principle <= 0:
    principle = float(input("enter the principle amount: "))
    if principle <= 0:
        print("principle can't be less or zero")

while rate <= 0:
    rate = float(input("enter the interest rate: "))
    if rate <= 0:
        print("interest rate can't be less or zero")

while time <= 0:
    time = int(input("enter the time in years: "))
    if time <= 0:
        print("time can't be less or zero")

total = principle * pow((1 + rate / 100), time)
print(f"total balance ${total:.2f}")