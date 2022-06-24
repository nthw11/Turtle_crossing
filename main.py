import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("not_Frogger")
screen.tracer(0)

player = Player()
car_manager = CarManager()
screen.listen()
screen.onkey(player.move, "Up")
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.spawn_car()
    car_manager.drive_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()


    if player.ycor() > 280:
        score.level += 1
        score.update_level()
        car_manager.speed_up()

        player.start()

screen.exitonclick()
