temperaturas=[40,33,20,10,-3,2,9,5,6,20,-5,31]
maior=temperaturas[0]
for listaTemperaturas in temperaturas:
    if listaTemperaturas > maior:
        maior = listaTemperaturas
print("A maior temperatura registrada foi : ",maior)
print("\n")
menor=temperaturas[0]
for listaTemperaturas in temperaturas:
    if listaTemperaturas < menor:
        menor = listaTemperaturas
print("A menor temperatura registrada foi : ",menor)