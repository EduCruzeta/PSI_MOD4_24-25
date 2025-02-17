contar = 0
email = input("")
ps = input("")
if len(ps) >= 8:
    contar = contar + 1
if ps not in email:
    contar = contar + 1
for l in ps:
    if l >= "a" and l <= "z":
        contar = contar + 1
        break

for l in ps:
    if l >= "A" and l <= "Z":
        contar = contar + 1

for l in ps:
    if l >= "0" and l <= "9":
        contar = contar + 1

if contar == 5:
    print("palavra pass segura")
else:
    print("palavra passe nao segura")