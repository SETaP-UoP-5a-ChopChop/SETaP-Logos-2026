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

def chop():
    t.penup()
    t.goto(-125, -125)
    t.pendown()
    t.right(180)
    def c():
        for i in range(18):
            t.forward(9)
            t.right(10)
        t.forward(10)
    c()
    def h():
        t.penup()
        t.forward(30)
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
    h()

    def o():
        t.penup()
        t.left(90)
        t.forward(80)
        t.pendown()
        t.circle(50)
    o()


def draw_circle(t, radius):
    t.circle(radius)

def draw_knife(t, angle=0,start_pos=(50,50)):
    t.pensize(1)
    t.penup()
    t.goto(start_pos)
    t.pendown()
    t.begin_fill()
    
    t.setheading(angle)
    #draw straight part of blade
    t.forward(100)
    t.right(90)
    t.forward(5)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(30)
    t.left(90)
    t.forward(5)
    # Draw curved part of blade
    t.right(90)
    t.circle(-280, 22)
    t.end_fill()
    t.penup()
    t.ht()

chop()
draw_knife(turtle.Turtle(), 30)
turtle.done()