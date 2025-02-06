import threading

class Contador:
   def __init__(self):
       self.valor = 0  # Contador inicializado en 0
       self.lock = threading.Lock()  # Lock para asegurar acceso atómico al contador


   # Función para incrementar el contador de forma segura
   def incrementar(self, total):
       with self.lock:  # Asegura que solo un hilo pueda modificar el contador a la vez
           if self.obtener_valor() >= total:   # Si el contador ya alcanza el total
               return  # Sale de la función
           self.valor += 1  # Incrementar el valor del contador

   # Función para obtener el valor actual del contador
   def obtener_valor(self):
       return self.valor

   # Función que simula la operación de incrementar el contador desde múltiples hilos
   def incrementar_contador(self, total):
       while self.obtener_valor() < total:
           self.incrementar(total)  # Cada hilo incrementará el contador N veces
           print(self.obtener_valor())

if __name__ == "__main__":
   contador = Contador()  # Crear una instancia de la clase Contador
   hilos = []  # Lista para guardar los hilos
   N = 10  # Número de hilos
   TOTAL = 10000  # Total a alcanzar

   # Crear y arrancar los hilos
   for _ in range(N):
       hilo = threading.Thread(target=contador.incrementar_contador, args=(TOTAL,))
       hilos.append(hilo)
       hilo.start()

   # Esperar a que todos los hilos terminen
   for hilo in hilos:
       hilo.join()

   # Mostrar el valor final del contador
   print(f"Valor final del contador: {contador.obtener_valor()}")