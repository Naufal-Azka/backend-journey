weight = float(input("berat? "))
unit = input("k atau p")

if unit == "k":
    weight *= 2.205
    unit = "kgs"

    print(f"beratnya adalah {round(weight, 2)}{unit}")
elif unit == "p":
    weight /= 2.205
    unit = "lbs"

    print(f"beratnya adalah {round(weight, 2)}{unit}")
else:
    print(f"{unit} tidak ada")

