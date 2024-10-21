
#coding: latin1

def main():
    print("XD")
    pregontas() # no bitches?

if __name__ == "__main__":
    main()

def pregontas():
    # El while para que fufe todo
    opcion=int
    while opcion!=0:
        print("1. Medir TULA")
        print("2. Cadenator")
        print("3. Ternario")
        print("4. Bucle While")
        print("5. Bucle For")
        print("6. SALUDAR")
        print("0. Salir")
        opcion=int(input("Elige opcion"))

        if opcion == 1:

            # XD
            longitud=int(input("Cuanto te mide mi pana?"))
            if longitud < 12:
                print("Not big tula")
            else:
                print("Nice tula mi pana")

        elif opcion == 2:

            # Cadenas
            cadena="gogogo gogogo2"
            palabras = cadena.split()
            print(palabras)
            lista="#".join(['1','2','3','4','5','6','7','8','9','0'])
            print(lista)

        elif opcion == 3:

            # Ternario
            num = int(input("Nummer"))
            var = "par" if (num % 2 == 0) else "impar"
            print(var)

        elif opcion == 4:

            nivel = 1
            while nivel < 16:
                nivel = nivel + 1
                print("Tu Mudkip subio a nivel " + str(nivel))
            print("Tu Mudkip ha evolucionado a Marshtomp")

        elif opcion == 5:

            cadena=input("¿Que le deseas a RENFE Cercanias?")
            for letra in cadena:
                print(letra)
                print("PUTA RENFE")

        elif opcion == 6:
            def saludo(nombre = "Diego"):
                print("Hola " + nombre)
            saludo("Pepitto")
            saludo()
        elif opcion == 7:
            lsty = [22, True, "lista halal", [1,2]]
            num = lsty[2][0]
            print(num)