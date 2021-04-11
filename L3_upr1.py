import turtle
import random
turtle.shape('turtle')


i = 2

while i > 1:
    x = random.randint(0, 90)
    if x > 45:
        turtle.left(x)
    else:
        turtle.right(x)
    turtle.forward(50*random.random())

i += 1

