my_pizzas = ['cheese','chicken','supreme','sausage']
friends_pizzas = my_pizzas[:]
friends_pizzas.append('cheese crust')
print('My pizzas',my_pizzas)
print('Friends pizzas',friends_pizzas)
for fp in friends_pizzas:
    print(fp)