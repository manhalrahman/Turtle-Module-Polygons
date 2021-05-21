from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
timmy.color("black") #Need not be there
my_screen = Screen()
# This code moves the turtle upwards a little bit as the shapes will grow downwards and may escape the screen
timmy.penup() #So the we don't see the turtle moving up to the top of the screen
timmy.goto(0, 290) #The canvas dimensions are 300 height, 400 width. Just lifts the turtle towards the top
timmy.pendown() #So that we can draw again

#Draws all the shape
def draw_shapes(start=3, end=10, sidelength=100): 
    my_screen.colormode(255)
    #All the polygons will have number of sides in the range [start, end]
    for sides in range(start, end+1):
        timmy.color(randint(0, 255), randint(0, 255), randint(0, 255)) #A random color for each movement
        for i in range(sides):
            angle = 360 / sides 
            timmy.forward(sidelength)
            timmy.right(angle)


draw_shapes(3, 30, 50)
my_screen.exitonclick() #Click on the screen to close it. Will work after all the shapes are drawn.
