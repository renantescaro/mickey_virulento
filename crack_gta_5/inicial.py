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

def infectarPc():
    dir = os.path.dirname(os.path.realpath(__file__))

t = threading.Thread(target=msgInstalacao)
t.start()

while t.isAlive():
    infectarPc()



