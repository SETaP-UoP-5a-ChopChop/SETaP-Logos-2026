import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("#f5f5f5")  


t.penup()
t.goto(0, -120)
t.pendown()
t.color("#1abc9c")        
t.begin_fill()
t.circle(120)
t.end_fill()


t.penup()
t.goto(-60, 60)
t.pendown()
t.color("#ffffff")        
t.begin_fill()
for _ in range(4):
    t.forward(120)
    t.right(90)
t.end_fill()


t.penup()
t.goto(0, -20)
t.color("#1abc9c")
t.write("DCS", align="center", font=("Arial", 40, "bold"))

t.hideturtle()
turtle.done()
