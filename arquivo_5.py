#Criar uma lista, na qual irá conter os números que são comuns em ambos os arquivos!


import pandas as pd

x = pd.read_csv("arquivo_1.csv")

y = x.Numeros.to_list()



print(y)

z = pd.read_csv("arquivo_2.csv")

k = z.Numeros.to_list()

print(k)

nova_lista = []


def CriarNovaListaSemRepeticao(nova_lista):
    for m in range(len(y)):

        for n in range(len(k)):
            if y[m] == k[n]:
                nova_lista.append(k[n])
                break


#Chamada da função, com o devido parâmetro!


CriarNovaListaSemRepeticao(nova_lista)


print(nova_lista)