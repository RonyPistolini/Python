class Carros:
    def __init__(self):
        self.marca="Ferrari"
        self.cor="Vermelho"

carro = Carros() #instanciando
print (carro.marca)
print (carro.cor)

carro.marca="Chevrolet"
carro.cor="Preta"
print (carro.marca)
print (carro.cor)

# criando classe com parametros
class Carros1:
    def __init__(self,pmarca,pcor):
        self.marca=pmarca
        self.cor=pcor
carro1 = Carros1("mustang","Amarelo") #instanciando
print (carro1.marca)
print (carro1.cor)

