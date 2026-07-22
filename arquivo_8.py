#OBJETIVO: Criar um dicionário, que irá armazenar cada palavra dessa sentença e irá contar quantas letras tem cada uma delas!



sentence = "What is the Airspeed Velocity of an Unladen Swallow?"


dicionario = {}

for x in sentence.split():
    if x in dicionario:
        dicionario[x] += 1
    else:
        dicionario[x] = 1

    
        


print(dicionario)


