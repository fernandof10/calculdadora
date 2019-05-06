# 0 - Importe o Tkinter
from tkinter import *


#TODO 1: Crie uma janela, com o nome Calculadora
janela = Tk()
janela.title("Calculadora")

largura = 350
altura = 250
tamanho = '{}x{}'.format(largura, altura)
janela.geometry(tamanho)

#TODO 2: Crie 2 frames. 1, que contem o resultado e o outro com os botões.
#TODO 3: O primeiro frame ocupa todo o espaço disponível em X e tem uma borda do tipo afundada
frame_res = Frame(janela, relief=SUNKEN,  width=largura)
frame_res.pack()
frame_but = Frame(janela, width=largura)
frame_but.pack()

#Exibe a janela e faz com que ela fique em loop
janela.mainloop()





#Links legais
#https://www.tutorialspoint.com/python3/tk_frame.htm
#https://www.tutorialspoint.com/python/tk_relief.htm