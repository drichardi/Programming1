import turtle

import math

# create turtle
bob = turtle.Turtle()
print(bob)  # display type of bob

# Make a square of length 100
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)

# Introduce looping
for i in range(4):
     print("Hello!")

# Implement looping to draw a square
# for i in range(4):
#      bob.fd(100)
#      bob.lt(90)

# Encapsulate code into a function
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

# Generalize function by adding parameters
def square2(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

# Add more generalization with more parameters
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

# Create an interface (How to use a function not How it does it
# Keep parameters relative to circle, not to polygon
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

# Refine code to handle circles of any size better
def circle2(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, length, n)


if __name__ == '__main__':
    square2(bob, 50)

    polygon(bob, 200, 9)
    polygon(bob, length=70, n=7)

    alexa = turtle.Turtle()

    circle(bob, 100)
    circle2(alexa, 500)
    turtle.mainloop()
