from turtle import *

setup(1080, 720)
screensize(1080,720)
bgcolor('black')

doll = Turtle()
doll.speed(7)
doll.width(4)
doll.color('gray','gray')
doll.hideturtle()

#cabeça if = 1
doll.begin_fill()
doll.circle(50)
doll.end_fill()


#tronco if=2

doll.left(270)
doll.forward(150)

doll.penup()
doll.home()

#Braço esquerdo if=3
doll.goto(0,-25)
doll.setheading(0)
doll.pendown()

for x in range(45):
    doll.seth(x)
    doll.forward(2)

doll.penup()
doll.home()

#braço direito if = 4
doll.goto(0,-25)
doll.setheading(180)
doll.pendown()

for x in range(180,135,-1):
    doll.seth(x)
    doll.forward(2)

doll.penup()
doll.home()

#perna esquerda if = 5
doll.goto(0,-150)
doll.setheading(315)
doll.pendown()

doll.forward(75)

doll.penup()
doll.home()

#perna direita  if = 6
doll.goto(0,-150)
doll.setheading(225)
doll.pendown()

doll.forward(75)

doll.penup()
doll.home()


#perdeu 6
doll.clear()

perdeu = Turtle()
perdeu.width(4)
perdeu.speed(-1)
perdeu.hideturtle()
perdeu.color('gray','gray')

#cabeça if = 1
perdeu.begin_fill()
perdeu.circle(50)
perdeu.end_fill()


#tronco if=2

perdeu.left(270)
perdeu.forward(150)

perdeu.penup()
perdeu.home()

#Braço esquerdo if=3
perdeu.goto(0,-25)
perdeu.setheading(0)
perdeu.pendown()

for x in range(45):
    perdeu.seth(x)
    perdeu.forward(2)

perdeu.penup()
perdeu.home()

#braço direito if = 4
perdeu.goto(0,-25)
perdeu.setheading(180)
perdeu.pendown()

for x in range(180,135,-1):
    perdeu.seth(x)
    perdeu.forward(2)

perdeu.penup()
perdeu.home()

#perna esquerda if = 5
perdeu.goto(0,-150)
perdeu.setheading(315)
perdeu.pendown()

perdeu.forward(75)

perdeu.penup()
perdeu.home()

#perna direita  if = 6
perdeu.goto(0,-150)
perdeu.setheading(225)
perdeu.pendown()

perdeu.forward(75)

perdeu.penup()
perdeu.home()

#olhos
perdeu.color('red')
perdeu.goto(15,70)
perdeu.setheading(315)
perdeu.pendown()

perdeu.forward(15)

perdeu.penup()
perdeu.goto(25,70)
perdeu.setheading(225)
perdeu.pendown()

perdeu.forward(15)

perdeu.penup()
perdeu.goto(-15,70)
perdeu.setheading(225)
perdeu.pendown()

perdeu.forward(15)

perdeu.penup()
perdeu.goto(-25,70)
perdeu.setheading(315)
perdeu.pendown()

perdeu.forward(15)

exitonclick()
