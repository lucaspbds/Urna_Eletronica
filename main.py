from tkinter import *
from operator import itemgetter
from tkinter import ttk
from pygame import mixer, USEREVENT

# Fazer o visor mostrar os números que o usuário está digitando
# Contabilizar os votos (apuração dos votos)
# Mostrar o raking ou quem ganhou a eleição e se teve empate mostrar.
"""Criar uma lista para receber os números dos candidados para poder verificar se é um novo candidado ou não.
Se for um candidato novo, vai ser colocado na lista e no dicionário com o contador. Se não for um novo candidato,
vai ser só somado +1 no contador.
eleicao = {}
candidatos = []
Vamos usar essa estratégia para apurar os votos: https://www.youtube.com/watch?v=cwrqIztaAwk
"""
# - Digitar uma senha para desbloquear isso!
eleicao = dict()
candidatos = list()
ranking = dict()
sound = 'efeito_sonoro/urna_eletronica.mp3'
buttonfont = 'Arial 15 bold'
buttonBackground = 'black'
buttonForeground = 'white'
buttonWidth = 5
buttonHeight = 2
password = '26102006'

window = Tk()
window.title("Urna Eletrônica")
window.geometry("940x470")

valorTexto = StringVar()
numbers = ''


# Functions

def som():
    mixer.init()
    mixer.music.load(sound)
    mixer.music.play()
    mixer.music.set_endevent(USEREVENT)


def exibir(num):
    global numbers
    numbers = numbers + num
    valorTexto.set(numbers)


def limpar():
    global numbers
    numbers = ''
    valorTexto.set('')


def apuracao():
    ranking = sorted(eleicao.items(), key=itemgetter(1), reverse=True)
    window.destroy()
    resultado = Tk()
    resultado.title("Resultado da eleição")
    columns = ('Nº do Candidato', 'Quantidade de votos')
    tree = ttk.Treeview(resultado, columns=columns, show='headings')
    tree.heading('Nº do Candidato', text='Nº do Candidato')
    tree.heading('Quantidade de votos', text='Quantidade de votos')
    tree.grid(row=0, column=0)
    for candidato in ranking:
        tree.insert('', END, values=candidato)
    resultado.mainloop()


def confirmarVoto():
    global numeroCandidato
    numeroCandidato = valorTexto.get()
    limpar()
    if numeroCandidato == password:
        apuracao()

    else:
        som()
        if numeroCandidato not in candidatos:
            candidatos.append(numeroCandidato)
            if numeroCandidato == '':
                eleicao['branco'] = 1
            else:
                eleicao[f"{numeroCandidato}"] = 1
        else:
            if numeroCandidato == '':
                eleicao['branco'] += 1
            else:
                eleicao[f"{numeroCandidato}"] += 1


# Frames
frameTela = Frame(window,
                  background='gray',
                  width=450,
                  height=425)
frameTeclado = Frame(window,
                     background='#101010',
                     width=380,
                     height=425)
frameTeclas = Frame(frameTeclado,
                    background='#101010',
                    width=250,
                    height=300)
frameTela.place(x=25, y=20)
frameTeclado.place(x=500, y=20)
frameTeclas.place(x=65, y=20)

# Tela

visor = Label(frameTela,
              textvariable=valorTexto,
              font='Arial 55 bold',
              background='gray',
              foreground='white',
              width=10,
              height=5,
              border=0,
              relief=FLAT)
visor.place(x=0, y=0)
# Buttons
bt_1 = Button(frameTeclas,
              font=buttonfont,
              text='1',
              bd=0,
              background=buttonBackground,
              foreground=buttonForeground,
              width=buttonWidth,
              height=buttonHeight,
              relief=RAISED,
              overrelief=RIDGE,
              command=lambda: exibir('1'))
bt_1.place(x=0, y=0)
bt_2 = Button(frameTeclas,
              font=buttonfont,
              text='2',
              bd=0,
              background=buttonBackground,
              foreground=buttonForeground,
              width=buttonWidth,
              height=buttonHeight,
              relief=RAISED,
              overrelief=RIDGE,
              command=lambda: exibir('2'))
