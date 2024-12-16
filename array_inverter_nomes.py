"""
O programa vai inverter um array com 5 elementos 1 passa a ultimo com 2 arrays
"""

import numpy as np

NR_elementos_total = 10

NR_elementos_dividido = NR_elementos_total // 2

nomes = np.empty(NR_elementos_total,dtype="U20")
nomes_invertido = np.empty(NR_elementos_total,dtype="U20")

for l in range(len(nomes)):
    nomes[l] = input("Introduza o nome: ")


for i in range(NR_elementos_dividido,-1):
    nomes_invertido = nomes[i]


print(nomes_invertido)

#######################
"""
O programa vai inverter um array com 5 elementos 1 passa a ultimo com 1 arrays
"""

NR_elementos_total = 10

NR_elementos_dividido = NR_elementos_total // 2

nomes = np.empty(NR_elementos_total,dtype="U20")

for i in range(len(nomes)):
    nomes[i] = input("Introduza o nome : ")

k = NR_elementos_total - 1

temp = ""

for i in range(NR_elementos_dividido):
    temp = nomes[i]
    nomes[i] = nomes[k]
    nomes[k] = temp
    k = k - 1

print(nomes)