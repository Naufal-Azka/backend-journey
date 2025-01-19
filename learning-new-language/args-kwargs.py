# *args = allows you to pass a variable number of arguments to a function
# **kwargs = allows you to handle named arguments that you have not defined in advance

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 9)) # returns 3


# display_name = takes in multiple names and displays them
def display_name(*names):
    for name in names:
        print(name, end=' ')

print(display_name("John", "Jane", "Doe")) # returns John Jane Doe None


# **kwargs prints the address
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Main Street", city="New York", state="NY", zip="10001")


# exercise
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=' ')
    print()

    if 'apt' in kwargs:
        print(f'Street: {kwargs["street"]} {kwargs["apt"]}')
    elif 'pobox' in kwargs:
        print(f'Street: {kwargs["street"]} {kwargs["pobox"]}')
    else:
        print(f'Street: {kwargs["street"]}')

    print(f'City: {kwargs["city"]} {kwargs["state"]} {kwargs["zip"]}')

shipping_label("John Doe", "James",
               street="123 Main Street", 
               city="New York", 
               state="NY", 
               zip="10001", 
               country="USA")