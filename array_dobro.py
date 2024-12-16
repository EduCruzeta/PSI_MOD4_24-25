"""Este programa vai preencher um array com o dobro do indice do mesmo"""
import numpy as np

numeros =  np.zeros(10)

for i in range(10):
    numeros[i] = i * 2

print(numeros)