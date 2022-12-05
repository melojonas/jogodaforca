from random import randint
def grupo_palavras(modalidade):
    
    '''fáceis''' 

    fruta_f = ['Amora' , 'Cereja' , 'Banana' , 'Morango' , 'Laranja' ] 
    objeto_f = ['Bandeira' , 'Chave' , 'Chinelo' , 'Janela' , 'Mala' ]
    pais_f = ['Argentina' , 'México' , 'Canadá' , 'Rússia' , 'Sérvia' ]
    cor_f = ['Azul' , 'Salmão' , 'Rosa' , 'Bege' , 'Lilás' ]
    animal_f = ['Abelha' , 'Foca' , 'Hiena' , 'Cachorro' , 'Gato' ]

    
    sortf = [fruta_f,pais_f,animal_f,objeto_f,cor_f] #Armazena listas de grupo de palavras
    sort_grupof = sortf[randint(0, len(sortf) -1)] #escolhe aleátorio um grupo de palavras


    '''dificeis '''
   
    objeto_d = ['Maçaneta' , 'Parafuso' , 'Abajur' , 'Envelope' , 'Espelho' ]
    animal_d = ['Flamingo' , 'Guiaxinim' , 'Golfinho' , 'Hipopótamo' , 'Garça' ]
    fruta_d = ['Damasco' , 'carambola' , 'Caqui' , 'Framboesa', 'Tangerina' ]
    cor_d = ['Turquesa' , 'Sépia' , 'Carmesim' , 'Fúchsia' , 'Índigo' ]
    pais_d = [ 'Afeganistão' , 'Venezuela' , 'Camarões' , 'Dinamarca' , 'Hungria' ]


  
    sortd = [fruta_d,pais_d,animal_d,objeto_d,cor_d] #Armazena listas de grupo de palavras
    sort_grupod = sortd[randint(0, len(sortd) -1)] #escolhe aleátorio um grupo de palavras


    
    if modalidade == 2: 
        return sort_grupod[randint(0, len(sort_grupod) -1)] #escolhe aleatoriamente difícil
    return  sort_grupof[randint(0, len(sort_grupof) -1)] #escolhe aleatoriamente fácil
        
