dicionarioNomes={1:"rony",
                 2:"Giovanna",
                 3:"Claudete"}
print(dicionarioNomes)
print(dicionarioNomes.keys())
print(dicionarioNomes.values())
print(dicionarioNomes[1])
dicionarioCursos={
    "python": 130,
    "java":120,
    "Html":90,
    "javaScript":134
}
print("\n")
print(dicionarioCursos)
print(dicionarioCursos.keys())
print(dicionarioCursos.values())
print(dicionarioCursos["python"])
dicionarioCursos["android"]=146

print("java" in  dicionarioCursos)
while True:
    nomePesquisar=input("Digite um nome de curso a ser pesquisado (ou fim para sair): ")
    if nomePesquisar == "fim":
        print("Pesquisa finalizada!")
        break
    if nomePesquisar in dicionarioCursos:
        print("Esse curso foi localizado")
    else:
        print("Esse cuso não foi localizado")