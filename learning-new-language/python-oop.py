class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    def drive(self):
        print(f"You drive the {self.model}")
    def stop(self):
        print(f"You stop the {self.model}")
    def description(self):
        print(f"The car is a {self.color} {self.year} {self.model}.")

car1 = Car("Toyota", 2019, "Red", True)
car2 = Car("Honda", 2018, "Blue", False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
car1.drive()
car1.stop()
car1.description()