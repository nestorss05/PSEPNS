from multiprocessing import Pool


class AlCarajoException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg

def contarVocales(letra):
    datos = leeFichero()
    if letra not in 'aeiouAEIOU' or len(letra) != 1:
        raise AlCarajoException("ERROR: no es vocal y/o longitud mayor que 1")

    cont = 0
    for linea in datos:
        for caracter in linea:
            if caracter.lower() == letra.lower():
                cont+=1

    return cont

def leeFichero():
    archivo = open("../ficheros/ejercicio1.txt", "r", encoding="utf-8")
    datos = archivo.read()
    archivo.close()
    return datos

if __name__ == "__main__":
    with Pool(processes=5) as pool:
        vocales = ['a', 'e', 'i', 'o', 'u']
        res = pool.map(contarVocales, vocales)
    print("Resultados:", res)