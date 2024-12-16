import threading
import time
import queue

def atender_cliente(id_caja, cliente_id, tiempo_atencion, resultados):
    print(f"Caja {id_caja} atendiendo al cliente {cliente_id} por {tiempo_atencion} segundos...")
    time.sleep(tiempo_atencion)
    print(f"Caja {id_caja} terminó de atender al cliente {cliente_id}.")
    resultados[id_caja] += 1

def trabajar_caja(id_caja, cola_clientes, resultados):
    while not cola_clientes.empty():
        try:
            cliente_id, tiempo_atencion = cola_clientes.get_nowait()
            atender_cliente(id_caja, cliente_id, tiempo_atencion, resultados)
        except queue.Empty:
            break

def main():
    N = 5  # Número de cajas registradoras
    clientes = [(i, 1 + i % 3) for i in range(10)]  # Lista de clientes con su tiempo de atención
    cola_clientes = queue.Queue()

    # Encolar a los clientes
    for cliente_id, tiempo_atencion in clientes:
        cola_clientes.put((cliente_id, tiempo_atencion))

    # Diccionario para almacenar los resultados de cada caja
    resultados = {i: 0 for i in range(N)}

    # Crear e iniciar los hilos para las cajas registradoras
    hilos = []
    for i in range(N):
        hilo = threading.Thread(target=trabajar_caja, args=(i, cola_clientes, resultados))
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    # Mostrar los resultados
    total_tiempo = sum(clientes[i][1] for i in range(len(clientes)))
    print("Tiempo total: {:.2f} segundos".format(total_tiempo))
    for id_caja, clientes_atendidos in resultados.items():
        print(f"Caja {id_caja} atendió a {clientes_atendidos} cliente(s).")

if __name__ == "__main__":
    main()
