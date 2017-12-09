import turtle
from turtle_funcs import draw_frac_comp


window = turtle.Screen()
startCoord = {'x': 0,
              'y': 0}

draw_frac_comp(100, startCoord)

window.exitonclick()
