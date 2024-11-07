import turtle
from turtle import Turtle,Screen
import random

tim=Turtle()
tim.shape("arrow")


tim.colormode(255)

direction=[0, 90, 180, 270]


def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color(r, g, b)



for _ in range(200):
    tim.forward(30)
    tim.setheading(random.choice(direction))
    tim.color(random_color())
    tim.pensize(15)
    tim.speed(0)


screen=Screen()
screen.exitonclick()