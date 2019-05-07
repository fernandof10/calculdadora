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

#TODO 4: Dentro desse primeiro frame existem dois labels:
# - um com uma fonte pequena, que vai conter toda a operação realizada,
# - outro com a fonte maior, contendo somente o número digitado ou o resultado.
# Eles são dispostos um sobre o outro e também preenchem todo o espaço disponível em X.
#TODO 5: O texto em ambos os labels é ancorado do lado direito.
label_ope = Label(frame_res, text='On',  font=("Helvetica", "12"), width=largura, anchor=E)
label_ope.pack()
label_res = Label(frame_res, text='0',  font=("Helvetica", "18"), width=largura, anchor=E)
label_res.pack()

#TODO 6: Dentro do segundo frame principal estão os botões. Eles são dispostos em uma grade, como uma tabela.
b7 = Button(frame_but, text='7')
b7.grid(row=0, column=0)
b8 = Button(frame_but, text='8')
b8.grid(row=0, column=1)
b9 = Button(frame_but, text='9')
b9.grid(row=0, column=2)
bdiv = Button(frame_but, text='\u00F7')
bdiv.grid(row=0, column=3)
bac = Button(frame_but, text='AC')
bac.grid(row=0, column=4)

b4 = Button(frame_but, text='4')
b4.grid(row=1, column=0)
b5 = Button(frame_but, text='5')
b5.grid(row=1, column=1)
b6 = Button(frame_but, text='6')
b6.grid(row=1, column=2)
bmult = Button(frame_but, text='\u00D7')
bmult.grid(row=1, column=3)
bapag = Button(frame_but, text='\u2190')
bapag.grid(row=1, column=4)

b1 = Button(frame_but, text='1')
b1.grid(row=2, column=0)
b2 = Button(frame_but, text='2')
b2.grid(row=2, column=1)
b3 = Button(frame_but, text='3')
b3.grid(row=2, column=2)
bneg = Button(frame_but, text='-')
bneg.grid(row=2, column=3)
bres = Button(frame_but, text='=')
bres.grid(row=2, column=4)
b0 = Button(frame_but, text='0')
b0.grid(row=3, column=0)
bp = Button(frame_but, text='.')
bp.grid(row=3, column=2)
bm = Button(frame_but, text='+')
bm.grid(row=3, column=3)

#Exibe a janela e faz com que ela fique em loop

janela.mainloop()





#Links legais
#3 - https://www.tutorialspoint.com/python3/tk_frame.htm
#3 - https://www.tutorialspoint.com/python/tk_relief.htm
#4 - https://www.tutorialspoint.com/python3/tk_label.htm
#4 - https://www.tutorialspoint.com/python/tk_fonts.htm
#5 - https://www.tutorialspoint.com/python/tk_anchors.htm
#6 - https://www.fileformat.info/info/unicode/category/Sm/list.htm
