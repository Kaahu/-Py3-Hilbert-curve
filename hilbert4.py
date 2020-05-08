from turtle import Turtle, Screen
import sys

#______GLOBAL VARIABLES______

t = Turtle()
screen = Screen()

# Recording the screen size for reference when scaling the contents of the screen.
WIDTH = screen.window_width()
HEIGHT = screen.window_height()

# Setting the world coordinates for easy calculations.
screen.setworldcoordinates(-1,-1,1,1)

rightside = 1
topside = 1


#______LINE SCALING CALCULATIONS______

# Line size is determined by the order of the curve. The order of the curve is defined
# by an argument on execution.
try:
    ORDER = int(sys.argv[1].strip())
except ValueError:
    print("The order argument must be a valid integer.")
    sys.exit()

# Honesty is important. 
if ORDER > 9:
    print("Heads up- this might take a minute to draw.")

# The resolution of the grid increases exponentially with the order of the
# curve.
line_scaling_factor = (2**ORDER)-1

# The full width/height of the canvas is 2, 1.9 gives a border of 0.1.
linelength = (1.9 / line_scaling_factor)

# Ensure the curve is drawn an equal distance from the top/bottom/sides of the canvas
startx = rightside - (0.05)
starty = topside - (0.05)

#______WINDOW SCALING FUNCTION______

# A function to scale the contents of the window appropriately is the window is resized.
# Periodically checks if the window height or width has changed and, if it has, updates
# and re-draws.

def keepscale():

    global screen, WIDTH, HEIGHT
    
    if WIDTH != screen.window_width():
        screen.setworldcoordinates(-1,-1,1,1)
        screen.update()
        WIDTH = screen.window_width()

    if HEIGHT != screen.window_height():
        screen.setworldcoordinates(-1,-1,1,1)
        screen.update()
        HEIGHT = screen.window_height()

    # Timer to call the method every 200 milliseconds.
    screen.ontimer(keepscale,200)
    

#______TURTLE CONTROL FUNCTIONS______

# Encapsulating the basic turtle movements for easier writing and readability

def right():
    global t
    t.rt(90)

def left():
    global t
    t.lt(90)

def forward():
    global t
    t.fd(linelength)

#______CURVE DRAWING RULES______

# ruleA and ruleB are tightly coupled functions which call eachother (and themselves)
# recursively. These methods are adapted from the Hilbert Curve representation as an
# L-system, as explained on https://en.wikipedia.org/wiki/Hilbert_curve (accessed
# Jan 30th 2020)
#
# This can be read as two sets of production rules:
# A → − B F + A F A + F B −
# B → + A F − B F B − F A +

def ruleA(order, line):
    
    global t

    if order != 0:
        left()
        ruleB(order-1, line)
        forward()
        right()
        ruleA(order-1, line)
        forward()
        ruleA(order-1, line)
        right()
        forward()
        ruleB(order-1, line)
        left()
    else:
        return

def ruleB(order, line):

    global t, WIDTH
    
    if order != 0:
        right()
        ruleA(order-1, line)
        forward()
        left()
        ruleB(order-1, line)
        forward()
        ruleB(order-1, line)
        left()
        forward()
        ruleA(order-1, line)
        right()
    else:
        return

#______DRAWING SETTINGS______

# Hide the turtle drawing cursor (sorry turtle). 
t.hideturtle()

# Draw as fast as a turtle can.
t.speed(0)


# Only display 1 in every 1000 screen updates. This means that it often misses the final
# drawing f the curve, which is why screen.update() is called at the end of the main loop.
screen.tracer(1000,1)

#______EXECUTION______

# Run the keepscale() function which periodically checks the screen dimensions and scales
# appropriately.
keepscale()

# Start off with the turtle facing left.
t.seth(180)
t.pu()

# Move turtle to start position.
t.goto(startx,starty)

# Place pen down, prepare for drawing.
t.pd()

# Execute rule A, drawing a Hilbert curve of the given order
ruleA(ORDER, linelength)

# Update the screen- this is in case the final drawing of the curve is skipped by the screen
# tracer settings
screen.update()

# Loop to cycle through functions
screen.mainloop()
