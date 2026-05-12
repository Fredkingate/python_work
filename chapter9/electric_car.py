class Car:
    "A attempt to represent a car."
    def __init__(self,make,model,year,odometer_reading):
        "Initialize attributes to describe a car."
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading
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
class ElectricCar(Car):
    "Represent aspects of a car, specific to electric vehicles."
    def __init__(self, make, model, year, odometer_reading):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year, odometer_reading)
    def describe_battery(self):
        "Print a statement describing the battery size."
        battery_size = 40
        print("This car has a 40-kWh battery.")
        if battery_size == 40:
            range = 150
        elif battery_size == 60:
            range = 225
        print(f"This car can go approximately {range} miles on a full charge.")
my_leaf = ElectricCar('nissan', 'leaf', 2020, 15000)
print(my_leaf.get_descriptive_name())
my_leaf.read_odometer()
my_leaf.update_odometer(16000)
my_leaf.describe_battery()