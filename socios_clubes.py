"""Este programa vai ler dois array e indicar qual a pessoa que se repete nos dois"""
import numpy as np

Socios_A = np.array(["joaquim","Maria","João","Luís"])

Socios_B = np.array(["Carla","António","Maria","Luís"])

contar = 0

for nome_A in Socios_A:
    for nome_B in Socios_B:
        if nome_A == nome_B:
            print(f"O sócio com o nome {nome_A} pertence aos dois clubes.")

# Versao 2

for nome_A in Socios_A:
    if nome_A in Socios_B:
        print(f"O sócio com o nome {nome_A} pertence aos dois clubes.")