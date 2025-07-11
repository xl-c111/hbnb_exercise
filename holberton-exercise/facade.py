"""
Usage:
simplifying  the usage of a complex library or a set of classes.
providing a single entry point for a group of related functionality.  
"""


class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")


class Lights:
    def turn_on(self):
        print("Lights turned on")

    def turn_off(self):
        print("Lights turned off")


class CarFacade:
    # self is the only parameter of CarFacade class
    def __init__(self):
        """
        - self.engine, self.lights are instance attributes of the CarFacade object, they store instances of Engine and Lights class
          when you create a CarFacade object, such as car = CarFacade(), the __init__ will be automatically called
          self.engine equals to a instance of Engine class
          self.lights eqauls to a instance of Lights class

        - By doing this, CarFacade can use all these attributes to call their methods
        """
        # self.engine and self.lights are instance attributes of CarFacade class(typically defined in __init__, using self)
        self.engine = Engine()
        self.lights = Lights()

    def start_car(self):
        self.engine.start()
        self.lights.turn_on()
        print("Car is ready to go!")


class ParkingFacade:
    def __init__(self):
        self.engine = Engine()
        self.lights = Lights()

    def car_park(self):
        self.engine.stop()
        self.lights.turn_off()
        print("Car is parked and everything is off.")


# create a object of CarFacade class, __init__ initializes its internal engine and lights attributes
car = CarFacade()
# call start_car method on the car object
car.start_car()
print("---")
# create a object of ParkingFacade class, __init__ initializes its internal engine and lights attributes
parking = ParkingFacade()
parking.car_park()
