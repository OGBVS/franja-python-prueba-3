import numpy as np
import random

def archivo():
    nombre_fichero = "./numeros_prueba.txt"
    with open(nombre_fichero, "w", encoding="utf-8") as file:
        for i in range(1,21):
            numero_aleatorio = random.randint(100, 1000)
            linea = str(numero_aleatorio)

            file.write(linea)
            file.write("\n")
def leer():
    numeros = []
    with open("./numeros_prueba.txt","r") as file:
        for linea in file:
            numeros.append(int(linea))

    numerosimpar = []

    for z in numeros:

        if z %2 !=0:

            numerosimpar.append(z)
        
    return numerosimpar

def main ():
    archivo()

    numerosimpar = leer()

    print(numerosimpar)

    arreglo = np.array(numerosimpar)
    print(arreglo.ndim)

if __name__ == '__main__':
    main()
