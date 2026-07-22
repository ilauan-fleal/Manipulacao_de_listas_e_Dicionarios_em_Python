#Exercício 2: Converter um tipo de lista em outro tipo:

lista_de_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']


#Criando função, para converter um tipo de lista em outro!


nova_lista = []


#Criando função para converter tipo de lista

def converter_tipo_lista(nova_lista,lista_de_strings):

        for x in range(len(lista_de_strings)):        
            nova_lista.append(int(lista_de_strings[x]))
           


#Criando função para identificar elementos repetidos e em seguida removê-los:

def remover_elementos_repetidos(nova_lista, lista_de_strings):
    converter_tipo_lista(nova_lista,lista_de_strings)
    for z in nova_lista:
         if nova_lista.count(z) > 1:
              nova_lista.remove(z)
              
    return nova_lista



y = remover_elementos_repetidos(nova_lista,lista_de_strings)


print(y)


