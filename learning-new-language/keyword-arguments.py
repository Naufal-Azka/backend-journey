# keyword arguments = arguments preceded by an identifier when we pass them to a function

def hello(greeting, title, first_name, last_name):
    print(f"{greeting}, {title} {first_name} {last_name}")

hello(greeting="Hello", title="Mr.", first_name="John", last_name="Doe")


# sep = separator
print('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', sep=' - ')


# phone number
def get_phone(country, area, first, last):
    return f"+{country}-{area}-{first}-{last}"

phone_num = get_phone(country="1", area="212", first="1243", last="5325")
print(phone_num)