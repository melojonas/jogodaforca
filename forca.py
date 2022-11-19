#!/usr/bin/env python3
#Autor: Jonas da Silva Melo
#Propósito: Jogo da Forca
#Contato: jonasmelo@ufrj.br
from random import randint
from unicodedata import normalize, combining


def main():
    escolha_mod = input("Insira o número correspondente para a modalidade: \n(1) Fácil ou (2) Difícil: ")
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
    p_facil = ['Amarelo','Amiga','Amor','Ave','Avião','Avó','Balão','Bebê','Bolo','Branco','Cama','Caneca','Celular','Céu','Clube','Copo','Doce','Elefante','Escola','Estojo','Faca','Foto','Garfo','Geleia','Girafa','Janela','Limonada','Mãe','Meia','Noite','Óculos','Ônibus','Ovo','Pai','Pão','Parque','Passarinho','Peixe','Pijama','Rato','Umbigo']
    p_dificil = ['Acender','Afilhado','Agnóstico','Ardiloso','Áspero','Assombração','Asterisco','Balaústre','Basquete','Caminho','Champanhe','Chiclete','Chuveiro','Coelho','Contexto','Convivência','Coração','Desalmado','Eloquente','Esfirra','Esquerdo','Exceção','Filantropo','Fugaz','Gororoba','Heterossexual','Horrorizado','Idiossincrasia','Impacto','Inócuo','Independência','Jocoso','Laurel','Modernidade','Oftalmologista','Otorrinolaringologista','Panaceia','Paralelepípedo','Pororoca','Prognósticio','Quarentena','Quimera','Refeição','Reportagem','Sino','Taciturno','Temperança','Tênue','Ufanismo','Viscera']

    if modalidade == '1':
        return p_facil[randint(0, len(p_facil) -1)]
    elif modalidade == '2':
        return p_dificil[randint(0, len(p_facil) -1)]


def atualizar_mascara(palavra, mascara):
    
    chute = input("Escolha uma letra: ")
    
    i = 0
    for x in palavra:

        if x.lower() in 'áéíóúâêôçã':
            y = normalize('NFD', x)
            y = ''.join(a for a in y if not combining(a))
            if y.lower() == chute:
                mascara[i] = x
        elif x.lower() == chute:
            mascara[i] = x

        i += 1
    
    return mascara



if __name__ == '__main__': 
    main()