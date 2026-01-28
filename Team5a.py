import turtle


t = turtle.Turtle()

turtle.Screen().bgcolor("orange")

t.speed(150)
t.pensize(10)
t.color("Black")
for i in range(2):
    t.forward(200)
    t.left(90)
    t.forward(150)
    t.left(90)


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
    t.penup()
    t.goto(180,120)
    t.pendown()
    t.setheading(angle)
    t.penup()
    t.backward(180)
    t.pendown()
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(20)
    # Draw curved part of blade
    t.right(90)
    t.circle(-280, 22)
    t.end_fill()


draw_knife(turtle.Turtle(), 30)
turtle.done()