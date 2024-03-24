
dicionarioCursos={
    "python": [130,"basico","desktop"],
    "java":[120,"intermediario","desktop"],
    "Html":[90,"avançado","desktop"],
    "arduino":[170,"avançado","robotica"],
    "javaScript":[134,"intermediario","desktop"]
}
for chave, informacoes in dicionarioCursos.items():
    print("Cursos: ",chave)
    print("Valor: %5.2f" % informacoes[0])
    print("Nivel: ",informacoes[1])
    print("Observação: ",informacoes[2])
    print("------------------------------")

print("usando o get ",dicionarioCursos.get("java"))
print("usando o setdefault ",dicionarioCursos.setdefault("java"))

copiaDicionarioCursos=dicionarioCursos.copy()

print(dicionarioCursos)
dicionarioCursos.clear()
print(dicionarioCursos)
print(copiaDicionarioCursos)