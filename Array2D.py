"""Introdução aos array de 2 dimensões (matrizes)"""

import numpy as np

matriz = np.array([[1,2,3],[3,5,0]])

print(matriz)
# Primeiro elemento da matriz [l,c]

print(matriz[0,0])
# Ultimo elemento da matriz

print(matriz[1,2])
print(f"função len com matriz {len(matriz)}")
# Percorrer todos os elementos da matriz

for l in range(2):
    for c in range(3):
        print(matriz[l,c])

# Nº de colunas
print("Nº de colunas da matriz: ",matriz.shape[1])
# Nº de linhas
print("Nº de linhas da matriz: ",matriz.shape[0])
