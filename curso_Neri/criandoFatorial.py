numeroDigitado = int(input("Digite um Numero inteiro: "))
def fatorial (numero):
    f=1
    while numero > 1:
        f*=numero
        numero -= 1
    return f
print("O fatorial do %d é %d"%(numeroDigitado,fatorial(numeroDigitado)))

numeroDigitado = int(input("Digite um Numero inteiro: "))
i=0
numero = numeroDigitado
while i <=numero:
    def fibonacci(i):
        if i <= 1:
            return i
        else:
            return fibonacci(i-1)+fibonacci(i-2)
    print("retorna o %d numero da sequencia de fibonacci: %d" % (i,fibonacci(i)))
    i +=1