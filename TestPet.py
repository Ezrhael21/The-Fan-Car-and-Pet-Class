# Ezrhael R. Sicat
# BSCpE 1-5
# 05/07/2023
# The Pet Class

import pyfiglet

print ("=" * 100)
font = pyfiglet.figlet_format("Test Pet Program", font = "slant", justify = "center")
print (font)
print ("=" * 100)

# Call the Pet Class
from Pet import Pet

pet = Pet()

# Ask user for pet details
user_pet_name = input("What is the name of your pet: ")
user_pet_type = input("What is the type of animal your pet is: ")
user_pet_age = int(input("What is the age of your pet: "))
print ("=" * 100)

# Set the pet details
pet.set_name(user_pet_name)
pet.set_type(user_pet_type)
pet.set_age(user_pet_age)

# Display the output
print ("Pet Details:")
print ("=" * 100)
print ("Name: " + str(pet.get_name()))
print ("Type: " + str(pet.get_type()))
print ("Age: " + str(pet.get_age()))
print ("=" * 100)


