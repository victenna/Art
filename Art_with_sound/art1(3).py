import turtle,time
import random
import winsound

t1=turtle.Turtle()
t2=turtle.Turtle()
turtle.bgpic('stars.gif')
turtle.tracer(17)
clr1=['red','brown','blue','pink','gold','violet','navy','green','firebrick','purple']
clr2=['orange red','blue','pink','gold','violet','brown','navy','green','firebrick','purple']
winsound.PlaySound('music1.wav', winsound.SND_ASYNC)

while True:
    k1=random.randint(56,168)
    i1=1
    t1.color('red')
    t1.up()
    #t1.clear()
    t1.goto(random.randint(-400,400),random.randint(-400,400))
    t1.down()
    t1.pensize(3)
    
    k2=random.randint(56,168)
    i2=1
    t2.color('red')
    t2.up()
    #t2.clear()
    t2.goto(random.randint(-400,400),random.randint(-400,400))
    t2.down()
    t2.pensize(3)
    for m in range(50):
        t1.fd(i1)
        t1.right(k1)
        t1.color(random.choice(clr1))
        i1=i1+1
        
        t2.fd(i2)
        t2.lt(k2)
        t2.color(random.choice(clr2))
        i2=i2+1
        time.sleep(0.02)