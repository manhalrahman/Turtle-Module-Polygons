import random
from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
timmy.color("black")
my_screen = Screen()
my_screen.colormode(255)


def random_walk(no_of_steps=50, min_step=10, max_step=30, pen_width=5):
    global timmy
    timmy.width(pen_width)
    for _ in range(no_of_steps):
        colors = (randint(0, 255), randint(0, 255), randint(0, 255))
        timmy.pencolor(colors)
        timmy.color(colors)
        length_of_step = min_step + (max_step-min_step)*random.random()
        timmy.left(360 * random.random())
        choice = int(random.random() >= 0.5)
        if choice == 1:
            timmy.forward(length_of_step)
        else:
            timmy.backward(length_of_step)


random_walk()
my_screen.exitonclick()
