# list comprehension = [expression for item in iterable if condition == True]

# doubles = [x * 2 for x in range(1, 11)]
# triples = [x * 3 for x in range(1, 11)]
# print(doubles)
# print(triples)


# numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
# positive_numbers = [num for num in numbers if num > 0]
# negative_numbers = [num for num in numbers if num < 0]

# print(positive_numbers)
# print(negative_numbers)


# grades
grades = [88, 75, 96, 55, 83]
passed = [grade for grade in grades if grade >= 60]
failed = [grade for grade in grades if grade < 60]

print(passed)
print(failed)
