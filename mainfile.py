from rocket import RocketBoard, Rocket

board = RocketBoard(3)

board[0].x = 12

# print(board[0].speed)

rocket1 = Rocket(altitude=5)
rocket2 = Rocket()
print(RocketBoard.get_distance(rocket1, rocket2))
