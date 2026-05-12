class Car:
    "A attempt to represent a car."

    def __init__(self,make,model,year):
        "Initialize attributes to describe a car."
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        "Return a neatly formatted descriptive name."
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        "Print a statement showing the car's mileage."
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self,mileage):
        "Set the odometer reading to the given value."
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading += miles
class Battery:
    "An attempt to model a battery for an electric car"
    
    def __init__(self,battery_size=40):
        "Initialize the battery's attribiutes"
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size} - kWh battery.")

    def get_range(self):
        "Print a statement about the range this battery provides"
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range}miles on a full charge.")
    
class ElectricCar(Car):
    """Models aspects ofa car, specific to electric vehicles"""

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()
my_new_car = Car('audi', 'a4', 2019)
my_second_car = Car('subaru', 'outback', 2020)
my_third_car = Car('toyota', 'camry', 2021)
print(my_new_car.get_descriptive_name())
print(my_second_car.get_descriptive_name())
print(my_third_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(25)
my_new_car.read_odometer()
