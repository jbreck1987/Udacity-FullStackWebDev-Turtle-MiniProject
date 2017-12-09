import turtle
from sys import path
from turtle_funcs import find_side_mids

newguy = turtle.Turtle()
position = newguy.pos()
#  print(position[0] + 1)
#  print(position[1] + 1)


mids = find_side_mids(100, newguy)
print(mids)
# print(turtle.position)
# print(path)
