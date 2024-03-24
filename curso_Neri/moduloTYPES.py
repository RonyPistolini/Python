import types
def mostraTipo(dado):
    tipo = type(dado)
    if tipo == str:
        return ("String")
    elif tipo == int:
        return ("inteiro")
    elif tipo == float:
        return ("Float")
    elif tipo == bool:
        return ("Boleano")
    elif tipo == list:
        return ("lista")
    elif tipo == dict:
        return ("dicionario")
    elif tipo == types.BuiltinFunctionType:
        return ("função interna")
    elif tipo == types.FunctionType:
        return ("função")
    else:
        return(str(tipo))
    
print(mostraTipo("Rony"))
print(mostraTipo(54))
print(mostraTipo(True))
print(mostraTipo(32.4))
print(mostraTipo(["a","b","c","d","e"]))
print(mostraTipo({"Java":230,"python":530}))
print(mostraTipo(print))
print(mostraTipo(None))
