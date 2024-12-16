"""
Programa para ler temperatura média mensal de uma cidade ao longo de um ano
O programa deve mostrar a média, a menor, a maior, a moda e os meses em que a temperatura
foi superior a média.
"""
import numpy as np

NR_MESES=12
temperaturas = np.empty(NR_MESES)

contar = 0
maior = 1
menor = 1

for i in range(len(temperaturas)):
    temperaturas[i] = int(input(f"Introduza a temperatura do {i+1} mês: "))
    contar = contar + temperaturas[i]
    if temperaturas[i] > maior:
        maior = temperaturas[i]
    elif temperaturas[i] <= menor:
        menor = temperaturas[i]

media = contar / NR_MESES

print(f"A temperatura mais elevada foi de {maior} cº e a menor temperatura foi de {menor} cº")
print(f"A temperatura média anual foi de {media}")

#mostrar mes superior a média

for mes in range(NR_MESES):
    if temperaturas[i] > media:
        print(f"A temperatura do mês {mes+1} foi de {temperaturas[i]} sendo superior à média")

# moda

moda = 0
nr_vezes_moda = 0
for mes in range(NR_MESES):
    conta = 0
    for m_atual in range(NR_MESES):
        if temperaturas[mes] == temperaturas[m_atual]: 
            conta = conta + 1
    if conta > nr_vezes_moda:   # se o conta é superior ao nr_vezes_moda este passa a ser a moda
        nr_vezes_moda = conta   # nº de vezess que a temperatura da posição mes aparece
        moda = mes              # a posição da temperatura contada
print(f"A moda é a temperatura {temperaturas[moda]} que ocorreu {nr_vezes_moda} vezes")