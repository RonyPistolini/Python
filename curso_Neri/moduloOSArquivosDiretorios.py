import os

print(os.listdir(".")) #mostra arquivos e pastas no diretorio atual
print("\n")
print(os.listdir(".vscode")) #mostra arquivos e pastas no diretorio ".vscode"
print("\n")
# os.mkdir("videoaulapython") #cria um novo diretorio
print(os.getcwd()) # mostra o diretorio atual
print("\n")
os.chdir("videoaulapython") # entra no diretorio "videoaulapython"
print(os.getcwd()) # mostra o diretorio atual
print("\n")
print(os.listdir(".")) #mostra arquivos e pastas no diretorio atual
open("arquivo.txt","w").close()
# os.makedirs("primeiraPasta/SegundaPasta/terceiraPasta") #cria pastas/diretorios e subpastas/subdiretorios
#os.rename("primeiraPasta","primeiroDiretorio") #renomeia uma pasta/diretorio
#os.mkdir("pastaTeste") #cria o diretorio pastaTeste
#os.rmdir("pastaTeste") # remove a o diretorio pastaTeste
# os.remove("arquivo.txt") # remove arquivos
#os.chdir("..") #retorna para o diretorio anterior
print(os.getcwd()) # mostra o diretorio atual
os.chdir("../.vscode") #retorna para o diretorio anterior e ja entra em outro diretorio
print(os.getcwd()) # mostra o diretorio atual
os.chdir("..") #retorna para o diretorio anterior
for arquivoPasta in os.listdir("."):
    print(arquivoPasta)