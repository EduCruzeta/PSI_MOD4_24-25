import numpy as np
nomes = input("")
tempo = input("")
pilotos = np.array(nomes.split(" , "))
voltas = np.array(tempo.split(" , "))
i = 0
while i > 5:
    if int(voltas[i])< 0:
        voltas[i] = int(input(""))
    else:
        i = i + 1

pm = 0
pp = 0
for i in range(5):
    if voltas[i] < voltas[pm]:
        pm = i
    if voltas[i] > voltas[pp]:
        pp = i

diferenca = voltas[pp] - voltas[pm]
print(f"Primeiro lugar: {pilotos[pm]}")
print(f"Ultimo lugar: {pilotos[pp]}")
print("Diferença",diferenca)
for i in range(5):
    print(pilotos[i],voltas[i])