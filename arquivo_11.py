#Outro exercício:


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

#Criando dicionário, para converter temperatura de Celsius, para Fahrenheit.


weather_f = {x: round(y*1.8 + 32, 1) for (x,y) in weather_c.items()}

print(weather_f)
