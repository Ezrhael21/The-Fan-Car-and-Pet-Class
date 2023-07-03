# Create a class named Fan
class Fan:
    # Initialize the fan object
    def __init__(self, speed = 3, radius = 5, color = "blue", power = False):
        self.speed = speed
        self.radius = radius
        self.color = color
        self.power = power
    
    # Method to get the current speed of the fan 
    def get_speed (self):
        return self.speed