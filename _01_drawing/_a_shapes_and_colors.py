import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
qwerty = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
qwerty.shape('turtle')
# Set your turtle's speed using .speed(2)
qwerty.speed(2)
# Set your turtle's color using .color('green') and .pencolor('blue')
qwerty.color('green')
qwerty.pencolor('blue')
# Move your turtle forward using .forward(100)
qwerty.forward(100)
# TEST    Did your turtle move forward?

# Move your turtle left or right using .left(90) or .right(90)
qwerty.left(90)
# Now put the forward and left/right code into a for loop to repeat 4 times.
# TEST    Did your turtle draw a square?
qwerty.forward(100)
qwerty.right(90)
qwerty.forward(50)
qwerty.left(90)
qwerty.backward(300)
qwerty.left(90)
# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
qwerty.goto(0, 0)
qwerty.goto(-100, -70)
# Have your turtle draw a circle using .circle(radius, steps=30)
# TEST    Did your turtle draw a circle?
qwerty.color('blue')
qwerty.begin_fill()
qwerty.circle(100, 360)
# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below
qwerty.end_fill()
# Draw 3 more shapes with different fill colors!
qwerty.color('orange')
qwerty.pencolor('orange')
qwerty.begin_fill()
for i in range(8):
    qwerty.forward(200)
    qwerty.right(45)

qwerty.end_fill()
qwerty.goto(150, 150)
qwerty.color('violet')
qwerty.pencolor('gray')
qwerty.begin_fill()
for a in range(2):
    qwerty.right(90)
    qwerty.forward(50)
for b in range(3):
    qwerty.right(45)
qwerty.forward(90)
# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
