import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)


def random_colour():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    t_tuple = (r, b, g)
    return t_tuple

directions = [0, 90, 180, 270]


timmy.speed("fastest")
def draw_spirograph(size_of_graph):
    for x in range(int(360/size_of_graph)):
        timmy.color(random_colour())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+size_of_graph)



draw_spirograph(5)







screen = t.Screen()
screen.exitonclick()