import turtle
turtle.shape('turtle')

def krug(x, y, z):

    for i in range(45):

        turtle.forward(x)
        turtle.right(y)
        turtle.forward(x)
    for i in range(45):
        turtle.forward(z)
        turtle.right(y)
        turtle.forward(z)


turtle.left(90)
a = 5
for i in range(a):
    krug(1, 4, 0.25)
    a -= 1