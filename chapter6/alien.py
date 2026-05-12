alien_0 = {'color':'green','points':5}
alien_O = {'color':'green'}
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']# We assign points to variable.
print(f"You just earned {new_points} points!")
alien_0['x_position'] = 0 # adding new key value pairs to a dictionary
alien_0['y_position'] = 25
print(alien_0)
print(alien_O)
print(f"The alien is {alien_O['color']}.")
alien_O['color'] = 'yellow'
print(f"The alien is now {alien_O['color']}.")
print(alien_O)

alien_p = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_p['x_position']}")
if alien_p['speed'] == 'slow':
    x_increment = 1
elif alien_p['speed'] == 'medium':
    x_increment = 2
else: 
    # This alien must be booking it
    x_increment = 3 

alien_p['x_position'] = alien_p['x_position'] + x_increment

print(f"New position: {alien_p['x_position']}")
# We can delete things as well like del alien_o['points]
