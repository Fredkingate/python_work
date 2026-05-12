cars = ['bmw','audi','toyota','subrau'] 
sorted_cars = []
reversed_cars = []
print(cars)
cars.reverse()
print(cars)
#sorted_cars = sorted(cars)
print(cars)
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
