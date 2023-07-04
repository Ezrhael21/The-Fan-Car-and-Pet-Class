# Create a class named Pet
class Pet:
    # Initialize the pet object
    def __init__(self):
        self.__name = None
        self.__type = None
        self.__age = None
    
    # Method to set the name of the pet
    def set_name (self, name):
        self.__name = name
    
    # Method to set the type of animal the pet is
    def set_type (self, type):
        self.__type = type
    
    # Method to set the age of the pet
    def set_age (self, age):
        self.__age = age
    
    # Method to get the name of the pet
    def get_name (self):
        return self.__name
    
    # Method to get the type of animal the pet is
    def get_type (self):
        return self.__type
    
    # Method to get the age of the pet
    def get_age (self):
        return self.__age

    

    