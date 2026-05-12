favorite_foods = ['pizza','falafel','carrot cake','cannoli','lasagna','ramen'
                  ,'blueberries','apples','eclairs','tacos']
message_one = "The first three items in the list are"
message_two = "The first three middle items in the list are"
message_three = "The last three items"
length_of_list=len(favorite_foods)
last_item = length_of_list - 3
middle_of_list = length_of_list/2
print(message_one,favorite_foods[0:3])
print(message_two,favorite_foods[int(middle_of_list):8])
print(message_three,favorite_foods[7:10]) # There's probably a more creative way
