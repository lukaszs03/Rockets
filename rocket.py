from random import randint
from math import sqrt


class Rocket:

    def __init__(self, speed=1, altitude=0, x=0):
        self.altitude = altitude

        self.speed = speed

        self.x = x

    def move_up(self):
        self.altitude += self.speed

    def __str__(self):
        return "Rocket is on height: " + str(self.altitude)


class RocketBoard:

    def __init__(self, amountOfRockets=5):
        self.rockets = [Rocket(randint(1, 6)) for _ in range(amountOfRockets)]

        for _ in range(10):
            rocketIndexToMove = randint(0, len(self.rockets) - 1)
            self.rockets[rocketIndexToMove].move_up()

        for rocket in self.rockets:
            print(rocket)

    def __getitem__(self, key):
        return self.rockets[key]

    def __setitem__(self, key, value):
        self.rockets[key].altitude = value

    @staticmethod
    def get_distance(obj1: Rocket, obj2: Rocket) -> float:
        """Get distance of rockets on the board

        Args:
            obj1 (Rocket): picked rocket on the board
            obj2 (Rocket): -||-

        Returns:    
            float: result of the distance
        """
        ab = (obj1.altitude - obj2.altitude) ** 2
        bc = (obj1.x - obj2.x) ** 2
        return "The distance between the rockets is: " + str(sqrt(ab + bc))

    def get_amount_of_rockets(self):
        """Getting amount of rockets on the board

        Returns:
            self: self.rockets in __init__
        """
        return len(self.rockets)
