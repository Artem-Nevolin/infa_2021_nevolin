import turtle
turtle.shape('turtle')

def krug(x, y):

    for i in range(45):

        turtle.forward(x)
        turtle.left(y)
        turtle.forward(x)
    for i in range(45):
        turtle.forward(x)
        turtle.right(y)
        turtle.forward(x)

turtle.left(90)
krug(3, 8)
krug(3.5, 8)
krug(4, 8)
krug(4.5, 8)
krug(5, 8)
krug(5.5, 8)
krug(6, 8)
krug(6.5, 8)
krug(7, 8)