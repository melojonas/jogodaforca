import turtle as t
from turtle import *

setup(500, 500)
t.bgcolor('black')
t.width(4)
color('white')
hideturtle()

#cabeça if = 1
t.circle (50)

#tronco if=2

t.left(270)
t.forward(130)
t.penup()

t.goto(0,0)
t,left(-270)

t.pendown()
#Braço esquerdo if=3
t.left(270)
t.forward(15)
t.left(-270)
t.left(225)
t.forward(75)
t.penup()
t.backward(75)
t.left(-225)

#braço direito if = 4
t.pendown()
t.left(315)
t.forward(75)
t.backward(75)
t.left(-315)

t.left(270)
t.forward(130)
t.left(-270)

#perna esquerda if = 5
t.left(225)
t.forward(75)
t.penup()
t.backward(75)
t.left(-225)


#perna direita  if = 6
t.pendown()
t.left(315)
t.forward(75)
t.backward(75)
t.left(-315)

t.left (90)
t.penup()
t.forward(200)
t.left(-90)



#perdeu 6

t.forward(25)
t.left(45)
t.pendown()
color('red')

t.forward(5)
t.left(-45)
t.left(225)
t.forward(10)
t.penup()
t.backward(5)
t.left(-225)
t.left(125)
t.pendown()
t.forward(5)
t.left(-125)
t.left(315)
t.forward(10)

t.penup()

t.left(-315)
t.backward(50)
t.pendown()

t.left(45)
t.pendown()

t.forward(5)
t.left(-45)
t.left(225)
t.forward(10)
t.penup()
t.backward(5)
t.left(-225)
t.left(125)
t.pendown()
t.forward(5)
t.left(-125)
t.left(315)
t.forward(10)
