from multiprocessing import Process, Value, Lock

def incremento(id,variable,lock):
    for _ in range(10):
        with lock:
            print(f"P{id}: ATACAR {_}")
            variable.value+=1

if __name__ == '__main__':
    numproc = 4
    variable = Value("i", 0)
    procesos = []
    lock=Lock()

    for i in range(numproc):
        p=Process(target=incremento, args=(i,variable,lock))
        procesos.append(p)
    for p in procesos:
        p.start()
    for p in procesos:
        p.join()

    print("Resultado:", variable.value)