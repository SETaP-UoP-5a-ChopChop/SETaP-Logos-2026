import turtle

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