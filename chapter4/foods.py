my_foods = ['pizaa','falafel','carrot cake']
friend_foods = my_foods[:] # How we copy a list
print("My favorite foods are")
print(my_foods)
print("My friends favorite foods are")
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
message_one = "My favorite foods are"
message_two = "My friends favotrite foods are"
print(message_one,my_foods)
print(message_two,friend_foods)
