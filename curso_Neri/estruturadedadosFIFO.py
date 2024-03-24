passageiros=["Neri","Silvino","Romilda","Lisiane","Giulia","Gustavo"]
posicaoUltimo=len(passageiros)

while True:
    print("\nTem %d passageiros na fila" % posicaoUltimo)
    print("Os passageiros na fila são: ")
    for i,num in enumerate(passageiros):
        print("Passageiros: [%d] --> %s" % (i+1,num))
    print("Digite 1 para adicionar uma pessoa na fila")
    print("Digite 2 para informar que a pessoa foi atendida (saiu da fila)")
    print("Digite 3 para encerrar")
    acao = int(input("Informe a operação (1, 2 ou 3)"))
    if acao == 1:
        pessoa=input("Digite o nome da pessoa que entrou na fila ")
        passageiros.append(pessoa)
        posicaoUltimo+=1
    elif acao == 2:
        if posicaoUltimo > 0:
            passageiros.pop(0)
            posicaoUltimo-=1
        else:
            print("A fila está vazia")
    elif acao == 3:
        print("Encerrado")
        break
    elif acao not in [1,2,3]:
        print ("\n Digite uma opção valida! \n")