"""O programa vai ler um array e dizer quantos carros existem de cada marca"""

import numpy as np

carros = np.array(["opel","maserati","bmw","volvo","tesla","maserati","ford","maserati","bugatti"],dtype="U20")
marcas = np.zeros(len(carros),dtype="U20")

n = 0
for carro in carros:
    if carro in marcas:
        continue
    marcas[n] = carro
    n = n + 1
    contar = 0
    for carro2 in carros:
        if carro == carro2:
            contar = contar + 1
    print(f"A {carro} tem {contar} carros(s).")

