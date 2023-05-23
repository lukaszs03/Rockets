from random import randint


class Rocket:

    def __init__(self, speed=1):
        self.altitude = 0

        self.speed = speed

    def move_up(self):
        self.altitude += self.speed

    def __str__(self):
        return "Rocket is on height: " + str(self.altitude) + ", and her speed is: " + str(self.speed)


class RocketBoard:

    def __init__(self, amountOfRockets=5):
        self.rockets = [Rocket(randint(1, 6)) for _ in range(amountOfRockets)]

        for _ in range(10):
            rocketIndexToMove = randint(0, len(self.rockets) - 1)
            self.rockets[rocketIndexToMove].move_up()

        for rocket in self.rockets:
            print(rocket)
