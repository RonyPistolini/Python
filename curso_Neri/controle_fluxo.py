notaaluno=int(input("Digite a nota do aluno: "))
mediaparapassar=6
if notaaluno >= mediaparapassar:
    print("aluno aprovado")
elif notaaluno >4:
    print("aluno de recuperação")
else:
    print("aluno reprovado")