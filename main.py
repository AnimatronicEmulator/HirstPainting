# Create a painting with 10 x 10 rows of dots, each 20px in size
# and spaced 50px apart. Each dot should be a random color chosen
# from the color-picked Hirst painting (I chose "Veil of Love Everlasting," 2017)

import colorgram
import random
import turtle as t


def colorgram_converter(list_of_colors):
    color_tuples = []
    for color in list_of_colors:
        color_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
        color_tuples.append(color_tuple)
    return color_tuples


def random_color_picker(list_of_rgb_colors):
    random_color = random.choice(list_of_rgb_colors)
    return random_color


def turn_around_next_row(row_num):
    if row_num != 0 and row_num % 2 == 0:
        hirst.right(90)
        hirst.penup()
        hirst.forward(50)
        hirst.right(90)
    elif row_num != 0 and row_num % 2 != 0:
        hirst.left(90)
        hirst.penup()
        hirst.forward(50)
        hirst.left(90)


def dot_maker(row_num):
    if row_num % 2 == 0:
        hirst.penup()
        hirst.forward(50)
        hirst.pendown()
        hirst.forward(0)
    else:
        hirst.pendown()
        hirst.forward(0)
        hirst.penup()
        hirst.forward(50)


colors = colorgram.extract("hirst.jpg", 50)
rgb_colors = colorgram_converter(colors)
rgb_colors.pop(0)

hirst = t.Turtle()
screen = t.Screen()

screen.screensize(500, 500)
screen.colormode(255)
hirst.pensize(20)
hirst.hideturtle()
hirst.penup()
hirst.goto(-275, -237.5)

for row in range(10):
    turn_around_next_row(row)
    for dot in range(10):
        hirst.pencolor(random_color_picker(rgb_colors))
        dot_maker(row)

screen.exitonclick()
