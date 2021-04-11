import turtle
turtle.shape('turtle')

def krug1(x, y, a, b):
    turtle.color(a, b)
    turtle.begin_fill() # начало заливки
    for i in range(90):
        turtle.forward(x)
        turtle.left(y)
        turtle.forward(x)
    turtle.end_fill() # конец заливки


krug1(4, 4, 'black', 'yellow')
turtle.penup() # поднял перо т.е. невидимый перенос
turtle.goto(-50, 140) # перенос в другую точку начала рисования
turtle.pendown() # опустил перо для дальнейшего рисования
krug1(0.7, 4, 'black', 'blue') # вызов функции, но с другими парамертрами - рисование глаза
turtle.penup()
turtle.goto(50, 140)
turtle.pendown()
krug1(0.7, 4, 'black', 'blue')
turtle.penup()
turtle.goto(0, 120)
turtle.pendown()
turtle.width(8) # изменил толщину линии
turtle.right(90)
turtle.forward(50)
turtle.penup()
turtle.goto(50, 70)
turtle.pendown()
turtle.color('red') # изменил цвет линии
turtle.circle(-50, 180)

turtle.penup()
turtle.goto(-45, 160)
turtle.pendown()
turtle.color('white')
turtle.width(0)
turtle.begin_fill() # начало заливки
turtle.circle(5)
turtle.end_fill() # конец заливки

turtle.penup()
turtle.goto(55, 160)
turtle.pendown()
turtle.color('white')
turtle.width(0)
turtle.begin_fill() # начало заливки
turtle.circle(5)
turtle.end_fill() # конец заливки


