class Rocket:

    def __init__(self, speed=1):
        self.altitude = 0

        self.speed = speed

    def move_up(self):
        self.altitude += self.speed

    def __str__(self):
        return "Rocket is on height: " + str(self.altitude) + ", and her speed is: " + str(self.speed)
