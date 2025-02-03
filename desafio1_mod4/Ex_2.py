import numpy as np

array = np.zeros(3)

for i in range(3):
    array[i] = 3

def Soma(array):
    soma_valores = 0
    for v in array:
        soma_valores = soma_valores + v
    return soma_valores

print(Soma(array))