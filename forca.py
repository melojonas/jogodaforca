'''
Autor: Jonas da Silva Melo, Gerson...
Propósito: Jogo da Forca
Contato: jonasmelo@ufrj.br
'''

from random import randint
from unicodedata import normalize, combining


def main():
    '''executa as funções que implementam o jogo'''
    escolha_mod = input("Insira o número correspondente para a modalidade:\n"
                        + "(1) Fácil ou (2) Difícil: ")
    palavra = choose_word(escolha_mod)
    mascara = ['_'] * len(palavra)

    print(f'A palavra tem {len(palavra)} letras.\n{" ".join(mascara)}')

    vidas = 6
    while ''.join(mascara) != palavra and vidas != 0:
        teste = mascara.copy()
        mascara = atualizar_mascara(palavra, mascara)

        if teste == mascara:
            vidas -= 1
            print(f'Você tem {vidas} vidas.')
        else:
            print(" ".join(mascara))

    if ''.join(mascara) == palavra:
        print(f'Você ganhou! A palavra é: {palavra}.')
    elif vidas == 0:
        print(f'Você foi enforcado. A palavra é: {palavra}.')

    input("Enter para encerrar.")

def choose_word(modalidade):
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
                'Otorrinolaringologista','Panaceia','Paralelepípedo','Pororoca','Prognósticio',
                'Quarentena','Quimera','Refeição','Reportagem','Sino','Taciturno','Temperança',
                'Tênue','Ufanismo','Viscera']

    if modalidade == '1':
        return p_facil[randint(0, len(p_facil) -1)]
    elif modalidade == '2':
        return p_dificil[randint(0, len(p_facil) -1)]


def atualizar_mascara(palavra, mascara):
    '''atualiza a máscara de acordo com o input do usuário'''
    chute = input("Escolha uma letra: ")

    i = 0
    for word in palavra:

        if word.lower() in 'áéíóúâêôçã':
            sem_acento = normalize('NFD', word)
            sem_acento = ''.join(a for a in sem_acento if not combining(a))
            if sem_acento.lower() == chute:
                mascara[i] = word
        elif word.lower() == chute:
            mascara[i] = word

        i += 1

    return mascara


if __name__ == '__main__':
    main()
