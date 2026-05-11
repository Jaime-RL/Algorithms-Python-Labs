import time
import matplotlib.pyplot as plt

# Description: Algoritmo que busca un elemento mayoritario en un array


def Mayoritario3(A, i, j):
    B = []
    for k in range(i, j + 1):
        B.append(A[k])
    m = Candidato(B, i, j)
    if m is not None:
        m = Comprobar(A, i, j, m)
    return m


def Candidato(B, i, j):
    """
    Encuentra el candidato que aparece más de la mitad de las veces en el subarreglo B[i:j+1].
    Args:
        B (list): Lista de elementos.
        i (int): Índice inicial del subarreglo.
        j (int): Índice final del subarreglo.
    Returns:
        El elemento que aparece más de la mitad de las veces en el subarreglo B[i:j+1] si existe,
        de lo contrario None.
    """

    if i == j:
        # Si el subarreglo tiene un solo elemento, ese es el candidato
        return B[i]

    if i > j or j == 0:
        # Si los índices son inválidos, no hay candidato
        return None

    x = 0

    for k in range(i, j + 1, 2):
        # Si hay un par de elementos iguales, se guarda uno de ellos en la posición x
        if k + 1 <= j and B[k] == B[k + 1]:
            B[x] = B[k]
            x += 1

    # Se llama recursivamente a Candidato con el nuevo subarreglo reducido
    resultado = Candidato(B, 0, x - 1)
    if resultado is None and (j - i + 1) % 2 != 0:
        return B[j]

    return resultado


def Comprobar(A, i, j, m):
    contador = 0
    for k in range(i, j + 1):
        if A[k] == m:
            contador += 1
    if contador > (j - i + 1) / 2:
        return m
    else:
        return None


# Graficar mejor caso y peor caso
def graficar_casos():
    tamanos = [10, 100, 1000, 10000, 100000]
    tiempos_mejor_caso = []
    tiempos_peor_caso = []

    for n in tamanos:
        # Mejor caso: no hay ninguna pareja de elementos iguales
        mejor_caso = list(range(0, n))
        inicio = time.time()
        Mayoritario3(mejor_caso, 0, n - 1)
        fin = time.time()
        tiempos_mejor_caso.append(fin - inicio)

        # Peor caso: no hay elemento mayoritario
        peor_caso = [1] * n
        inicio = time.time()
        Mayoritario3(peor_caso, 0, n - 1)
        fin = time.time()
        tiempos_peor_caso.append(fin - inicio)

    plt.plot(tamanos, tiempos_mejor_caso, label="Mejor caso")
    plt.plot(tamanos, tiempos_peor_caso, label="Peor caso")
    plt.xlabel("Tamaño del array")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Tiempo de ejecución del algoritmo Mayoritario3")
    plt.legend()
    plt.show()


# graficar_casos()
