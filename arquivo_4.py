#Trabalhando com o list comprehension!
lista_de_numeros = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']

lista_de_numeros_convertida = [int(v) for v in lista_de_numeros]

lista_repetida = [z for z in lista_de_numeros_convertida]

lista_de_numeros_pares = [x for x in lista_de_numeros_convertida if x % 2 == 0 or x == 0]

print(lista_de_numeros_convertida)

print(lista_repetida)


print(lista_de_numeros_pares)