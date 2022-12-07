import json
import turtle as t
from random import choice
from unicodedata import normalize, combining


def main():
    '''executa as funções que implementam o jogo'''
    modalidade = escolher_modalidade()
    palavra = escolher_palavra(modalidade)
    mascara = ['_'] * len(palavra)

    #iniciar turtle
    iniciar_turtle()

    #criar objeto para atualizar vidas
    vidas = t.Turtle()
    n_vidas = 6
    atualizar_vidas(vidas, n_vidas)

    #escrever mascara e retornar posições para escrever letras
    posicoes = escrever_mascara(mascara)

    #iniciar loop do jogo
    while ''.join(mascara) != palavra and n_vidas != 0:
        teste = mascara.copy()
        mascara = atualizar_mascara(palavra, mascara, posicoes)

        if teste == mascara:
            n_vidas -= 1
            atualizar_vidas(vidas, n_vidas)
            desenhar_boneco(n_vidas)

    #avaliar e expor motivo de saída do loop
    perdeu_ou_ganhou(palavra, mascara, n_vidas)

    t.exitonclick()

def escolher_palavra(modalidade):
    '''retorna uma palavra conforme a modalidade escolhida'''

    with open("data_file.json", "r") as read_file:
        palavras = json.load(read_file)
    
    grupo = choice(list(palavras[modalidade].keys()))
    palavra = choice(palavras[modalidade][grupo])

    t.penup()
    t.goto(340,260)
    t.pendown()
    t.write('Grupo: ', True, align='right', font=('Arial',24,'normal'))
    t.write(f'{grupo}', align='left', font=('Arial',24,'normal'))

    return palavra

def iniciar_turtle():
    '''Inicia o modulo turtle e cria um fundo'''
    t.title('Jogo da Forca')
    screen = t.Screen()
    screen.setup(1090,730)
    screen.screensize(1080,720)
    screen.bgpic('background.png')

def escolher_modalidade():
    '''Input do usuário que define a dificuldade do jogo'''
    modalidade = t.textinput('Insira um número', '(1) Fácil ou (2) Difícil: ')
    texto_mod = 'Fácil' if modalidade == '1' else 'Difícil' #resolver problema de unicode UTF-8 no arquivo json

    t.hideturtle()
    t.color('white')

    t.penup()
    t.goto(340,300)
    t.pendown()
    t.write('Modalidade: ', True, align='right', font=('Arial',24,'normal'))
    t.write(f'{texto_mod}', align='left', font=('Arial',24,'normal'))

    return texto_mod

def atualizar_vidas(vidas, n_vidas):
    '''cria um objeto do Turtle para atualizar o número de vidas'''
    vidas.clear()

    vidas.hideturtle()
    vidas.color('white')

    vidas.penup()
    vidas.goto(340,220)
    vidas.pendown()
    vidas.write('Vidas: ', True, align='right', font=('Arial',24,'normal'))
    vidas.write(f'{n_vidas}', align='left', font=('Arial',24,'normal'))

def escrever_mascara(mascara):
    '''Escreve underlines na tela'''
    t.hideturtle()
    t.color('white')

    t.penup()
    t.goto(-250,-210)
    t.pendown()

    length = len(mascara)
    size_under = 105 - 5 * length
    space = 60 - 3 * length

    posicoes = []

    for underline in mascara:
        posicoes.append(t.pos()[0])
        t.write(underline, True, align='left', font=('Arial',size_under,'normal'))
        t.penup()
        t.forward(space)
        t.pendown()

    return posicoes

def atualizar_mascara(palavra, mascara, posicoes):
    '''Escreve as letras caso o input esteja correto'''
    length = len(mascara)
    tam_letra = 54 - 2.7 * length
    x_letra = (70 - 3.2 * length) / 2

    chute = t.textinput('Chute', 'Insira uma letra: ')

    i = 0
    for word in palavra:

        if word.lower() in 'áéíóúâêôçã':
            sem_acento = normalize('NFD', word)
            sem_acento = ''.join(a for a in sem_acento if not combining(a))
            if sem_acento.lower() == chute:
                mascara[i] = word
                t.penup()
                t.goto(posicoes[i] + x_letra,-200)
                t.pendown()
                t.write(word, align='center', font=('Arial',int(tam_letra),'normal'))
        elif word.lower() == chute:
            mascara[i] = word
            t.penup()
            t.goto(posicoes[i] + x_letra,-200)
            t.pendown()
            t.write(word, align='center', font=('Arial',int(tam_letra),'normal'))
        i += 1

    return mascara

def perdeu_ou_ganhou(palavra, mascara, n_vidas):
    '''Avalia se o jogador completou a mascara ou zerou as vidas'''
    t.hideturtle()
    t.color('red')

    t.penup()
    t.goto(0,0)
    t.pendown()

    if ''.join(mascara) == palavra:
        t.write('Você ganhou!', align='center', font=('Arial',32,'bold'))
    elif n_vidas == 0:
        t.write(f'Você perdeu! A palavra era: {palavra}.', align='center', font=('Arial',32,'bold'))

def desenhar_boneco(n_vidas):
    boneco = t.Turtle()
    boneco.speed(7)
    boneco.width(4)
    boneco.color('beige','beige')
    boneco.hideturtle()

    boneco.penup()

    if n_vidas == 5: #cabeça
        boneco.goto(-70,145)
        boneco.pendown()
        
        boneco.begin_fill()
        boneco.circle(30)
        boneco.end_fill()
    elif n_vidas == 4: #tronco
        boneco.goto(-70,145)
        boneco.pendown()

        boneco.left(270)
        boneco.forward(150)
    elif n_vidas == 3: #braço esquerdo
        boneco.goto(-70,120)
        boneco.setheading(0)
        boneco.pendown()

        for x in range(45):
            boneco.seth(x)
            boneco.forward(2)
    elif n_vidas == 2: #braço direito
        boneco.goto(-70,120)
        boneco.setheading(180)
        boneco.pendown()

        for x in range(180,135,-1):
            boneco.seth(x)
            boneco.forward(2)
    elif n_vidas == 1: #perna esquerda
        boneco.goto(-70,-5)
        boneco.setheading(315)
        boneco.pendown()

        boneco.forward(75)
    elif n_vidas == 0: #perna direita e olhos
        boneco.goto(-70,-5)
        boneco.setheading(225)
        boneco.pendown()

        boneco.forward(75)

        boneco.color('red')
        boneco.penup()
        boneco.goto(-60,190)
        boneco.setheading(315)
        boneco.pendown()

        boneco.forward(15)

        boneco.penup()
        boneco.goto(-50,190)
        boneco.setheading(225)
        boneco.pendown()

        boneco.forward(15)

        boneco.penup()
        boneco.goto(-80,190)
        boneco.setheading(225)
        boneco.pendown()

        boneco.forward(15)

        boneco.penup()
        boneco.goto(-90,190)
        boneco.setheading(315)
        boneco.pendown()

        boneco.forward(15)

if __name__ == '__main__':
    main()
