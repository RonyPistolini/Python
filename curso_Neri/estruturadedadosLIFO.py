panqueca=["Panqueca1","Panqueca2","Panqueca3","Panqueca4","Panqueca5","Panqueca6"]
posicaoUltimo=len(panqueca)
qtdadepanqueca=len(panqueca)
while True:
    print("\nTem %d panquecas na pilha" % posicaoUltimo)
    print("As panquecas na fila são: ")
    for i,num in enumerate(panqueca):
        print("Panqueca: [%d] --> %s" % (i+1,num))
    print("Digite 1 para adicionar uma nova panqueca na pilha")
    print("Digite 2 para informar que a panqueca foi atendida (saiu da pilha)")
    print("Digite 3 para encerrar")
    acao = int(input("Informe a operação (1, 2 ou 3)"))
    if acao == 1:
        qtdadepanqueca+=1
        panqueca.append("panqueca%d" % qtdadepanqueca)
        posicaoUltimo+=1        
    elif acao == 2:
        if posicaoUltimo > 0:
            panqueca.pop(-1)
            posicaoUltimo-=1
        else:
            print("A pilha está vazia")
    elif acao == 3:
        print("Encerrado")
        break
    elif acao not in [1,2,3]:
        print ("\n Digite uma opção valida! \n")