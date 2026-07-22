

#OBJETIVO: Criar um dicionário, que irá armazenar cada palavra dessa sentença e irá contar quantas letras tem cada uma delas!

import random

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"



dicionario_1 = {sentence: x for x in range(len(sentence)) if sentence[x] != " "}


dicionario_2 = {x for x in dicionario_1.keys() if dicionario_1[x] != " "}


print(dicionario_1)

print(dicionario_2)