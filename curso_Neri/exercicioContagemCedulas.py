valor=float(input("Digite o valor: "))
cedulas=0
valorCedulaAtual=100
valorSerEntregue=valor
while True:
    if valorCedulaAtual <= valorSerEntregue:
        cedulas +=1
        valorSerEntregue -= valorCedulaAtual
    else:
        if cedulas > 0 and valorCedulaAtual > 1:
            print("%d cédula(s) de R$ %5.2f" % (cedulas,valorCedulaAtual))
        if cedulas > 0 and valorCedulaAtual <= 1:
            print("%d moéda(s) de R$ %5.2f" % (cedulas,valorCedulaAtual))
        if valorSerEntregue == 0:
            break
        if valorCedulaAtual == 100:
            valorCedulaAtual = 50
        elif valorCedulaAtual == 50:
            valorCedulaAtual = 20
        elif valorCedulaAtual == 20:
            valorCedulaAtual = 10
        elif valorCedulaAtual == 10:
            valorCedulaAtual = 5
        elif valorCedulaAtual == 5:
            valorCedulaAtual = 2
        elif valorCedulaAtual == 2:
            valorCedulaAtual = 1
        elif valorCedulaAtual == 1:
            valorCedulaAtual = 0.5
        elif valorCedulaAtual == 0.5:
            valorCedulaAtual = 0.25
        elif valorCedulaAtual == 0.25:
            valorCedulaAtual = 0.1
        elif valorCedulaAtual == 0.1:
            valorCedulaAtual = 0.05
        elif valorCedulaAtual == 0.05:
            valorCedulaAtual = 0.01
        elif valorCedulaAtual == 0.01:
            valorCedulaAtual = 0.00
            break
        cedulas = 0
            