# Create a class named Fan
class Fan:
    # Initialize the fan object
    def __init__(self, speed = 1, radius = 5, color = "blue", power = False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__power = power
    
    # Method to get the current speed of the fan 
    def get_speed (self):
        if self.__speed == 1:
            return "slow"
        elif self.__speed == 2:
            return "medium"
        elif self.__speed == 3:
            return "Fast"
        else:
            return "unknown"
    
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

    # Method to get the power of the fan
    def get_power (self):
        return self.__power

    # Method to set the power of the fan
    def set_power (self, power):
        self.__power == power
    
    

    
