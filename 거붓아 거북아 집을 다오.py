import turtle
lol=turtle.Screen()
lol.bgcolor('light green')

x=int(input("집의 한변의 길이를 입력하세요:"))

t=turtle.Turtle()
t.shape('turtle')
t.right(90)
t.forward(x)
t.left(90)
t.forward(x)
t.left(90)
t.forward(x)
t.left(90)
t.forward(x+x/2)
t.right(150)
t.forward(((x+x/2)+(x))//2)
t.right(60)
t.forward(((x+x/2)+(x))//2)
t.right(150)
t.forward(((x+x/2)+(x))//2)

turtle.done()
