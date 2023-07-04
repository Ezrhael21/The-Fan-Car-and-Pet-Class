# Ezrhael R. Sicat
# BSCpE 1-5
# 03/07/2023
# The Car Class

# Call the Car Class
from Car import Car

# Ask User for Car Details
user_car_model = str(input("What is the Year Model of your car: "))
user_car_make = str(input("What is the make of your Car: "))

car = Car(user_car_model, user_car_make)

# Display the Output
