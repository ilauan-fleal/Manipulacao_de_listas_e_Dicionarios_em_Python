
import pandas as pd

#Armazenando leitura de arquivo csv na variável x

x = pd.read_csv("nato_phonetic_alphabet.csv")


dicionario_fonetico = {a.letter:a.code for (b,a) in x.iterrows()}

print(dicionario_fonetico)


y = input("Insira uma palavra:").upper()




lista_saida = [dicionario_fonetico[letter] for letter in y]



print(lista_saida)

