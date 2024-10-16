#coding: latin1
from Clases import *
from ClaseCRUD import *
from pip._vendor import requests

def main():

    ## opc1: Periodistas o articulos
    opc1 = 3

    ## opc2: Opciones principales
    opc2 = int

    ## Codigo principal
    while opc1 != 0:
        print("1. Periodistas")
        print("2. Articulos")
        print("0. Salir")
        opc1 = int(input("Inserta una opcion: "))

        ## Opc1 = 1: periodista
        if opc1 == 1:
            opc2 = 5
            while opc2 != 0:

                ## Menu principal periodista
                print("1. Crear periodista")
                print("2. Modificar periodista")
                print("3. Mostrar periodistas")
                print("4. Borrar periodista")
                print("0. Volver")
                opc2 = int(input("Inserta una opcion: "))

                ## Opc2 = 1: creacion de un periodista
                if opc2 == 1:
                    creaPeriodista()

                ## Opc2 = 2: modificacion de datos
                elif opc2 == 2:
                    modificarPeriodistas()

                ## Opc2 = 3: muestra de periodistas
                elif opc2 == 3:
                    mostrarPeriodistas()

                ## Opc2 = 4: borrado de periodistas
                elif opc2 == 4:
                    borrarPeriodistas()

                ## Opc2 = 0: volver
                elif opc2 == 0:
                    print("Volviendo...")

                ## Otro: opcion invalida
                else:
                    print("ERROR: opcion invalida")

        ## Opc1 = 2: Articulo
        elif opc1 == 2:
            opc2 = 5
            while opc2 != 0:

                ## Menu principal articulo
                print("1. Crear articulo")
                print("2. Modificar articulo")
                print("3. Mostrar articulos")
                print("4. Borrar articulo")
                print("0. Volver")
                opc2 = int(input("Inserta una opcion: "))

                ## Opc2 = 1: creacion de un articulos
                if opc2 == 1:
                    crearArticulo()

                ## Opc2 = 2: modificacion de datos
                elif opc2 == 2:
                    modificarArticulos()

                ## Opc2 = 3: muestra de articulos
                elif opc2 == 3:
                    mostrarArticulos()

                ## Opc2 = 4: borrado de articulos
                elif opc2 == 4:
                    borrarArticulos()

                ## Opc2 = 0: volver
                elif opc2 == 0:
                    print("Volviendo...")

                ## Otro: opcion invalida
                else:
                    print("ERROR: opcion invalida")

        ## Opc1 = 0: salida
        elif opc1 == 0:
            print("Saliendo del programa...")

        ## Opc1 = otro: error
        else:
            print("ERROR: opcion invalida")

## Codigo que hace ejecutar el main
if __name__ == "__main__":
    main()