bt_2.place(x=92, y=0)
bt_3 = Button(frameTeclas,
              font=buttonfont,
              text='3',
              bd=0,
              background=buttonBackground,
              foreground=buttonForeground,
              width=buttonWidth,
              height=buttonHeight,
              relief=RAISED,
              overrelief=RIDGE,
              command=lambda: exibir('3'))
bt_3.place(x=184, y=0)
bt_4 = Button(frameTeclas,
              font=buttonfont,
              text='4',
              bd=0,
              background=buttonBackground,
              foreground=buttonForeground,
              width=buttonWidth,
              height=buttonHeight,
              relief=RAISED,
              overrelief=RIDGE,
              command=lambda: exibir('4'))
bt_4.place(x=0, y=80)
bt_5 = Button(frameTeclas,
              font=buttonfont,
              text='5',
              bd=0,
              background=buttonBackground,
              foreground=buttonForeground,
              width=buttonWidth,
              height=buttonHeight,
              relief=RAISED,
              overrelief=RIDGE,
              command=lambda: exibir('5'))
bt_5.place(x=92, y=80)
bt_6 = Button(frameTeclas,
              font=buttonfont,
              text='6',
              bd=0,
              background=buttonBackground,
              foreground=buttonForeground,
              width=buttonWidth,
              height=buttonHeight,
              relief=RAISED,
              overrelief=RIDGE,
              command=lambda: exibir('6'))
bt_6.place(x=184, y=80)
bt_7 = Button(frameTeclas,
              font=buttonfont,
              text='7',
              bd=0,
              background=buttonBackground,
              foreground=buttonForeground,
              width=buttonWidth,
              height=buttonHeight,
              relief=RAISED,
              overrelief=RIDGE,
              command=lambda: exibir('7'))
bt_7.place(x=0, y=160)
bt_8 = Button(frameTeclas,
              font=buttonfont,
              text='8',
              bd=0,
              background=buttonBackground,
              foreground=buttonForeground,
              width=buttonWidth,
              height=buttonHeight,
              relief=RAISED,
              overrelief=RIDGE,
              command=lambda: exibir('8'))
bt_8.place(x=92, y=160)
bt_9 = Button(frameTeclas,
              font=buttonfont,
              text='9',
              bd=0,
              background=buttonBackground,
              foreground=buttonForeground,
              width=buttonWidth,
              height=buttonHeight,
              relief=RAISED,
              overrelief=RIDGE,
              command=lambda: exibir('9'))
bt_9.place(x=184, y=160)
bt_0 = Button(frameTeclas,
              font=buttonfont,
              text='0',
              bd=0,
              background=buttonBackground,
              foreground=buttonForeground,
              width=buttonWidth,
              height=buttonHeight,
              relief=RAISED,
              overrelief=RIDGE,
              command=lambda: exibir('0'))
bt_0.place(x=92, y=240)
branco = Button(frameTeclado,
                font='Arial 12 bold',
                text='BRANCO',
                bd=0,
                background='white',
                foreground='black',
                width=9,
                height=2,
                relief=RAISED,
                overrelief=RIDGE,
                command=lambda: confirmarVoto())
branco.place(x=16, y=350)
corrigir = Button(frameTeclado,
                  font='Arial 12 bold',
                  text='CORRIGIR',
                  bd=0,
                  background='#fca61d',
                  foreground='black',
                  width=9,
                  height=2,
                  relief=RAISED,
                  overrelief=RIDGE,
                  command=lambda: limpar())
corrigir.place(x=134, y=350)
confirmar = Button(frameTeclado,
                   font='Arial 12 bold',
                   text='CONFIRMAR',
                   bd=0,
                   background='green',
                   foreground='black',
                   width=11,
                   height=2,
                   relief=RAISED,
                   overrelief=RIDGE,
                   command=lambda: confirmarVoto())
confirmar.place(x=250, y=350)

window.mainloop()
