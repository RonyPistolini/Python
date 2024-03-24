def pesquisar(lista,codigo):
    for i,codigos in enumerate(lista):
        if codigos == codigo:
            return ("Codigo encontrado no indice ",i)
    return ("Codigo não %d encontrado" % codigo)

listaProdutos=[4,8,2,676,5,12,69]
print(pesquisar(listaProdutos,12))
print(pesquisar(listaProdutos,8))
print(pesquisar(listaProdutos,69))
print(pesquisar(listaProdutos,128))
print("-----------------------")
dicionarioCursos={
    "python": 130,
    "java":120,
    "Html":90,
    "javaScript":134
}
def pesquisaDicionario(dicionarioPesquisar,cursoPesquisar):
        if cursoPesquisar in dicionarioPesquisar:
            print("O curso %s foi localizado, o seu preço é R$ %5.2f" % cursoPesquisar, dicionarioPesquisar[cursoPesquisar])
        else:
            print("Esse cuso não foi localizado")

pesquisaDicionario(dicionarioCursos,"java")