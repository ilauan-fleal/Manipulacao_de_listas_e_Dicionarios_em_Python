# Dictionary comprehension
nomenclatura = ["Alpha", "Gama", "Beta", "Delta", "Theta", "Eta", "Lambda"]

import random

recorde_nomes = {x : random.randint(1,100) for x in nomenclatura}



nomes_aprovados = {x:y for (x,y) in recorde_nomes.items() if y >= 70 }

print(recorde_nomes)

print(nomes_aprovados)



