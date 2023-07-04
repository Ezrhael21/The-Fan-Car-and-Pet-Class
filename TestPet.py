# Ezrhael R. Sicat
# BSCpE 1-5
# 05/07/2023
# The Pet Class

import pyfiglet

font = pyfiglet.figlet_format("Test Pet Program", font = "slant", justify = "center")
print (font)

# Call the Pet Class
from Pet import Pet

# Ask user for pet details
user_pet_name = input("What is the name of your pet: ")
user_pet_type = input("What is the type of animal your pet is: ")
user_pet_age = int(input("What is the age of your pet: "))

# Set the pet details
pet = Pet(user_pet_name, user_pet_type, user_pet_age) 

# Display the output
print ("Pet Details:")
print ("Name: " + str(pet.get_name()))
print ("Type: " + str(pet.get_type()))
print ("Age: " + str(pet.get_age()))


