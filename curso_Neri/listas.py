alfabeto=["a","b","c"]
alfabeto += "defg"
print (alfabeto)
alfabeto.extend("hijkl")
print (alfabeto)
alfabeto += ["mnop"]
print (alfabeto)
del alfabeto[0]
print (alfabeto)
del alfabeto[-1]
print (alfabeto)
alfabeto.remove("h")
print (alfabeto)
del alfabeto[2:4]
print (alfabeto)

print('\n')
listaNomes=["Neri","Silvino","Romilda","Gustavo"]
print(listaNomes)
listaNomes.append("Valderi")
print(listaNomes)
listaNomes.insert(1,"Henrique")
print(listaNomes)
listaNomes.insert(0,"Leonardo")
print(listaNomes)
listaNomes.insert(-1,"Joao")
print(listaNomes)
listaNomes.pop()
print(listaNomes)

print('\n')
listaCursos=["Python","Java","C++","PHP","Android","Python","Java","C++","PHP","Delphi","html"]
print(listaCursos.count("Java"))
print(listaCursos)
listaCursos.reverse()
print(listaCursos)
print(listaCursos.index("PHP"))
# listaCursos.sort()
print(listaCursos)
for cursosLista in listaCursos:
    print(cursosLista)
print('\n')
for i, cursosLista in enumerate (listaCursos):
    print(cursosLista)

listaFamilia=[]
while True:
    pessoaFamilia=input("Digite uma pessoa da sua familia (sair para encerrar): ")
    if pessoaFamilia == "sair":
        print ("saiu")
        break
    listaFamilia.append(pessoaFamilia)
for a in listaFamilia:
    print (a)
