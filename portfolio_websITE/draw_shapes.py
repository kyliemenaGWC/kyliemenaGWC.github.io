from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below:
sides = int(input('how many sides?'))
for x in range(sides):
	t.forward(100)
	t.right(360/sides)
# Close window on click.
exitonclick()