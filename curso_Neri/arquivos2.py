arquivo=open("texto.txt","w")
arquivo.write("#lista de pessoas da texto do Neri: \n")
arquivo.write("*Neri\n")
arquivo.write("*Liziane\n")
arquivo.write("*Giulia\n")
arquivo.write("*Gustavo\n")
arquivo.flush()
arquivo.close()

arquivo=open("texto.txt","r")
for linha in arquivo.readlines():
    if linha[0]=="#":
        print(linha.center(100))
        print(linha[1:].center(100))
    if linha[0]=="*":
        print(linha[1:].rjust(100))




arquivo.close()