from multiprocessing import Pipe, Process
from random import *

def generaIPs(t1Left):
    for i in range(0,10):
        num1 = randint(0,255)
        num2 = randint(0, 255)
        num3 = randint(0, 255)
        num4 = randint(0, 255)

        ip = f"{num1}.{num2}.{num3}.{num4}"
        t1Left.send(ip)
    t1Left.send(None)

def clasificaIPs(t1Right, t2Left):
    for _ in range(0,10):
        ip = t1Right.recv()
        octetos = ip.split(".")
        primero = int(octetos[0])

        if 0 <= primero <= 223:
            t2Left.send(ip)
    t2Left.send(None)

def pintarIPs(t2Right):
    ip = t2Right.recv()
    while ip is not None:
        octetos = ip.split(".")
        primero = int(octetos[0])
        if primero <= 127:
            print(ip, 'Clase A')
        elif primero <= 191:
            print(ip, 'Clase B')
        else:
            print(ip, 'Clase C')
        ip = t2Right.recv()

if __name__ == '__main__':
    t1Left, t1Right = Pipe()
    t2Left, t2Right = Pipe()
    proceso1 = Process(target=generaIPs, args=(t1Left, ))
    proceso2 = Process(target=clasificaIPs, args=(t1Right, t2Left))
    proceso3 = Process(target=pintarIPs, args=(t2Right, ))
    proceso1.start()
    proceso2.start()
    proceso3.start()
    proceso1.join()
    proceso2.join()
    proceso3.join()