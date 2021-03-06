"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Ethan Mahn.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
import math
window = rg.TurtleWindow()

felix=rg.SimpleTurtle('turtle')
felix.pen=rg.Pen('SeaGreen3',22)
felix.speed=176
penelope=rg.SimpleTurtle('turtle')
penelope.pen=rg.Pen('bisque4',19)
penelope.speed=184

for k in range(27):
    felix.right(math.cosh(k))
    felix.forward(10*math.atan(k))
    penelope.draw_regular_polygon(k,k**3/(k*10+1))
    felix.left(90)
    felix.forward(20)
    penelope.forward(7)
window.close_on_mouse_click()