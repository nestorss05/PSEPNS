from multiprocessing import Pool
import random

ficheroMedias = "../ficheros/medias.txt"

def proceso1(fichero: str):
    with open(fichero, "w", encoding="utf-8") as archivo:
        for i in range(6):
            num = round(random.uniform(1.0, 10.0), 2)
            archivo.write(f"{num}\n")

def proceso2(fichero: str, nombreAlumno: str):
    with open(fichero, "r", encoding="utf-8") as archivo:
        datos = list(map(float, archivo.readlines()))
    media = round(sum(datos)/len(datos), 2)
    infoFichero = f"{media} {nombreAlumno}"
    with open(ficheroMedias, "w", encoding="utf-8") as medias:
        medias.write(f"{infoFichero}\n")

def proceso3():
    notamax = 0
    alumnomax = ""
    with open(ficheroMedias, "r", encoding="utf-8") as medias:
        for linea in medias:
            nota, alumno = linea.split()
            nota = float(nota)
            if nota > notamax:
                notamax = nota
                alumnomax = alumno
    print(f"Maxima nota: {notamax}")
    print(f"Alumno con la maxima nota: {alumnomax}")

def main():

    fichero = [f"../ficheros/ejercicio3_alumno{i + 1}.txt" for i in range(10)]
    with Pool(processes=10) as pool:
        pool.map(proceso1, fichero)

    alumnos = [f"Alumno{i + 1}" for i in range(10)]
    with Pool(processes=10) as pool:
        pool.starmap(proceso2, zip(fichero, alumnos))

    proceso3()

if __name__ == "__main__":
    main()