import turtle
turtle.shape('turtle')
a = 1
while a > 0:

    x = -10
    y = -10
    z = 20

    for i in range(10):

        turtle.forward(z)
        turtle.left(90)
        turtle.forward(z)
        turtle.left(90)
        turtle.forward(z)
        turtle.left(90)
        turtle.forward(z)
        turtle.left(90)

        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

        x -= 10
        y -= 10
        z += 20
    "?"


























    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    a += 1



