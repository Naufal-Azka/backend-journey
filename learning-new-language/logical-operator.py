# Logical operators = kayak operator || sama &&
# ada (or/and/not)
# NOT = kebalikan misalnya boolean TRUE tapi ada NOT jadi FALSE

# OR
temp = 28
is_raining = False
is_sunny = False

if temp > 35 or temp < 0 or is_raining:
    print("outdoor event cancelled")
else:
    print("outdoor event scheduled")



# AND sama NOT
if temp >= 28 and is_sunny:
    print("PANASS")
elif temp <= 0 and is_sunny:
    print("DINGIN tetapi tidak kejam")
elif temp < 28 and temp > 0 and is_sunny:
    print("Hangat")
elif temp >= 28 and not is_sunny:
    print("awan")
elif temp <= 0 and not is_sunny:
    print("hujan")
elif temp < 28 and temp > 0 and not is_sunny:
    print("mendung")
