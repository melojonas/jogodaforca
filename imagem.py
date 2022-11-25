import turtle as t
from random import randint
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

    #avaliar e expor motivo de saída do loop
    perdeu_ou_ganhou(palavra, mascara, n_vidas)

    t.exitonclick()

def escolher_palavra(modalidade):
    '''retorna uma palavra conforme a modalidade escolhida'''
    p_facil = ['Amarelo','Amiga','Amor','Ave','Avião','Avó','Balão',
                'Bebê','Bolo','Branco','Cama','Caneca','Celular','Céu',
                'Clube','Copo','Doce','Elefante','Escola','Estojo','Faca',
                'Foto','Garfo','Geleia','Girafa','Janela','Limonada','Mãe',
                'Meia','Noite','Óculos','Ônibus','Ovo','Pai','Pão','Parque',
                'Passarinho','Peixe','Pijama','Rato','Umbigo']
    p_dificil = ['Acender','Afilhado','Agnóstico','Ardiloso','Áspero','Assombração',
                'Asterisco','Balaústre','Basquete','Caminho','Champanhe','Chiclete',
                'Chuveiro','Coelho','Contexto','Convivência','Coração','Desalmado',
                'Eloquente','Esfirra','Esquerdo','Exceção','Filantropo','Fugaz',
                'Gororoba','Heterossexual','Horrorizado','Idiossincrasia','Impacto',
                'Inócuo','Independência','Jocoso','Laurel','Modernidade','Oftalmologista',
                'Panaceia','Paralelepípedo','Pororoca','Prognósticio',
                'Quarentena','Quimera','Refeição','Reportagem','Sino','Taciturno','Temperança',
                'Tênue','Ufanismo','Viscera']

    if modalidade == '2':
        return p_dificil[randint(0, len(p_facil) -1)]
    
    return p_facil[randint(0, len(p_facil) -1)]

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
    texto_mod = 'Fácil' if modalidade == '1' else 'Difícil'

    t.hideturtle()
    t.color('white')

    t.penup()
    t.goto(300,300)
    t.pendown()
    t.write('Modalidade: ', True, align='right', font=('Arial',24,'normal'))
    t.write(f'{texto_mod}', align='left', font=('Arial',24,'normal'))

    return modalidade

def atualizar_vidas(vidas, n_vidas):
    '''cria um objeto do Turtle para atualizar o número de vidas'''
    vidas.clear()

    vidas.hideturtle()
    vidas.color('white')

    vidas.penup()
    vidas.goto(300,270)
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

if __name__ == '__main__':
    main()
