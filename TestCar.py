# Ezrhael R. Sicat
# BSCpE 1-5
# 03/07/2023
# The Car Class

import pyfiglet

print ("=" * 100)
font = pyfiglet.figlet_format("Test Car Program", font = "slant", justify = "center")
print (font)
print ("=" * 100)

# Call the Car Class
from Car import Car

# Ask User for Car Details
user_car_model = str(input("What is the Year Model of your car: "))
user_car_make = str(input("What is the Make of your Car: "))
print ("=" * 100)

car = Car(user_car_model, user_car_make)

# Call the Method Accelerate five times
print ("Car Accelerate")
print ("=" * 100)
for _ in range(5):
    car.accelerate()
    # Display the Output for Car Speed
    print (str(car.get_speed()) + " kph")
print ("=" * 100)

# Call the Method Brake five times 
print ("Car Brake")
print ("=" * 100)
for _ in range(5):
    car.brake()
    # Display the Output for Car Speed
    print (str(car.get_speed()) + " kph")
print ("=" * 100)
    
    
