class Dog:
    "A simple attempt to model a dog."

    def __init__(self,name,age):
        "Initialize name and the age attrributes."
        self.name = name
        self.age = age

    def sit(self):
        "Simulate a dog sitting in response to a given command."
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        "Simulate rolling over in response to a given command."
        print(f"{self.name.title()} rolled over!")
my_dog = Dog('willie', 6)
print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old.")
print(my_dog.sit())
print(my_dog.roll_over())