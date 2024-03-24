listaNomes=["Neri","Silvino","Romilda","Gustavo","Valderi","Henrique","Leonardo"]
print(listaNomes)
nomePesquisar=input("digite o nome a pesquisar: ")
encontrou=False
numeroAlunos = 0
while numeroAlunos < len(listaNomes):
    if nomePesquisar==listaNomes[numeroAlunos]:
        encontrou=True
        break
    numeroAlunos+=1
if encontrou == True:
    print("Aluno localizado")
else:
    print("Aluno não localizado")

print("\n")

for alunos in listaNomes:
    if nomePesquisar == alunos:
        print("Aluno localizado")
        break
else:
    print("Aluno não localizado")