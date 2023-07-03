# Create a class named Fan
class Fan:
    # Initialize the fan object
    def __init__(self, speed = 3, radius = 5, color = "blue", power = False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__power = power
    
    # Method to get the current speed of the fan 
    def get_speed (self):
        return self.__speed
    
    # Method to set the speed of the fan
    def set_speed (self, speed):
        self.__speed = speed

    # Method to get the radius of the fan 
    def get_radius (self):
        return self.__radius
    
    # Method to set the radius of the fan
    def set_radius (self, radius):
        self.__radius = radius

    # Method to get the color of the fan 
    def get_color (self):
        return self.__color
    
    # Method to set the color of the fan
    def set_color (self, color):
        self.__color = color

    # Method to turn on the fan
    def turn_on (self):
        self.__on = True
    
    # Method to turn off the fan
    def turn_off(self):
        self.__on = False
    
    

    
