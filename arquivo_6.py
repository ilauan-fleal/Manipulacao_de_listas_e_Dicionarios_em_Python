

#Obtendo dados de arquivo.txt e convertendo-o em uma lista!



#Criando função, para realizar leitura de arquivo e em seguida armazená-lo em uma lista

lista_de_strings_1 = []

lista_de_strings_2 = []

Nova_Lista = []

#Definindo função, para criar lista:

def CriarLista(lista_1, lista_2):
    with open("arquivo_1.txt", "r") as f:
        lista_1 += f.read().splitlines()
    with open("arquivo_2.txt", "r") as r:
        lista_2 += r.read().splitlines()

#Chamada da função, com os argumentos!

CriarLista(lista_de_strings_1,lista_de_strings_2)



#Convertendo a lista do tipo str, para int:



lista_1_convertida = [int(v) for v in lista_de_strings_1]

lista_2_convertida = [int(j) for j in lista_de_strings_2]

#Criando função, para gerar lista de elementos em comum

def CriarListaDeElementosEmComum(lista_1, lista_2):
    for k in range(len(lista_1)):
        for u in range(len(lista_2)):
            if lista_1[k] == lista_2[u]:
                Nova_Lista.append(lista_2[u])
                break


CriarListaDeElementosEmComum(lista_1_convertida, lista_2_convertida)

print(Nova_Lista)
