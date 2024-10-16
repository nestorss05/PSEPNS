#coding: latin1
from Clases import Calculo
res = 5
while res != 0:
    obj = Calculo(6, 3)
    res = int(input("Inserta una opcion: "))
    if res == 1:
        print(Calculo.suma(obj))
    elif res == 2:
        print(Calculo.resta(obj))
    elif res == 3:
        print(Calculo.multp(obj))
    elif res ==4 :
        print(Calculo.divi(obj))
    elif res == 0:
        print("Saliendo del programa")
    else:
        print("ERROR: opcion invalida")