# Ezrhael R. Sicat
# BSCpE 1-5
# 03/07/2023
# The Fan Class

import pyfiglet
import colorama

print (colorama.Fore.GREEN + "=" * 100)
font = pyfiglet.figlet_format("TV Test Program", font = "slant", justify = "center")
print (colorama.Fore.YELLOW + font)
print (colorama.Fore.GREEN + "=" * 100)

# Call the Fan Class
from Fan import Fan

# Create two seperate instances of the Fan Class
fan_one = Fan()
fan_two = Fan()

# Ask the user for Fan1 Details
user_speed_one = int(input(colorama.Fore.BLUE + "Enter the speed of Fan 1: (1=Slow, 2=Medium, 3=Fast) "))
user_radius_one = float(input("Enter the radius of Fan 1: "))
user_color_one = str(input("Enter the color of Fan 1: "))
user_power_one = input("Is Fan 1 on/off: (True=On|False=Off) ").lower()

# Set Fan1 Details 
fan_one.set_speed(user_speed_one)
fan_one.set_radius(user_radius_one)
fan_one.set_color(user_color_one)

# Set the Power for Fan 1
if user_power_one == "true":
    fan_one.set_power(True)
elif user_power_one == "false":
    fan_one.set_power(False)
else:
    print(colorama.Fore.WHITE + "Invalid input. Setting default power (False).")
    fan_one.set_power(False)

# Ask the user for Fan2 Details
print (colorama.Fore.GREEN + "=" * 100)
user_speed_two = int(input(colorama.Fore.BLUE + "Enter the speed of Fan 2: (1=Slow, 2=Medium, 3=Fast) "))
user_radius_two = float(input("Enter the radius of Fan 2: "))
user_color_two = str(input("Enter the color of Fan 2: "))
user_power_two = input("Is Fan 2 on/off: (True=On|False=Off) ").lower()

# Set Fan2 Details 
fan_two.set_speed(user_speed_two)
fan_two.set_radius(user_radius_two)
fan_two.set_color(user_color_two)

# Set the Power for Fan 2
if user_power_two == "true":
    fan_two.set_power(True)
elif user_power_one == "false":
    fan_two.set_power(False)
else:
    print("Invalid input. Setting default power (False).")
    fan_two.set_power(False)

# Time Delay
print (colorama.Fore.GREEN + "=" * 100)
print (colorama.Fore.WHITE + "Processing...")
import time
time.sleep(5)

# Display the Output
print (colorama.Fore.GREEN + "=" * 100) 
print (colorama.Fore.WHITE + "Fan 1 Details:")
print ("Speed: " + str(fan_one.get_speed()))
print ("Radius: " + str(fan_one.get_radius()))
print ("Color: " + str(fan_one.get_color()))
print ("Power: " + str(fan_one.get_power()))

print (colorama.Fore.GREEN + "=" * 100)
print (colorama.Fore.WHITE + "Fan 2 Details:")
print ("Speed: " + str(fan_two.get_speed()))
print ("Radius: " + str(fan_two.get_radius()))
print ("Color: " + str(fan_two.get_color()))
print ("Power: " + str(fan_two.get_power()))
print (colorama.Fore.GREEN + "=" * 100)


