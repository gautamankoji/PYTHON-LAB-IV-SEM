""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:42:40 
"""

""" EXERCISE 08
    8.(a) Define classes and objects using python for the real-world scenario.
"""

class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.available = True

    def displayInfo(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: ₹{self.price}")

    def sell(self):
        if self.available:
            print(f"The {self.year} {self.make} {self.model} has been sold.")
            self.available = False
        else:
            print("Sorry, this car is already sold.")

class Customer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def buyCar(self, car):
        if car.available and car.price <= self.budget:
            print(f"{self.name} bought the {car.year} {car.make} {car.model}.")
            self.budget -= car.price
            car.sell()
        elif not car.available:
            print("Sorry, this car is already sold.")
        else:
            print(f"Sorry, {self.name} cannot afford the {car.year} {car.make} {car.model}.")

car1 = Car("Toyota", "Camry", 2020, 250000)
car2 = Car("Honda", "Civic", 2018, 200000)
customer1 = Customer("Akash", 300000)
customer2 = Customer("Bablu", 150000)
car1.displayInfo()
car2.displayInfo()
customer1.buyCar(car1)
customer2.buyCar(car1)
customer2.buyCar(car2)


""" --------------[OUTPUT]--------------------

Make: Toyota, Model: Camry, Year: 2020, Price: ₹250000
Make: Honda, Model: Civic, Year: 2018, Price: ₹200000
Akash bought the 2020 Toyota Camry.
The 2020 Toyota Camry has been sold.
Sorry, this car is already sold.
Sorry, Bablu cannot afford the 2018 Honda Civic.

--------------[END-OF-OUTPUT]-------------- """
