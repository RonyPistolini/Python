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

#herança
class ContaEspecial(ContaBanco):
    def __init__(self,cliente,numeroConta,saldo=0,limite=0):
        ContaBanco.__init__(self,cliente,numeroConta,saldo)
        self.limite = limite
    def saque(self,valor):
        self.saldo += conta1.limite
        self.saldo -= valor
    def relatorio(self):
        print("Cliente: %s, conta numero: %s, saldo %8.2f, com o limite de %8.2f" % (self.cliente,self.numeroConta,self.saldo,self.limite))

conta1 = ContaEspecial("Neri","43394334-3",1000,2000)
conta1.relatorio()
conta1.deposito(300)
conta1.relatorio()
conta1.saque(450)
conta1.relatorio()