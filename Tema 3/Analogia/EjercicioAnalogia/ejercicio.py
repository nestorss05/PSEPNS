import threading
import time

def proc1():
    print("Preparando er cafe")
    time.sleep(3)
    print("LITTO")

def proc2():
    print("Preparando er pan")
    time.sleep(2)
    print("LITTO")

def proc3():
    print("Preparando la wea gabacha")
    time.sleep(4)
    print("LITTO")

if __name__ == "__main__":
    hilos = []
    # Seran 5 clientes
    for _ in range(5):
        hilos.append(threading.Thread(target=proc1))
        hilos.append(threading.Thread(target=proc2))
        hilos.append(threading.Thread(target=proc3))

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("FINIQUITAO")