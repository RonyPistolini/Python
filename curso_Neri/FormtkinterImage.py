from tkinter import *
from PIL import Image, ImageTk

# Função para exibir a imagem
def exibir_imagem():
    imagem = Image.open("imagem.jpg")
    imagem = ImageTk.PhotoImage(imagem)
    label_imagem.configure(image=imagem)
    label_imagem.image = imagem  # Manter uma referência para evitar a coleta de lixo

# Criar a janela principal
root = Tk()
root.title("Exibição de Imagem")

# Criar um rótulo para a imagem
label_imagem = Label(root)
label_imagem.pack()

# Botão para exibir a imagem
botao_exibir = Button(root, text="Exibir Imagem", command=exibir_imagem)
botao_exibir.pack()

# Iniciar o loop principal da interface gráfica
root.mainloop()
