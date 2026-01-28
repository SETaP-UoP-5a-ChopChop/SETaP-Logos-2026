import turtle



t = turtle.Turtle()
t.right(180)
for i in range(20):
    t.forward(10)
    t.right(10)
t.penup()
t.forward(10)
t.right(90)
t.forward(30)
t.pendown()

t.circle(50)
turtle.done()