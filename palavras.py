import json
from random import randint, choice

with open("data_file.json", "r") as read_file:
    palavras = json.load(read_file)

grupo = choice(list(palavras['Facil'].keys()))  
print(choice(palavras['Facil'][grupo]))
#palavras['Fácil'][randint(0, len(palavras) -1)])