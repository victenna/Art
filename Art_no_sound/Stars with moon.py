import turtle
import random
t=turtle.Turtle()
t.hideturtle()
turtle.tracer(2)
colors=['gold','green','yellow','blue','navy']
turtle.bgcolor('navy')
t.up()
t.goto(0,0)
t.color('gold')
t.begin_fill()
t.circle(100)
t.end_fill()
t.up()
t.goto(-30,0)
t.color('navy')
t.down()
t.begin_fill()
t.circle(100)
t.end_fill()
for i in range(500):
    a=random.randint(-1000,1000)
    b=random.randint(-1000,1000)
    c=random.randint(0,180)
    d=random.randint(10,50)
    t.setheading(c)
    t.up()
    t.goto(a,b)
    t.down()
    t.color(random.choice(colors))
    t.color('white')
    t.begin_fill()
    
    for i in range(5):
        
        t.fd(d)
        t.left(144)

    t.end_fill()
