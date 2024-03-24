print("Sem usar funções. A soma é: ",(5+6))
def soma(num1, num2):
    print("Usando funções (DEF), a soma é ", (num1+num2))


def somarLista(lista):
    totalSoma=0
    for numeroLista in lista:
        totalSoma += numeroLista
    return totalSoma

def mediaLista(lista):
    return (somarLista(lista)/len(lista))


listaNumeros=[5,8,6,3,7,9,2,4,3]
print("A soma da lista é ",somarLista(listaNumeros))
print("A media da lista é %5.2f" % mediaLista(listaNumeros))

