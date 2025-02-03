import random
import time
from threading import Event, Thread

ratones = 5

class Raton(Thread):
    def __init__(self, nombre, event:Event):
        Thread.__init__(self, name=nombre)
        self.event = event

    def run(self):
        while not self.event.is_set():
            print(f"A el raton {self.name} le renta esperar")
            self.event.wait()
        self.event.clear()
        print(f"El raton {self.name} esta siendo un raton malo")
        time.sleep(random.randint(1,3))
        print(f"El raton {self.name} se quito de en medio al Doctor Malvedades")
        self.event.set()

if __name__ == "__main__":
    print("Los ratones")
    event = Event()
    event.set()
    threads = []

    for i in range(ratones):
        r = Raton(f"R{i+1}", event)
        threads.append(r)
        r.start()

    for t in threads:
        t.join()