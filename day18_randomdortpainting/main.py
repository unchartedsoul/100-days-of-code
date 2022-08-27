# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("projectimage.jpg",30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")
color_list = [(50, 25, 7), (49, 14, 39), (133, 89, 42), (221, 155, 73), (36, 26, 69), (80, 80, 25), (238, 61, 43), (66, 34, 118), (240, 113, 171), (238, 213, 97), (144, 28, 18), (19, 40, 29), (243, 239, 188), (147, 147, 66), (69, 98, 129), (211, 84, 126), (147, 63, 90), (96, 184, 204), (109, 33, 63), (68, 109, 97), (102, 235, 246), (251, 148, 207), (199, 248, 243), (70, 156, 167), (179, 236, 249), (117, 179, 167), (114, 240, 233), (252, 197, 237), (82, 153, 142), (41, 77, 65)]
tim.setheading(225)
tim.forward(225)
tim.setheading(0)
number_of_dots = 100



for x in range(1,number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if x % 10 == 0 :
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = t.Screen()
screen.exitonclick()
