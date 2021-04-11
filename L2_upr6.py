import turtle
turtle.shape('turtle')
x = 30

for i in range(50):
    turtle.right(x)
    turtle.forward(100)
    turtle.stamp()
    turtle.goto(0, 0)
x += 30