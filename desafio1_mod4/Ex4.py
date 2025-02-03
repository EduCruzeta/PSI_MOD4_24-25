
def Contar(nomes,nome):
    contar = 0
    for v in nomes:
        if v == nome:
            contar = contar + 1
    return contar

def ContarV2(nomes,nome):
    contar = 0
    for p in range (len(nomes)):
        if nomes[p] == nome:
            contar = contar + 1
    return contar

