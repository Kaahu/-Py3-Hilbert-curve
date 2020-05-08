Hilbert4.py

________HOW TO EXECUTE_________________________________________________________

Navigate to folder containing hilbert4.py and run using python3, followed by
the desired order of the curve. To draw a hilbert curve of order 3:

$ python3 hilbert4.py 3

The order argument must be an integer value or the program will exit and prompt
you to input a value integer.

________BACKGROUND_______________________________________________________________

Hilbert4.py is a turtle based Python 3 program to draw a Hilbert curve (a 2D 
space-filling fractal) of arbitrary order.

My original plan was to find an iterative approach to drawing the curve because I
assumed a recursive approach would be too slow. After a couple of agonising days
of failed attempts I scrapped the idea and looked online for how people
traditionally approach the problem.

The Hilbert Curve Wikipedia page explains how the curve can be expressed as a
Lindenmayer system ("L-System"). After reading up on L-Systems I implemented
the curve using the L-system rules as doubled recursive methods which take the
order of the curve as an argument, decrement the value, and terminate when the
value reaches 0.

Once I learned how to limit the number of screen updates while drawing using
turtle.tracer(), I found the recursive approach actually draws quite quickly,
even for quite high order curves.

Scaling the curve is handled by the keepscale() function which checks the
dimensions of the screen. If the dimensions have been altered since the last
check, the canvas coordinates reset and the screen is updated. It calls the
turtle.ontimer() function to poll every 200 milliseconds.

References:
https://en.wikipedia.org/wiki/Hilbert_curve
https://runestone.academy/runestone/books/published/thinkcspy/Strings/TurtlesandStringsandLSystems.html

________PERFORMANCE____________________________________________________________

I have tested the program on orders up to 20. Orders above 12 take upwards of 60
seconds to draw (on my lab machine). Because of this, the program will print a
terminal warning on any order over 9.

________AUTHOR_________________________________________________________________

Mickey Treadwell
