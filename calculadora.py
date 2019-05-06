# 0 - Importe o Tkinter
from tkinter import *


#TODO:1 - Crie uma janela, com o nome Calculadora
janela = Tk()
janela.title("Calculadora")

largura = 350
altura = 250
tamanho = '{}x{}'.format(largura, altura)
janela.geometry(tamanho)

#Exibe a janela e faz com que ela fique em loop
janela.mainloop()
