import tkinter as tk
from PIL import Image, ImageTk
from defineTroco import calculaTroco
from tkinter import messagebox

def mostrar_troco():
    texto1 = campoTexto.get()
    texto2 = campoTexto2.get()
    texto1 = trocaVirgula(texto1)
    texto2 = trocaVirgula(texto2)
    texto1Validado = remover_caracteres(texto1)
    texto2Validado = remover_caracteres(texto2)
    if texto1Validado != "" and texto2Validado != "":
        if float(texto1) > float(texto2):
            popup("O valor dado pelo cliente não cobre a conta")
        else:
            lista = (calculaTroco(texto1,texto2)) 
            exibi_imagens(lista)
    else:
        popup("Preencha os dois campos corretamente")
    
    
janela = tk.Tk()

janela.title("AuxilioPreço")
janela.geometry("630x400")
janela.configure(bg="#282A36")

# Cria uma label
label = tk.Label(janela, text="Digite o valor da conta: ", bg="#282A36", fg="white",font=("", 10, "bold"))
label.grid(row=0, column=0, padx=20, pady=10)

label2 = tk.Label(janela, text="Digite o valor entregue pelo cliente:", bg="#282A36", fg="white",font=("", 10, "bold"))
label2.grid(row=0, column=1, padx=25, pady=10)

# Cria um campo de texto
campoTexto = tk.Entry(janela)
campoTexto.grid(row=1, column=0, padx=5, pady=10)

campoTexto2 = tk.Entry(janela)
campoTexto2.grid(row=1, column=1, padx=5, pady=10)

botao = tk.Button(janela, text="TROCO",bg="#026143", fg="white", command=mostrar_troco,font=("", 14, "bold"))
botao.grid(row=1, column=2, pady=10)


def exibi_imagens(lista_imagens):

    coluna = 0
    linha = 2

    for caminho in lista_imagens:
    
        # carregar imagem    
        imagem = Image.open(caminho)  # Substitua pelo caminho da sua imagem

        imagem_redimensionada = imagem.resize((120, 60), Image.LANCZOS) #o Image.LANCZOS nao é necessario, só serve pra ajudar na qualidade da imagem

        #converte a imagem pro formato do tk
        imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)

        # label para exibir a imagem
        label_imagem = tk.Label(janela, image=imagem_tk,bg="#282A36")
        label_imagem.image = imagem_tk #nao descarta as imagens mantendo a integridade delas conforme o loop roda
        label_imagem.grid(row=linha, column=coluna, padx=5, pady=10)
        coluna = coluna + 1
        if coluna == 3:
            coluna = 0
            linha = linha + 1


def popup(mensagem):

    messagebox.showinfo("ERRO", mensagem)


def remover_caracteres(texto):
    caracteresRemovidos = "qwertyuiopasdfghjklçzxcvbnmR$"
    for char in caracteresRemovidos:
        texto = texto.replace(char, "")
    return texto

def trocaVirgula(texto):
    virgula = ","
    for char in virgula:
        texto = texto.replace(char, ".")
    return texto

janela.mainloop()