numeros=[40,33,20,10,3,2,9,5,6,20,5,31]
for verificaNumero in numeros:
    if int(verificaNumero)%2 == 0:
        print("O numero: ",verificaNumero," é par com o resto: ",int(verificaNumero)%2,"\n")
    else:
        print("O numero: ",verificaNumero," é impar com o resto: ",int(verificaNumero)%2,"\n")

print('\n')

i=0
for num in numeros:
    print("sem enumerate: [%d] --> %d" %(i,num))
    i+=1

print('\n')

for i,num in enumerate(numeros):
    print("com enumerate: [%d] --> %d" %(i,num))