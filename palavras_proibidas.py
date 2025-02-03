"""O programa vai ler a frase do utilizador e vai substituir palarvas proibidas"""

import numpy as np

proibidas = np.array(["mau","pobre","infeliz","péssimo","horrivel","feio"])
alternativa = np.array(["bom","rico","feliz","otimo","incrivel","bonito"])

frase = input("Insira a frase: ")

for i in range (len(proibidas)):
    if proibidas[i] in frase:
        frase = frase.replace(proibidas[i],alternativa[i])

print(frase)
        