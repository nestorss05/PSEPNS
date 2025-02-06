from threading import Timer

Hecho = False

def funcion():
    print("Hoal (ya no puedes cancelar)")
    Hecho = True

if __name__ == '__main__':
    temporizador = Timer(5, funcion)
    temporizador.start()
    temporizador.join()
    print("Esperate chacho")
    res = input("¿Cancelas? (SI para cancelar) ").upper()
    if res == "SI" and not Hecho:
        temporizador.cancel()
        print("Pues cancelao chacho")