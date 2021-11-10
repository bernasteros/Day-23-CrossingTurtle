import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

HEIGHT = 600
WIDTH = 600

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Turtle Crossing")

froggy = Player()


game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
