class Restaurant:
    def __init__(self, restaurant_name, cuisine_type,number_served=0):
        #Attributes restaurant,cuisine,number served
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    def set_number_served(self, number_served):
        self.number_served = number_served
    def increment_number_served(self, additional_served):
        self.number_served += additional_served
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine. It has served {self.number_served} customers today.")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
restaurant = Restaurant('Pasta Palace', 'Italian') #The constructor
print(restaurant.restaurant_name)
restaurant.set_number_served(20)
print(restaurant.number_served)
restaurant1 = Restaurant('Sushi Central', 'Japanese')
restaurant1.set_number_served(30)
print(restaurant1.number_served)
print(restaurant1.restaurant_name)
restaurant2 = Restaurant('Taco Town', 'Mexican')
restaurant2.set_number_served(50)
print(restaurant2.number_served)
print(restaurant2.restaurant_name)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2.describe_restaurant()
restaurant2.open_restaurant()  