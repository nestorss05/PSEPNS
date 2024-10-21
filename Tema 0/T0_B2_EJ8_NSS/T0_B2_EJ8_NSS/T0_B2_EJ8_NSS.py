#coding: latin1
def main():
    ventas = {}
    nom = ""
    uds = 0
    opc = 3
    while opc != 0:
        print("1. Agregar ventas")
        print("2. Calcular tota lde ventas de un producto")
        print("0. Salir")
        opc = int(input("Inserte la opcion: "))
        if opc == 1:
            nom = input("Inserta el nombre del producto: ")
            uds = int(input("Inserta la cantidad de ventas: "))
            ventas[nom] = uds
            print("Producto añadido")
        elif opc == 2:
            nom = input("Inserta el nombre del producto: ")
            if nom in ventas is True:
                print(ventas[nom])
            else:
                print("ERROR: producto no encontrado")   
        elif opc == 0:
            print("Saliendo del programa...")
        else:
            print("ERROR: opcion invalida")

if __name__ == "__main__":
    main()