import json
from random import randint, choice

with open("data_file.json", "r") as read_file:
    palavras = json.load(read_file)

grupo = choice(list(palavras['Fácil'].keys()))  
print(choice(palavras['Fácil'][grupo]))
#palavras['Fácil'][randint(0, len(palavras) -1)]

'''palavras = {
    "Fácil": {
    "Fruta": ['Amora', 'Cereja', 'Banana', 'Morango', 'Laranja'], 
    "Objeto": ['Bandeira', 'Chave', 'Chinelo', 'Janela', 'Mala'],
    "País": ['Argentina', 'México', 'Canadá', 'Rússia', 'Sérvia'],
    "Cor": ['Azul', 'Salmão', 'Rosa', 'Bege', 'Lilás'],
    "Animal": ['Abelha', 'Foca', 'Hiena', 'Cachorro', 'Gato']},

    "Difícil": {
        "Fruta": ['Damasco', 'carambola', 'Caqui', 'Framboesa', 'Tangerina'],
        "Objeto": ['Maçaneta', 'Parafuso', 'Abajur', 'Envelope', 'Espelho'],
        "País": [ 'Afeganistão', 'Venezuela', 'Camarões', 'Dinamarca', 'Hungria'],
        "Cor": ['Turquesa', 'Sépia', 'Carmesim', 'Fúchsia', 'Índigo'],
        "Animal": ['Flamingo', 'Guiaxinim', 'Golfinho', 'Hipopótamo', 'Garça']}
}

with open("data_file.json", "w") as write_file:
    json.dump(palavras, write_file, indent=4, ensure_ascii=False)'''