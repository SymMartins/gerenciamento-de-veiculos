from tkinter import *
from tkinter import ttk


def barra_progresso(m):
    cont = 0
    etapas = m/100
    while cont < etapas:
        cont += 1
        i = 0
        while i < 1000000:
            i += 1
        varBarra.set(cont)
        janela.update()

janela = Tk()
janela.geometry('800x600')
janela.title('Gerenciamento de Veículos')
janela_bemvindo = Label(janela, text='Bem vindo ao programa de\nGerenciamento de Veículos')
janela_bemvindo.place(x=300, y=15) #width=200, height=300)
varBarra = DoubleVar()
varBarra.set(0)
pb = ttk.Progressbar(janela, variable=varBarra, maximum=100)
pb.place(x=150, y=500, width=500, height=40)
barra_carregando = Label(command=barra_progresso(10000))
janela.mainloop()