#coding: latin1
from multiprocessing import Process, Pipe
import datetime

def proceso1(fichero, anio, pipe):
    with open(fichero, "r", encoding="utf-8") as archivo:
        sender = ""
        for linea in archivo:
            pelicula, anioPeli = linea.split(";")
            anioPeli = int(anioPeli)
            if anioPeli == anio:
                sender += f"{linea}"
        pipe.send(sender)

def proceso2(pipe, anio):
    datos = pipe.recv()
    with open(f"../ficheros/peliculas{anio}.txt", "w", encoding="utf-8") as archivo:
        archivo.write(datos)

def main():
    anio = int(input("Ingrese el año: "))
    while (anio >= datetime.datetime.now().year):
        anio = int(input("Ingrese el año. (No puede ser menor que el actual)"))
    fichero = input("(../ficheros/peliculas.txt) Ingrese la ruta del fichero: ")
    if fichero == "":
        fichero = "../ficheros/peliculas.txt"
    pipe1, pipe2 = Pipe()
    p1 = Process(target=proceso1, args=(fichero, anio, pipe1))
    p2 = Process(target=proceso2, args=(pipe2, anio))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    main()