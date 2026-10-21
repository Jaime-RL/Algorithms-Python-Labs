"""Suma de distancias al siguiente elemento mayor usando una pila monótona: O(n).

Para cada posición i se busca el primer j > i con vec[j] > vec[i] y se suma j - i
(si no existe, se suma la distancia hasta el final del vector). Se mide el tiempo
de ejecución en el mejor y en el peor caso para comprobar empíricamente la complejidad lineal.
"""
import time

import matplotlib.pyplot as plt


def suma_distancia(vec):
    d = 0
    stack = []  # Pila para almacenar índices de elementos pendientes

    for i in range(len(vec)):
        while stack and vec[stack[-1]] < vec[i]:
            d += i - stack.pop()
        stack.append(i)

    # Los elementos restantes en la pila nunca encontraron un número
    while stack:
        d += len(vec) - stack.pop()

    return d


def calcula_tiempo(vec: list, tiempos: list) -> list:
    for i in vec:
        tiempo_inicial = time.time()
        suma_distancia(i)
        tiempo_final = time.time()
        tiempos.append(tiempo_final - tiempo_inicial)
    return tiempos


if __name__ == "__main__":
    # n entre 10^4 y 10^6, de 10 000 en 10 000: mejor caso (vector creciente)
    vectores_mejor_caso = [list(range(i)) for i in range(10000, 1000001, 10000)]

    # Mismos tamaños: peor caso (vector decreciente)
    vectores_peor_caso = [list(range(i, 0, -1)) for i in range(10000, 1000001, 10000)]

    tiempos_mejor_caso = calcula_tiempo(vectores_mejor_caso, [])
    tiempos_peor_caso = calcula_tiempo(vectores_peor_caso, [])

    # Graficar mejor caso
    plt.plot([len(vec) for vec in vectores_mejor_caso], tiempos_mejor_caso, label="Mejor caso")
    plt.xlabel("Tamaño del vector")
    plt.ylabel("Tiempo de ejecución")
    plt.title("Mejor caso")
    plt.grid()
    plt.legend()
    plt.show()

    # Graficar peor caso
    plt.plot([len(vec) for vec in vectores_peor_caso], tiempos_peor_caso, label="Peor caso")
    plt.xlabel("Tamaño del vector")
    plt.ylabel("Tiempo de ejecución")
    plt.title("Peor caso")
    plt.grid()
    plt.legend()
    plt.show()
