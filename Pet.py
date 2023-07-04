# Create a class named Pet
class Pet:
    # Initialize the pet object
    def __init__(self, name, type, age):
        self.__name = name
        self.__type = type
        self.__age = age
    
    # Method to set the name of the pet
    def set_name (self, name):
        self.__name = name
    
    # Method to set the type of animal the pet is
    def set_type (self, type):
        self.__type = type

    

    