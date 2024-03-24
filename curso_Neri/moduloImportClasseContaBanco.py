class ContaBanco:
    def __init__(self,cliente,numeroConta,saldo=0):
        self.saldo=saldo
        self.cliente=cliente
        self.numeroConta=numeroConta
    def deposito(self,valor):
        self.saldo += valor
    def saque(self,valor):
        self.saldo -= valor
    def relatorio(self):
        print("Cliente: %s, conta numero: %s, slado %8.2f" % (self.cliente,self.numeroConta,self.saldo))