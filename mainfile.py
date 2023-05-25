from rocket import RocketBoard, Rocket

board = RocketBoard(3)

board[0].x = 12

# print(board[0].speed)

rocket1 = Rocket(speed=2, altitude=3, x=4)
rocket2 = Rocket(speed=3, altitude=2, x=5)

print(RocketBoard.get_distance(rocket1, rocket2))

print(board.get_amount_of_rockets())
