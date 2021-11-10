from turtle import Turtle

HEIGHT = 600
STARTING_POSITION = (0, -HEIGHT/2+20)
MOVE_DISTANCE = 10
FINISH_LINE_Y = HEIGHT-20
COLOR = "light green"
FACE_UP = 90


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.hideturtle()
        self.color(COLOR)
        self.penup()
        self.goto(STARTING_POSITION)
        self.showturtle()
        self.setheading(FACE_UP)

    def move(self):
        self.forward(MOVE_DISTANCE)
