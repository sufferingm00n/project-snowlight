import turtle

import random



def Leftclick(x,y):
    global r,g,b
    turtle.penup()
    turtle.color(r,g,b,)
    turtle.stamp()
    ts=random.randrange(1,10)
    tc=random.randrange(1,360)
    r=random.random()
    g=random.random()
    b=random.random()
    turtle.right(tc)
    turtle.shapesize(ts)
    turtle.goto(x,y)
    
r,g,b= 0.0,0.0,0.0
##main code##


turtle.title("거북이 도장")

turtle.shape('turtle')

turtle.onscreenclick(Leftclick,1)

turtle.done()
