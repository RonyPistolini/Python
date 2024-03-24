assentosVagos=[8,7,0,24,11,60]
quantidadeRotas=len(assentosVagos)
for rota,assentosDisponiveis in enumerate(assentosVagos):
    print("Rota %d possui %d assentos disponíveis" % (rota+1,assentosDisponiveis))
while True:
    rotaEscolhida=int(input("Escolha uma rota de 1 a %d (para sair digite 0)" % quantidadeRotas))
    if rotaEscolhida == 0:
        print("Sistema finalizado ........ até logo!!!")
        break
    if rotaEscolhida > quantidadeRotas or rotaEscolhida < 1:
        print("Rota invalida!")
    elif assentosVagos[rotaEscolhida-1] == 0:
        print("Rota com vagas indisponíveis")
    else:
        quantidadePassagens=int(input("Quantas passagens deseja comprar ?"))
        if quantidadePassagens > assentosVagos[rotaEscolhida-1]:
            print("Você escolheu uma quantidade de passagens maior do que o disponível!")
        elif quantidadePassagens <1:            
            print("Escolheu uma quantidade de passagens maior do que zero!")
        else:
            assentosVagos[rotaEscolhida-1] -= quantidadePassagens            
            print("\nCompra realizada com sucesso!\n")
            for rota,assentosDisponiveis in enumerate(assentosVagos):
                print("Rota %d possui %d assentos disponíveis" % (rota+1,assentosDisponiveis))

