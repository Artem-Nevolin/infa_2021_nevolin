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


krug(3, 8)
turtle.left(60)
krug(3, 8)
turtle.left(60)
krug(3, 8)
turtle.speed(10)