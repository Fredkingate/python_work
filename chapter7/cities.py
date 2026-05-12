prompt = "\nPlease enter the name of a city you have visited"
prompt += "\n(Enter quit when you are finished)"
cities = []

while True:
    city = input(prompt)
    if city == 'quit':
        break 
    else:
        cities.append(city)
        print(f"I'd love to go to {city.title}!")

for city in cities:
    print(city)