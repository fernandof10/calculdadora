# 0 - Importe o Tkinter
from tkinter import *


#TODO:1 - Crie uma janela, com o nome Calculadora
janela = Tk()
janela.title("Calculadora")

largura = 350
altura = 250
tamanho = '{}x{}'.format(largura, altura)
janela.geometry(tamanho)

#TODO:2 - Crie 2 frames. 1, que contem o resultado e o outro com os botões.
frame_res = Frame(janela)
frame_res.pack()
frame_but = Frame(janela)
frame_but.pack()

#Exibe a janela e faz com que ela fique em loop
janela.mainloop()
