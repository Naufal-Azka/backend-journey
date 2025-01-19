# function =  a block of code which only runs when it is called

def happy_birhday(name, age):
    print(f"Happy Birthday to {name}")
    print(f"You are {age} years old")
    print(f"Happy Birthday to you\n")

happy_birhday('nopal', 20)
happy_birhday('eaaa', 30)
happy_birhday('ahahe', 40)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your invoice amount is ${amount:.2f}")
    print(f"Please pay before {due_date}\n")

display_invoice('nopal', 1000, '2021-12-31')


# return statement
def add(x, y):
    z = x + y
    return z

def substract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(10, 20))
print()


def create_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return first_name + ' ' + last_name

full_name = create_name('nopal', 'arifin')
print(full_name)