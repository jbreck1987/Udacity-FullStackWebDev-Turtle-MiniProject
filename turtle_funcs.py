import math


def find_side_mids(sideSize, turtleObject):
    """
    Function is used to find the middle coordinate
    of each side of an equilateral triangle,
    given the length of the triangle's side
    and the starting position attribute from
    the passed in turtle object.
    """

    halfSide = sideSize / 2
    tri_height = sideSize / 2 * math.sqrt(3)

    bottomMiddle_x = turtleObject.pos()[0] + halfSide
    bottomMiddle_y = turtleObject.pos()[1]

    leftMiddle_x = bottomMiddle_x - halfSide / 2
    leftMiddle_y = bottomMiddle_y + tri_height / 2

    rightMiddle_x = leftMiddle_x + halfSide
    rightMiddle_y = leftMiddle_y

    # Return a dict of dicts.
    # Each index of the dict
    # denotes the side in question.
    # Index 'x' in each sub-dict contains the
    # X-axis of the coordinate. Index 'y'
    # in each subdict contains the Y-axis of
    # the coordinate.

    return {'left': {'x': leftMiddle_x, 'y': leftMiddle_y},
            'right': {'x': rightMiddle_x, 'y': rightMiddle_y},
            'bottom': {'x': bottomMiddle_x, 'y': bottomMiddle_y}}


def find_tri_verts(sideSize, turtleObject):
    """
    Function is used to find the coordinates
    of the vertices of an equilateral triangle,
    based on the postion of the turtle
    object that is passed in and the length
    of the side of the triangle that is passed
    in.
    """

    halfSide = sideSize / 2
    tri_height = sideSize / 2 * math.sqrt(3)

    leftVert_x = turtleObject.pos()[0]
    leftVert_y = turtleObject.pos()[1]

    rightVert_x = turtleObject.pos()[0] + sideSize
    rightVert_y = turtleObject.pos()[1]

    topVert_x = turtleObject.pos()[0] + halfSide
    topVert_y = turtleObject.pos()[1] + tri_height

    # Return a dict of dicts.
    # Each index of the dict
    # denotes the vertice in question.
    # Index 'x' in each sub-dict contains the
    # X-axis of the coordinate. Index 'y'
    # in each subdict contains the Y-axis of
    # the coordinate.

    return {'left': {'x': leftVert_x, 'y': leftVert_y},
            'right': {'x': rightVert_x, 'y': rightVert_y},
            'top': {'x': topVert_x, 'y': topVert_y}}


def draw_tri(sideSize, turtleObject):
    """
    This function is used to draw an
    equilateral triangle of arbitary
    size, with the starting postion
    based on the position of the turtle
    object passed in.
    """
    for i in range(3):
        turtleObject.forward(sideSize)
        turtleObject.right(120)


def draw_frac_comp(sideSize, turtleObject, startCoord):
    """
    This function draws a sub-component
    of a fractal triangle. Think of a tri-force :).
    It will be used multiple times when drawing
    a full fractal triangle.
    """

    """
    Draw the first, larger triangle
    using the original values passed
    into the function
    """
    draw_tri(sideSize, turtleObject)

    """
    Find the middle position of each
    side of the previously drawn triangle,
    based on passed in information. Turtle
    object is passed in to get original
    coordinates and for future access.
    """
    sideMids = find_side_mids(sideSize, turtleObject)

    """
    Draw triangle half the size as
    the original in the same starting
    position. Turtle object is passed
    in to get original coordinates and
    for future access.
    """
    draw_tri(sideSize / 2, turtleObject)

    """
    Move turtle position to the middle
    coordinate of the left side of the
    original triangle drawn.
    """
    turtleObject.pen(pendown=False)
    turtleObject.setposition(sideMids['left']['x'],
                             sideMids['left']['y'])
    turtleObject.pen(pendown=True)

    """
    Draw triangle half the size as
    the original in the new position.
    (middle of left side)
    """
    draw_tri(sideSize / 2, turtleObject)

    """
    Move turtle position to the middle
    coordinate of the bottom side of the
    original triangle drawn.
    """
    turtleObject.pen(pendown=False)
    turtleObject.setposition(sideMids['bottom']['x'],
                             sideMids['bottom']['y'])
    turtleObject.pen(pendown=True)

    """
    Draw triangle half the size as
    the original in the new position.
    (middle of bottom side)
    """
    draw_tri(sideSize / 2, turtleObject)

    """
    Set turtle to it's original starting position
    """
    turtleObject.setposition(startCoord['x'],
                             startCoord['y'])
