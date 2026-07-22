import pandas as pd

dados = {
    "Estudante":["Alpha", "Beta", "Gama", "Delta"],
    "recorde":[98,76,84,85]
}

data_frame_estudante = pd.DataFrame(dados)
print(data_frame_estudante)

for(x,y) in data_frame_estudante.iterrows():
    if y.Estudante == "Alpha":
        print(y.recorde)
