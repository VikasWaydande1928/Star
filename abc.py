import turtle
import colorsys
p=turtle.Turtle()
s=turtle.Screen()
s.title("StudyMuch")
s.bgcolor("black")
p.pensize(3)
p.speed(0)
n=36
h=0.5

for i in range(75):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=1/n
    p.color(c)
    p.left(10)
    for j in range(75):
        p.forward(400)
        p.left(500)
turtle.done()
