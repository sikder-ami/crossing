import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('aqua')
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(player.up,'Up')
screen.onkey(player.down,'Down')

game_is_on = True
while game_is_on:
    car_manager.create_car()
    car_manager.move_cars()
    time.sleep(0.1)
    scoreboard.update()
    screen.update()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        player.goto(0,-280)
        car_manager.increase_speed()
        scoreboard.level += 1
        if car_manager.chance > 2:
            car_manager.chance-=1

screen.exitonclick()