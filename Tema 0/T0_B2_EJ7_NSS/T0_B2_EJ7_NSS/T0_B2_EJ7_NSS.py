def main():
    opc = 4
    tel = 0
    nom = ""
    contactos = {}
    while opc != 0:
        input("Presione una tecla para continuar")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("0. Salir")
        opc = int(input("Elige una opcion: "))
        if opc == 1:
            nom = input("Inserta un nombre: ")
            tel = input("Inserta un telefono: ")
            contactos[nom] = tel
            print("Contacto agregado")
        elif opc == 2:
            nom = input("Inserta un nombre: ")
            if (nom in contactos):
                print(nom + " " + contactos[nom])
            else:
                print("ERROR: contacto no encontrado")
        elif opc == 3:
            nom = input("Inserta un nombre: ")
            contactos.pop(nom)
            print("Contacto eliminado")
        elif opc == 0:
            print("Saliendo del programa...")
        else:
            print("ERROR: opcion invalida")

if __name__ == "__main__":
    main()