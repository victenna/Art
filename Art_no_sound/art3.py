import turtle
import random
turtle.tracer(5)
wn=turtle.Screen()
wn.bgcolor('blue')
#turtle.tracer(5)
t=turtle.Turtle('turtle')
#t.hideturtle()

t.pensize(2)
#t.up()
clr=['red','brown','blue','pink','gold','violet','navy','green','firebrick']

def draw_star(points,size,x,y):
    t.up()
    t.goto(x,y)
    t.down()
    angle=180-(180/points)
    t.color(random.choice(clr))
    t.begin_fill()
    for m in range(points):
        t.fd(size)
        t.rt(angle)
    t.end_fill()
    
draw_star(12,100, 200,-100)   
    
while True:
    Xpos=random.randint(-300,300)
    Ypos=random.randint(-300,300)
    length=random.randint(10,30)
    points_num=random.randint(3,10)
    draw_star(points_num,length, Xpos,Ypos) 
    
    