import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,2**3,3**3,4**3,5**3]
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(input_values,squares,linewidth=3) #Line width controls the thickness. 
ax.set_title("Cube Integers", fontsize=24) #Set's 
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Cube of value", fontsize=14)
ax.tick_params(labelsize=14)
plt.show()