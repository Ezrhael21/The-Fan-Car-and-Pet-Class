# Ezrhael R. Sicat
# BSCpE 1-5
# 05/07/2023
# The Pet Class

import pyfiglet
import colorama

print (colorama.Fore.GREEN + "=" * 100)
font = pyfiglet.figlet_format("Test Pet Program", font = "slant", justify = "center")
print (colorama.Fore.YELLOW + font)
print (colorama.Fore.GREEN + "=" * 100)

# Call the Pet Class
from Pet import Pet

pet = Pet()

# Ask user for pet details
user_pet_name = input(colorama.Fore.BLUE + "What is the name of your pet: ")
user_pet_type = input("What is the type of animal your pet is: ")
user_pet_age = int(input("What is the age of your pet: "))
print (colorama.Fore.GREEN + "=" * 100)

# Set the pet details
pet.set_name(user_pet_name)
pet.set_type(user_pet_type)
pet.set_age(user_pet_age)

# Display the output
print (colorama.Fore.YELLOW + "Pet Details:")
print (colorama.Fore.WHITE + "Name: " + str(pet.get_name()))
print ("Type: " + str(pet.get_type()))
print ("Age: " + str(pet.get_age()))
print (colorama.Fore.GREEN + "=" * 100)


