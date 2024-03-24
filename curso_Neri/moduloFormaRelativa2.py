# import moduloFormaRelativa
# print(moduloFormaRelativa.nom1)

from moduloFormaRelativa import nom1
from moduloFormaRelativa import nom2
print(nom1)
print(nom2)

from datetime import date
mesPorExtenso=["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
diaDaSemana=["segunda-feira","terça-feira","quarta-feira","quinta-feira","sexta-feira","sabado","domingo"]
hoje=date.today()
dia=hoje.day
mes=hoje.month
ano=hoje.year
rodape="Piracicaba, %d de %s de %d" % (dia,mesPorExtenso[mes],ano)
print("data de hoje: ",hoje)
print("dia: ",dia)
print("mes: ",mes)
print("ano: ",ano)
print(rodape)
print("daqui 40 dias será: ",date.fromordinal(hoje.toordinal()+40))
print("dia da semana: ",diaDaSemana[hoje.weekday()])