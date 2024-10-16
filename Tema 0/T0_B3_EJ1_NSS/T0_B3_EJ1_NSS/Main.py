from Clases import *

def main():
    opc = 3
    cant = 0
    obj = CuentaCorriente("567F", "Pepitto", 68943)
    while opc != 0:
        print("1. Sacar dinero")
        print("2. Ingresar dinero")
        print("0. Salir")
        opc = int(input("Inserta una opcion: "))

        if opc == 1:
            cant = int(input("Inserta la cantidad a retirar: "))
            if (CuentaCorriente.sacarDinero(obj, cant)) :
                print("Operacion realizada con exito")
            else:
                print("ERROR: no se ha podido retirar el dinero")
        elif opc == 2:
            cant = int(input("Inserta la cantidad a introducir: "))
            CuentaCorriente.ingresarDinero(obj, cant)
        elif opc == 0:
            print("Saliendo del programa...")
        else:
            print("ERROR: opcion invalida")

if __name__ == "__main__":
    main()