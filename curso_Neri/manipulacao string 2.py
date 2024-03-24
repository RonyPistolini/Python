dados = ['andre','douglas','fernando','luiz','marcelo','pedro']
print (dados)
print ("\n".join(dados))

palavra="nerialdoirnietzke"
palavra2="Neri Aldoir Nietzke"
palavra3="                    neri aldoir nietzke                     "
print("ljust = ",palavra.ljust(20))
print("rjust = ",palavra.rjust(20))
print("partition, divide em 3 a string = ",palavra.partition("aldoir"))
print("rpartition, divide em 3 a string = ",palavra.rpartition("aldoir"))
print("split, divide em lista = ",palavra2.split(" "))
print("rsplit, divide em lista = ",palavra2.rsplit(" "))

print("startswhith retorna verdadeiro se a string inicia com a substring ",palavra2.startswith('neri'))
print("string antes do strip ","##",palavra3,"##")
print("strip elimina caracteres a esquerda e a direita de uma string ##",palavra3.strip(),"##")
print("rstrip elimina caracteres a esquerda e a direita de uma string ##",palavra3.rstrip(),"##")
print("lstrip elimina caracteres a esquerda e a direita de uma string ##",palavra3.lstrip(),"##")
print("zfill preenche a esquerda com zero (0) ","465".zfill(8))
print("swapcase - inverte caracteres maiusculo e minusculo",palavra2.swapcase())