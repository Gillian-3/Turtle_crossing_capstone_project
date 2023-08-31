import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board=Scoreboard()
screen.listen()
screen.onkey(fun=player.move, key="Up")
iteration = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    iteration += 1
    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with the car
    for car in car_manager.all_car:
        if car.distance(player)<20:
            score_board.game_over()
            game_is_on=False
    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.lever_up()
        score_board.increase_level()

screen.exitonclick()
