def validar(pergunta, notaMin, notaMax):
    while True:
        nota=int(input(pergunta))
        if nota < notaMin or nota > notaMax:
            print("Atenção, a nota %d é invalida, tem que ser entre %d e %d" % (nota, notaMin, notaMax))
        else:
            print("Nota valida")
            return True

validar("Digite a nota do aluno: ", 2, 8)