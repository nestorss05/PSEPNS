from threading import Thread

class AlCarajoException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg

class Vocal(Thread):
    def __init__(self, vocal, texto):
        Thread.__init__(self)
        self.vocal = vocal
        self.texto = texto

    def run(self):
        if self.vocal not in self.texto:
            raise AlCarajoException(f"ERROR: no hay nada en la vocal {self.vocal}")

        cont = 0
        for linea in self.texto:
            for caracter in linea:
                if caracter.lower() == self.vocal.lower():
                    cont+=1

        print(f"Caracteres de letra {self.vocal}: {cont}")

if __name__ == '__main__':
    texto = "A saber cuantas vocales hay aqui"
    vocales = ["a", "e", "i", "o", "u"]
    hilos = []

    for vocal in vocales:
        v = Vocal(vocal, texto)
        hilos.append(v)
        v.start()

    for h in hilos:
        h.join()