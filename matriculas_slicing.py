"""Programaa para registar as matriculas e o tempo(segundos) de utilização de um estacionamento.
O programa deve ler uma linha com as matriculas separadas por , e os tempos em segundos separados por ,

p.ex.:
    00-00-oo, AB-CD-33, 33-44-ZY   (strings)
    120, 535, 10333                (segundos)
No máximo o programa deve permitir 10 matriculas/tempos"""


import numpy as np

matriculas = np.empty(10,dtype="U20")
matriculas = np.zeros(10)

print(matriculas)

matriculas = input("Insira as matriculas dos carros separadas por virgulas: ")