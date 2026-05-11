import matplotlib.pyplot as plt
import time


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


# n entre 104 y 106 de 10 000 en 10 000 en el mejor caso
vectores_mejor_caso = []
for i in range(10000, 1000001, 10000):
    vec = list(range(i))
    vectores_mejor_caso.append(vec)

# n entre 10000 y 1000000 de 10000 en 10000 en el peor caso
vectores_peor_caso = []
for i in range(10000, 1000001, 10000):
    vec = list(range(i, 0, -1))
    vectores_peor_caso.append(vec)

print(vectores_peor_caso[1])

tiempos_mejor_caso = []
tiempos_peor_caso = []


def calcula_tiempo(vec: list, tiempos: list) -> list:
    for i in vec:
        tiempo_inicial = time.time()
        suma_distancia(i)
        tiempo_final = time.time()
        tiempos.append(tiempo_final - tiempo_inicial)
    return tiempos


tiempos_mejor_caso = calcula_tiempo(vectores_mejor_caso, tiempos_mejor_caso)
tiempos_peor_caso = calcula_tiempo(vectores_peor_caso, tiempos_peor_caso)

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
