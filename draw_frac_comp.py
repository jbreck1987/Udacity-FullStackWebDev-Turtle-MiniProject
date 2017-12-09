import turtle
import turtle_funcs as tf

side = 200
window = turtle.Screen()

startCoord = {'x': 0,
              'y': 0}
"""
Instantiate new turtle to pass
into functions that draw the shape
"""

newTurtle = turtle.Turtle()
newTurtle.setposition(startCoord['x'],
                      startCoord['y'])
newTurtle.setheading(60)

# Start drawing the full fractal

"""
Calculate the vertices of the first larger
triangle
"""

vertTri = tf.find_tri_verts(side, newTurtle)

tf.draw_frac_comp(side, newTurtle, startCoord)

newTurtle.pen(pendown=False)
newTurtle.setposition(vertTri['top']['x'],
                      vertTri['top']['y'])
startCoord = {'x': vertTri['top']['x'],
              'y': vertTri['top']['y']}
newTurtle.pen(pendown=True)

tf.draw_frac_comp(side, newTurtle, startCoord)

newTurtle.pen(pendown=False)
newTurtle.setposition(vertTri['right']['x'],
                      vertTri['right']['y'])
startCoord = {'x': vertTri['right']['x'],
              'y': vertTri['right']['y']}
newTurtle.pen(pendown=True)

tf.draw_frac_comp(side, newTurtle, startCoord)

newTurtle.setposition(0, 0)

window.exitonclick()
