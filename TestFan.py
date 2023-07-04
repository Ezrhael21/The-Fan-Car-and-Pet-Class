# Ezrhael R. Sicat
# BSCpE 1-5
# 03/07/2023
# The Fan Class

# Call the Fan Class
from Fan import Fan

# Create two seperate instances of the Fan Class
fan_one = Fan()
fan_two = Fan()

# Ask the user for Fan1 Details
user_speed_one = input("Enter the speed of the fan: ")
user_radius_one = input("Enter the radius of the fan: ")
user_color_one = input("Enter the color of the fan: ")
user_power_one = input("Is the fan on/off: ")

# Set Fan1 Details 
fan_one.set_speed(user_speed_one)
fan_one.set_radius(user_radius_one)
fan_one.set_color(user_color_one)

# Ask the user for Fan2 Details
user_speed_two = input("Enter the speed of the fan: ")
user_radius_two = input("Enter the radius of the fan: ")
user_color_two = input("Enter the color of the fan: ")
user_power_two = input("Is the fan on/off: ")

# Set Fan2 Details 
fan_two.set_speed(user_speed_two)
fan_two.set_radius(user_radius_two)
fan_two.set_color(user_color_two)

# Display the Output 
print ("Fan 1 Details:")
print ("Speed: " + str(fan_one.get_speed()))
print ("Radius: " + str(fan_one.get_radius()))
print ("Color: " + str(fan_one.get_color()))
print ("Power: " + str(fan_one.get_power()))

print ("Fan 1 Details:")
print ("Speed: " + str(fan_two.get_speed()))
print ("Radius: " + str(fan_two.get_radius()))
print ("Color: " + str(fan_two.get_color()))
print ("Power: " + str(fan_two.get_power()))


