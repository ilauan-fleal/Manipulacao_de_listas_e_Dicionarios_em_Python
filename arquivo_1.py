#Observa-se alguns modos interessantes, para manipular listas em Python!

numeros = [1,2,3,4,5,6,7,8,9]

nova_lista = [x for x in numeros if x % 2 == 0]

print(nova_lista)

#Lista geradora de números em Python!

lista_geradora = [n * 2 for n in range(1,14,1)]

print(lista_geradora)

lista_letras = ["Alpha", "Gama", "Beta", "Delta", "Theta"]

outra_lista = [y for y in lista_letras if len(y) < 5]

print(outra_lista)