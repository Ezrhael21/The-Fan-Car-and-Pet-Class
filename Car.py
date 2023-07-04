# Create a class named Car
class Car:
    # Initialize the Car object
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    
    # Method to accelerate the current speed of the car
    def accelerate(self):
        self.__speed += 5

    # Method to brake the current speed of the car
    def brake(self):
        self.__speed -= 5
    
    # Method to get the current speed of the car
    def get_speed(self):
        return self.__speed
    

