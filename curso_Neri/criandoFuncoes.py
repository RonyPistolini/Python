print("Sem usar funções. A soma é: ",(5+6))
# sem return
def soma(num1, num2):
    print("Usando funções (DEF), a soma é ", (num1+num2))
def subtracao(num1, num2):
    print("Usando funções (DEF), a subtracao é ", (num1-num2))
def multiplicacao(num1, num2):
    print("Usando funções (DEF), a multiplicacao é ", (num1*num2))
def divisao(num1, num2):
    print("Usando funções (DEF), a divisao é ", (num1/num2))

soma(15,64)
subtracao(50,20)
multiplicacao(4,6)
divisao(50,5)

#com return
def somaR(num1, num2):
    return(num1+num2)
def subtracaoR(num1, num2):
    return(num1-num2)
def multiplicacaoR(num1, num2):
    return(num1*num2)
def divisaoR(num1, num2):
    return(num1/num2)
print("--------------------------")
print("Usando funções (DEF) com return, a soma é ", somaR(10,4))
print("Usando funções (DEF) com return, a subtracao é ", subtracaoR(10,4))
print("Usando funções (DEF) com return, a multiplicacao é ", multiplicacaoR(10,4))
print("Usando funções (DEF) com return, a divisao é ", divisaoR(10,4))

print("--------------------------")
def numeroPar(numero):
    if (numero%2 == 0):
        return("Par")
    else:
        return("Impar")
numero = int(input("Digite um numero inteiro: "))
print("O numeor é ", numeroPar(numero))