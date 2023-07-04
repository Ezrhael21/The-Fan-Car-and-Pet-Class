# Ezrhael R. Sicat
# BSCpE 1-5
# 05/07/2023
# The Pet Class

# Call the Pet Class
from Pet import Pet

pet = Pet() 

# Ask user for pet details
user_pet_name = input("What is the name of your pet: ")
user_pet_type = input("What is the type of animal your pet is: ")
user_pet_age = int(input("What is the age of your pet: "))

# Set the pet details
pet.set_name(user_pet_name)
pet.set_type(user_pet_type)
pet.set_age(user_pet_age)

# Display the output

