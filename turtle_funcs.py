import math
import turtle


def find_side_mids(sideSize, turtleObject):

    # Function is used to find the middle coordinate
    # of each side of an equilateral triangle, given the
    # the length of the triangle's side and starting point
    # coordinates

    halfSide = sideSize / 2
    tri_height = sideSize / 2 * math.sqrt(3)

    bottomMiddle_x = turtleObject.pos()[0] + halfSide
    bottomMiddle_y = turtleObject.pos()[1]

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

    coords = {'left': {'x': leftMiddle_x, 'y': leftMiddle_y},
              'right': {'x': rightMiddle_x, 'y': rightMiddle_y},
              'bottom': {'x': bottomMiddle_x, 'y': bottomMiddle_y}}

    return coords


def draw_tri(sideSize, turtleObject):
    for i in range(3):
        turtleObject.forward(sideSize)
        turtleObject.right(120)


def draw_frac_comp(sideSize, startCoord):
    """
    This function draws a sub-component
    of a fractal. Think of a tri-force :).
    it will be used multiple times when drawing
    a full fractal.
    """

    newTurtle = turtle.Turtle()
    newTurtle.setposition(startCoord['x'], startCoord['y'])
    newTurtle.setheading(60)

    """
    Draw the first, larger triangle
    using the original values passed
    into the function
    """

    draw_tri(sideSize, newTurtle)

    """
    Find the middle position of each
    side of the previously drawn triangle,
    based on passed in information. Turtle
    object is passed in to get original
    coordinates and for future access.
    """
    sideMids = find_side_mids(sideSize, newTurtle)

    """
    Draw triangle half the size as
    the original in the same starting
    position. Turtle object is passed
    in to get original coordinates and
    for future access.
    """
    draw_tri(sideSize / 2, newTurtle)

    """
    Move turtle position to the middle
    coordinate of the left side of the
    original triangle drawn.
    """
    newTurtle.pen(pendown=False)
    newTurtle.setposition(round(sideMids['left':['x']], 2),
                          round(sideMids['left':['y']], 2))
    newTurtle.pen(pendown=True)

    """
    Draw triangle half the size as
    the original in the new position.
    (middle of left side)
    """
    draw_tri(sideSize / 2, newTurtle)

    """
    Move turtle position to the middle
    coordinate of the bottom side of the
    original triangle drawn.
    """
    newTurtle.pen(pendown=False)
    newTurtle.setposition(sideMids['bottom':[0]], sideMids['bottom':[1]])
    newTurtle.pen(pendown=True)

    """
    Draw triangle half the size as
    the original in the new position.
    (middle of bottom side)
    """
    draw_tri(sideSize / 2, newTurtle)

    """
    Set turtle to original starting position
    """
    newTurtle.position(startCoord['x'], startCoord['y'])
