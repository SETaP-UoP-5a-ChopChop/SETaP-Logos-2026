import turtle



t = turtle.Turtle()

turtle.Screen().bgcolor("orange")

t.speed(53268)
t.pensize(10)
t.color("Black")
for i in range(2):
    t.forward(200)
    t.left(90)
    t.forward(150)
    t.left(90)
t.penup()
t.goto(180,120)
t.pendown()

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