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
        print("Cliente: %s, conta numero: %s, saldo %8.2f" % (self.cliente,self.numeroConta,self.saldo))

contaBanco = ContaBanco("Neri Neutzky","9745-58",500)
contaBanco.relatorio()
contaBanco.deposito(300)
contaBanco.relatorio()
contaBanco.saque(450)
contaBanco.relatorio()