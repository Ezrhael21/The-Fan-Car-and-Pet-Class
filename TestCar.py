# Ezrhael R. Sicat
# BSCpE 1-5
# 03/07/2023
# The Car Class

import pyfiglet
import colorama

print (colorama.Fore.GREEN + "=" * 100)
font = pyfiglet.figlet_format("Test Car Program", font = "slant", justify = "center")
print (colorama.Fore.YELLOW + font)
print (colorama.Fore.GREEN + "=" * 100)

# Call the Car Class
from Car import Car

# Ask User for Car Details
user_car_model = str(input(colorama.Fore.BLUE + "What is the Year Model of your car: "))
user_car_make = str(input("What is the Make of your Car: "))
print (colorama.Fore.GREEN + "=" * 100)

car = Car(user_car_model, user_car_make)

# Time Delay
print (colorama.Fore.YELLOW + "Car Accelerate")
print (colorama.Fore.WHITE + "Processing...")
print (colorama.Fore.GREEN + "=" * 100)
import time
time.sleep(5)

# Call the Method Accelerate five times
for _ in range(5):
    car.accelerate()
    # Display the Output for Car Speed
    print (colorama.Fore.WHITE + str(car.get_speed()) + " kph")
print (colorama.Fore.GREEN + "=" * 100)

# Time Delay
print (colorama.Fore.YELLOW + "Car Brake")
print (colorama.Fore.WHITE + "Processing...")
print (colorama.Fore.GREEN + "=" * 100)
import time
time.sleep(5)

# Call the Method Brake five times
for _ in range(5):
    car.brake()
    # Display the Output for Car Speed
    print (colorama.Fore.WHITE + str(car.get_speed()) + " kph")
print (colorama.Fore.GREEN + "=" * 100)
    
    
