class Student:
    # Class variable
    class_year = 2024
    number_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.number_students += 1

student1 = Student('John', 20)
student2 = Student('Jane', 21)
student3 = Student('Doe', 22)

print(student1.name)
print(student1.age)
print(Student.class_year)

print(Student.number_students)