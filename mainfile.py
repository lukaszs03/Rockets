from rocket import Rocket
from random import randint

rockets = [Rocket(randint(1, 6)) for _ in range(5)]

for _ in range(10):
    rocketIndexToMove = randint(0, len(rockets) - 1)
    rockets[rocketIndexToMove].move_up()


for rocket in rockets:
    print(rocket)
