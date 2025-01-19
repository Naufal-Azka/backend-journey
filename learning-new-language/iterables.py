# iterables = list, tuple, dict, set, str, file objects, etc.

numbers = (1, 2, 3, 4, 5)

for number in reversed(numbers):
    print(number, end=' ')


# sorted(iterable, key=None, reverse=False)
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
for fruit in sorted(fruits):
    print(fruit, end=' ')


# enumerate(iterable, start=0)
name = 'Python'

for char in name:
    print(char, end=' ')


# zip(iterable1, iterable2, ...)
my_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
for key, value in my_dictionary.items():
    print(key, value)