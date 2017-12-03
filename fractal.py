import turtle
import math


window = turtle.Screen()
startCoord = {'x': 0,
              'y': 0}


def draw_tri(sideSize, startCoord):
    newTurtle = turtle.Turtle()
    newTurtle.setheading(60)
    newTurtle.setposition(startCoord['x'], startCoord['y'])

    for i in range(3):
        newTurtle.forward(sideSize)
        newTurtle.right(120)

    side_mids = find_side_mids(sideSize, startCoord)

    newTurtle.setposition(side_mids['left'][0],
                          side_mids['left'][1])
    newTurtle.dot()

    newTurtle.setposition(side_mids['right'][0],
                          side_mids['right'][1])
    newTurtle.dot()

    newTurtle.setposition(side_mids['bottom'][0],
                          side_mids['bottom'][1])
    newTurtle.dot()


def find_side_mids(sideSize, startCoord):

    # Function is used to find the middle coordinate
    # of each side of an equilateral triangle, given the
    # the length of the triangle's side and starting point
    # coordinates

    halfSide = sideSize / 2
    tri_height = sideSize / 2 * math.sqrt(3)

    bottomMiddle_x = startCoord['x'] + halfSide
    bottomMiddle_y = startCoord['y']

    leftMiddle_x = bottomMiddle_x - halfSide / 2
    leftMiddle_y = bottomMiddle_y + tri_height / 2

    rightMiddle_x = leftMiddle_x + halfSide
    rightMiddle_y = leftMiddle_y

    # Return a dict of lists.
    # Each index of the dict
    # denotes the side in question.
    # Index 0 in each sublist is the
    # X-axis of the coordinate. Index 1
    # in each sublist is the Y-axis of
    # the coordinate.

    return {'left': [leftMiddle_x, leftMiddle_y],
            'right': [rightMiddle_x, rightMiddle_y],
            'bottom': [bottomMiddle_x, bottomMiddle_y]}


draw_tri(600, startCoord)


window.exitonclick()
