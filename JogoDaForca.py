#!/usr/bin/python3
'''
Autor: Jonas da Silva Melo, Gerson...
Propósito: Jogo da Forca
Contato: jonasmelo@ufrj.br
'''
import json
import turtle as t
from tkinter import Button
from random import choice
from unicodedata import normalize, combining

def main():
    
    #iniciar o GUI
    iniciarTurtle()

    #objetos Turtle que serão atualizados
    boneco = t.Turtle()
    bracos = t.Turtle()
    vidas = t.Turtle()

    #escolher modalidade e sortear palavra
    modalidade = escolher_modalidade()
    palavra = escolher_palavra(modalidade)
    mascara = ['_'] * len(palavra)

    
    n_vidas = 6
    atualizar_vidas(vidas, n_vidas)

    #escrever mascara e retornar posições para escrever letras
    posicoes = escrever_mascara(mascara)

    #iniciar loop do jogo
    while ''.join(mascara) != palavra and n_vidas != 0:
        teste = mascara.copy()
        mascara, chute = atualizar_mascara(palavra, mascara, posicoes)

        if teste == mascara:
            if chute == "":
                continue
            elif chute == None:
                break              
            else:
                n_vidas -= 1 
                atualizar_vidas(vidas, n_vidas)
                desenhar_boneco(n_vidas, boneco, bracos)
                cemiterio(chute, n_vidas)

    #avaliar e expor motivo de saída do loop
    perdeu_ou_ganhou(palavra, mascara, n_vidas)
    
    t.Screen().mainloop()

def iniciarTurtle():
    screen = t.Screen()
    screen.setup(1090,730)
    screen.screensize(1080,720)
    screen.bgpic('background.png')

    def reiniciar():
        screen.reset()
        main()
    def fechar():
        screen.bye()

    canvas = screen.getcanvas()
    botao_reiniciar = Button(canvas.master, text="Reiniciar", command=reiniciar)
    botao_fechar = Button(canvas.master, text="Fechar", command=fechar)
    
    botao_reiniciar.pack()
    botao_reiniciar.place(x=40, y=30)

    botao_fechar.pack()
    botao_fechar.place(x=100, y=30)

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

def escolher_palavra(modalidade):
    '''retorna uma palavra conforme a modalidade escolhida'''

    with open("palavras.json", "r") as read_file:
        palavras = json.load(read_file)
    
    grupo = choice(list(palavras[modalidade].keys()))
    palavra = choice(palavras[modalidade][grupo])

    t.penup()
    t.goto(340,260)
    t.pendown()
    t.write('Grupo: ', True, align='right', font=('Arial',24,'normal'))
    t.write(f'{grupo}', align='left', font=('Arial',24,'normal'))

    return palavra

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

    return mascara, chute

def desenhar_boneco(n_vidas, boneco, bracos):
    '''desenha o boneco do jogo da forca no Turtle
    int, Turtle object --> None'''
    boneco.speed(1)
    boneco.width(4)
    boneco.color('beige','beige')
    boneco.hideturtle()

    boneco.penup()

    bracos.speed(1)
    bracos.width(4)
    bracos.color('beige','beige')
    bracos.hideturtle()

    bracos.penup()

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
        bracos.goto(-70,120)
        bracos.setheading(0)
        bracos.pendown()

        for x in range(45):
            bracos.seth(x)
            bracos.forward(2)
    elif n_vidas == 2: #braço direito
        bracos.goto(-70,120)
        bracos.setheading(180)
        bracos.pendown()

        for x in range(180,135,-1):
            bracos.seth(x)
            bracos.forward(2)
    elif n_vidas == 1: #perna esquerda
        boneco.goto(-70,-5)
        boneco.setheading(315)
        boneco.pendown()

        boneco.forward(75)
    elif n_vidas == 0: 
        #perna direita
        boneco.goto(-70,-5)
        boneco.setheading(225)
        boneco.pendown()

        boneco.forward(75)

        #braços
        bracos.clear()
        bracos.speed(0)

        bracos.goto(-70,120)
        bracos.setheading(240)
        bracos.pendown()
        bracos.forward(75)

        bracos.up()
        bracos.goto(-70,120)
        bracos.setheading(300)
        bracos.pendown()
        bracos.forward(75)

        #olhos
        boneco.speed(0)
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

def cemiterio(chute, n_vidas):
    '''Escreve os chutes errados na tela
    str, int --> None'''
    t.penup()
    t.goto((-100 - n_vidas*60), -280) #Espaçamento de acordo com o número de vidas
    t.pendown()
    t.write(chute, move=True, align='right', font=('Arial',32,'normal'))
    if n_vidas > 0:
        t.write(" - ", align='left', font=('Arial',32,'normal'))

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

if __name__ == '__main__':
    main()
