import random


class Insect:
    def __init__(self):  # could add (self,wings,legs)
        self.two_wings = 2  # if changed to above, two_wings must be set to wings
        self.four_legs = 4
        self.miles = 0

    def flight_time(self):
        self.miles = random.randint(0, 10)

    def flight_miles(self):
        return self.flight
