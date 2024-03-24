for numeros in "0123456789":
    print(numeros)
else:
    print("fim")

for numeros2 in range (20):
    print(numeros2)
    if numeros2 > 5:
        break
else:
    print("fim")

for nomes in ['rony','mauricio','derli','joao','luiz']:
    print(nomes)
else:
    print("fim")

dadostupla = [('a','b'),('c','d'),('e','f')]
for (alf1,alf2) in dadostupla:
    print(alf1)
    print(alf2)
    print(alf1,alf2)

for numeros2 in range (20, 40, 4):
    print(numeros2)
    if numeros2 > 35:
        break
else:
    print("fim")

for numeros3 in range (10, 20):
    if numeros3 == 15:
        continue
    print(numeros3)
else:
    print("fim")

for tabuada in range (1,11):
    print (tabuada, ' x 4 = ', tabuada*4)
