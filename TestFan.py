# Ezrhael R. Sicat
# BSCpE 1-5
# 03/07/2023
# The Fan Class

# Create two seperate instances of the Fan Class
fan_one = ()
fan_two = ()

# Ask the user for Fan1 Details
user_speed_one = input("Enter the speed of the fan: ")
user_radius_one = input(int("Enter the radius of the fan: "))
user_color_one = input(str("Enter the color of the fan: "))
user_power_one = input("Is the fan on/off: ")

# Set Fan1 Details 
fan_one.set_speed(user_speed_one)
fan_one.set_speed(user_radius_one)
fan_one.set_speed(user_color_one)
fan_one.set_speed(user_power_one)

# Ask the user for Fan2 Details
user_speed_two = input("Enter the speed of the fan: ")
user_radius_two = input(int("Enter the radius of the fan: "))
user_color_two = input(str("Enter the color of the fan: "))
user_power_two = input("Is the fan on/off: ")

# Set Fan2 Details 
fan_two.set_speed(user_speed_two)
fan_two.set_speed(user_radius_two)
fan_two.set_speed(user_color_two)
fan_two.set_speed(user_power_two)

# Call the methods in the main file
# Display the Output
print ("Fan 1 Details:\n Speed:\n" + str(fan_one.get_speed()) + "Radius:\n" + str(fan_one.get_radius()) + "Color:\n" + str(fan_one.get_color()) + "Power:\n" + fan_one.turn_on())


