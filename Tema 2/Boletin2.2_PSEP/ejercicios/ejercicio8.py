from multiprocessing import Process, Pipe

def producer(pipe: Pipe, proc: int):
    print("PROCESO " + str(proc))
    numeros = leeFichero().split(" ")
    pipe.send(numeros)
    print("Enviado")

def consumer(pipe: Pipe):
    numeros = pipe.recv()
    num1 = int(numeros[0])
    num2 = int(numeros[1])
    inicio = min(num1, num2)
    fin = max(num1, num2)
    res = sum(range(inicio, fin + 1))
    print(f"Suma entre los dos numeros: {res}")
    pipe.close()

def leeFichero():
    archivo = open("../ficheros/ejercicios7y8.txt", "r", encoding="utf-8")
    datos = archivo.read()
    archivo.close()
    return datos

if __name__ == '__main__':
    pipe1, pipe2 = Pipe()
    proceso1a = Process(target=producer, args=(pipe1, 1))
    proceso1b = Process(target=consumer, args=(pipe2,))
    proceso2a = Process(target=producer, args=(pipe1, 2))
    proceso2b = Process(target=consumer, args=(pipe2,))
    proceso1a.start()
    proceso1b.start()
    proceso2a.start()
    proceso2b.start()
    proceso1a.join()
    proceso1b.join()
    print("P1 terminado")
    proceso2a.join()
    proceso2b.join()
    print("P2 terminado")