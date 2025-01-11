# {value:flags} formating value berdasarkan jenis

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

# jumlah desimal
print(f"price 1 is ${price1:.1f}")
print(f"price 2 is ${price2:.2f}")
print(f"price 3 is ${price3:.3f}")

print("\n")
# tambah spaci
print(f"price 1 is ${price1:010}")
print(f"price 2 is ${price2:<10}")
print(f"price 3 is ${price3:>10}")
print(f"price 3 is ${price3:^10}")

print("\n")

# positive value 
print(f"price 1 is {price1:+}")
print(f"price 2 is {price2:+}")
print(f"price 3 is {price3:+}")

print("\n")

# comma setiap ribuan bakal dikasih koma
print(f"price 1 is {price1:,}")
print(f"price 2 is {price2:,}")
print(f"price 3 is {price3:,}")

print("\n")

# bisa kombinasi
print(f"price 1 is {price1:+,.2f}")
print(f"price 2 is {price2:+,.2f}")
print(f"price 3 is {price3:+,.2f}")
