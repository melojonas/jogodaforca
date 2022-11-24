import turtle as t

t.screensize(500,500)
screen = t.Screen()

t.title('Jogo da Forca')

"""chute = t.textinput('Chute', 'Insira uma letra: ')"""

def rectangle(base1, base2, x, y, angle):
    '''desenha um retângulo, sendo base1 a menor e base2 a maior, x e y a coordenadas de partida, e angle a direção de partida
    int, int, int, int, int -> None'''
    rectangle = t.Turtle()
    rectangle.speed(0)
    rectangle.hideturtle()
    rectangle.color('brown', 'brown')

    rectangle.penup()
    rectangle.setpos(x,y)
    rectangle.setheading(angle)
    rectangle.pendown()

    rectangle.begin_fill()
    for x in range(2):
        rectangle.forward(base2)
        rectangle.right(90)
        rectangle.forward(base1)
        rectangle.right(90)
    rectangle.end_fill()

rectangle(25,500,250,-250,180)
rectangle(25,500,-250,-250,90)
rectangle(25,250,-250,250,0)
rectangle(25,50,0,250,270)
rectangle(25,(100*2**0.5),-250,150,45)



t.exitonclick()
