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
frame_res = Frame(janela, relief=SUNKEN, width=largura)
frame_res.pack()
frame_but = Frame(janela, width=largura)
frame_but.pack()

#TODO 4: Dentro desse primeiro frame existem dois labels:
# - um com uma fonte pequena, que vai conter toda a operação realizada,
# - outro com a fonte maior, contendo somente o número digitado ou o resultado.
# Eles são dispostos um sobre o outro e também preenchem todo o espaço disponível em X.
#TODO 5: O texto em ambos os labels é ancorado do lado direito.

#TODO 7: Crie 2 variáveis globais do tipo string para os labels de resultado e operações.Vamos usar essas variáveis junto com os labels, assim, sempre que as alteramos, os textos nos labels também mudarão
str_resultado = StringVar()
str_operacao = StringVar()
str_resultado.set('')
str_operacao.set('')
label_ope = Label(frame_res, textvariable=str_operacao,  font=("Helvetica", "12"), width=largura, anchor=E)
label_ope.pack()
label_res = Label(frame_res, textvariable=str_resultado,  font=("Helvetica", "18"), width=largura, anchor=E)
label_res.pack()

#TODO 6: Dentro do segundo frame principal estão os botões. Eles são dispostos em uma grade, como uma tabela.
#TODO 6.1: Configuramos o tamanho dos botões e a font
#TODO 8: Crie funções para os botões
def clk_0():
    str_resultado.set(str_resultado.get() + '0')

def clk_1():
    str_resultado.set(str_resultado.get() + '1')

def clk_2():
    str_resultado.set(str_resultado.get() + '2')

def clk_3():
    str_resultado.set(str_resultado.get() + '3')

def clk_4():
    str_resultado.set(str_resultado.get() + '4')

def clk_5():
    str_resultado.set(str_resultado.get() + '5')

def clk_6():
    str_resultado.set(str_resultado.get() + '6')

def clk_7():
    str_resultado.set(str_resultado.get() + '7')
    print(str_resultado.get())

def clk_8():
    str_resultado.set(str_resultado.get() + '8')

def clk_9():
    str_resultado.set(str_resultado.get() + '9')

def clk_p():
    str_resultado.set(str_resultado.get() + '.')

def clk_mais():
    str_operacao.set(str_operacao.get() + str_resultado.get())
    str_resultado.set('+')

def clk_menos():
    str_operacao.set(str_operacao.get() + str_resultado.get())
    str_resultado.set('-')

def clk_mult():
    str_operacao.set(str_operacao.get() + str_resultado.get())
    str_resultado.set('*')

def clk_div():
    str_operacao.set(str_operacao.get() + str_resultado.get())
    str_resultado.set('/')

def clk_ac():
    str_resultado.set('')
    str_operacao.set('')

def clk_apag():
    str_resultado.set(str_resultado.get()[:-1])

def clk_res():
    str_resultado.set(eval(str_operacao.get() + str_resultado.get()))
    str_operacao.set('')



b7 = Button(frame_but, text='7',font=("Helvetica", "18"),  height=1, width=4, command=clk_7)
b7.grid(row=0, column=0)
b8 = Button(frame_but, text='8',font=("Helvetica", "18"),  height=1, width=4, command=clk_8)
b8.grid(row=0, column=1)
b9 = Button(frame_but, text='9',font=("Helvetica", "18"),  height=1, width=4, command=clk_9)
b9.grid(row=0, column=2)
bdiv = Button(frame_but, text='\u00F7',font=("Helvetica", "18"),  height=1, width=4, command=clk_div)
bdiv.grid(row=0, column=3)
bac = Button(frame_but, text='AC',font=("Helvetica", "18"),  height=1, width=4, command=clk_ac)
bac.grid(row=0, column=4)

b4 = Button(frame_but, text='4',font=("Helvetica", "18"), height=1, width=4, command=clk_4)
b4.grid(row=1, column=0)
b5 = Button(frame_but, text='5',font=("Helvetica", "18"), height=1, width=4, command=clk_5)
b5.grid(row=1, column=1)
b6 = Button(frame_but, text='6',font=("Helvetica", "18"),  height=1, width=4, command=clk_6)
b6.grid(row=1, column=2)
bmult = Button(frame_but, text='\u00D7',font=("Helvetica", "18"), height=1, width=4, command=clk_mult)
bmult.grid(row=1, column=3)
bapag = Button(frame_but, text='\u2190',font=("Helvetica", "18"),  height=1, width=4, command=clk_apag)
bapag.grid(row=1, column=4)

b1 = Button(frame_but, text='1',font=("Helvetica", "18"),  height=1, width=4, command=clk_1)
b1.grid(row=2, column=0)
b2 = Button(frame_but, text='2',font=("Helvetica", "18"),  height=1, width=4, command=clk_2)
b2.grid(row=2, column=1)
b3 = Button(frame_but, text='3',font=("Helvetica", "18"),  height=1, width=4, command=clk_3)
b3.grid(row=2, column=2)
bneg = Button(frame_but, text='-',font=("Helvetica", "18"),  height=1, width=4, command=clk_menos)
bneg.grid(row=2, column=3)
bres = Button(frame_but, text='=',font=("Helvetica", "18"),  height=1, width=4, command=clk_res)
bres.grid(row=2, column=4, rowspan = 2,sticky = N+S)

b0 = Button(frame_but, text='0',font=("Helvetica", "18"),  height=1, width=4, command=clk_0)
b0.grid(row=3, column=0, columnspan = 2, sticky = W+E)
bp = Button(frame_but, text='.',font=("Helvetica", "18"),  height=1, width=4, command=clk_p)
bp.grid(row=3, column=2)
bm = Button(frame_but, text='+',font=("Helvetica", "18"),  height=1, width=4, command=clk_mais)
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
#6 - https://www.tutorialspoint.com/python/tk_button.htm
#6.1 https://effbot.org/tkinterbook/grid.htm
#6.1 https://www.tutorialspoint.com/python/tk_grid.htm
