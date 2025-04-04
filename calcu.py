import tkinter as tk

def fnAdicao():
    x = float(entryNumero1.get())
    y = float(entryNumero2.get())
    resultado = x + y
    lbnresultado.config(text=f'a soma é{resultado}')


def fnSubtracao():
    x = float(entryNumero1.get())
    y = float(entryNumero2.get())
    resultado = x - y
    lbnresultado.config(text=f'a soma é{resultado}')

def fnMultiplicacao():
    x = float(entryNumero1.get())
    y = float(entryNumero2.get())
    resultado = x * y
    lbnresultado.config(text=f'a soma é{resultado}')

def fnDivisao():
    x = float(entryNumero1.get())
    y = float(entryNumero2.get())
    resultado = x / y
    lbnresultado.config(text=f'a soma é{resultado}')


janela = tk.Tk() #Desenha uma janila
janela.title("expert calculadori")
janela.geometry('1920x1080')

Ibtitulo =  tk.Label(janela,
                     text= 'caltunadora',
                     font=('Old English Text MT',32),
                     fg='black',
                     bg='white',
                     width=800)


Ibtitulo.pack(padx=10,pady=10)
nine1 = tk.Label(janela,
                 text='digite um numero ',
                 font=('Old English Text MT',30))
nine1.pack(padx=10, pady=10)


entryNumero1 = tk.Entry(janela,
                        width=40,
                        font=('Old English Text MT', 20))


entryNumero1.pack(padx=5, pady=5)




nine2 = tk.Label(janela,
                 text='digite outro numero ',
                 font=('Old English Text MT',30))
nine2.pack(padx=10, pady=10)


entryNumero2 = tk.Entry(janela,
                        width=40,
                        font=('Old English Text MT',20))


entryNumero2.pack(padx=5, pady=5)

#result

lbnresultado = tk.Label(janela,
                     text='0.00',
                     font=('Old English Text MT',22))

lbnresultado.pack(padx=5,pady=5)


#add

btnAdicao =tk.Button(janela,
                     text='adicao',
                     font=('Old English Text MT',40),
                     command=fnAdicao)

btnAdicao.pack(padx=5, pady=5)

#sub

btnsubtracao =tk.Button(janela,
                     text='subtracao',
                     font=('Old English Text MT',40),
                     command=fnSubtracao)

btnsubtracao.pack(padx=5, pady=5)

#multi

btnMuiltiplicaçao =tk.Button(janela,
                     text='multiplicacao',
                     font=('Old English Text MT',40),
                     command=fnMultiplicacao)

btnMuiltiplicaçao.pack(padx=5, pady=5)

#divisao

btnDivizao =tk.Button(janela,
                     text='divisao',
                     font=('Old English Text MT',40),
                     command=fnDivisao)
btnDivizao.pack(padx=10, pady=10)




janela.mainloop()