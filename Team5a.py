import turtle


t = turtle.Turtle()
t.right(180)
for i in range(18):
    t.forward(10)
    t.right(10)
t.forward(10)
t.penup()
t.forward(50)
t.pendown()
t.right(90)
t.forward(100)
t.right(180)
t.forward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(180)
t.forward(100)

t.penup()
t.right(90)
t.forward(50)
t.pendown()
t.circle(50)


def draw_circle(t, radius):
    t.circle(radius)


def draw_knife(t, angle=0):
    t.setheading(angle)
    t.forward(100)
    t.right(90)
    t.forward(20)
    # Draw curved part of blade
    t.right(90)
    t.circle(-280, 22)


draw_knife(turtle.Turtle(), 270)
turtle.done()