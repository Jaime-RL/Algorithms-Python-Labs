"""Puzzle de las ranas: intercambiar dos grupos de fichas (1 y -1) separadas por un hueco (0).

Cada ficha solo avanza hacia delante, deslizándose al hueco o saltando sobre una ficha contraria.
Se resuelve con un esquema recursivo y con su transformación a iterativo, mostrando el
tablero en cada paso con colores ANSI.
"""
# Implementación de los algoritmos
def Recursivo(A, hueco, ficha, m):
    if m >= len(A) - 2:  # ES_SENCILLO
        Mostrar(A)
        return 0
    else:  # C(RECURSIVO(F(x)), x)
        Mostrar(A)
        A[hueco], A[ficha] = A[ficha], A[hueco]
        n = len(A) // 2
        if ficha == n:
            m += 1
        if n - 1 <= ficha <= n + 1:
            m += 1
        if hueco - 1 <= ficha <= hueco + 1:
            return Recursivo(A, ficha, hueco - A[hueco], m) + 1
        elif A[hueco] == A[ficha + A[hueco]]:
            return Recursivo(A, ficha, ficha + A[hueco], m) + 1
        else:
            return Recursivo(A, ficha, ficha + A[hueco] * 2, m) + 1


"""RECURSIVO(x): 
    if ES_SENCILLO(x): 
        y ← DIRECTO(x) 
    else: 
        y ← C(RECURSIVO(F(x)), x) 
    return y 

ITERATIVO(x): 
    x´ ← x 
    while not ES_SENCILLO(x´): 
        x´ ← F´(x) 
    y ← DIRECTO(x´) 
    while x´ ≠ x: 
        x´ ← F-1(x´) 
        y ← C(y, x´) 
    return y"""


def Iterativo(A, tabl=False):
    n = len(A) // 2
    hueco = n
    ficha = hueco - 1
    m = 0

    while m < 2 * n - 1:
        Mostrar(A)
        A[hueco], A[ficha] = A[ficha], A[hueco]

        if ficha == n:
            m += 1
        if n - 1 <= ficha <= n + 1:
            m += 1
        if hueco - 1 <= ficha <= hueco + 1:
            ficha, hueco = hueco, ficha - A[hueco]
        elif A[hueco] == A[ficha + A[hueco]]:
            ficha, hueco = ficha, ficha + A[hueco]
        else:
            ficha, hueco = ficha, ficha + A[hueco] * 2

    return m


def Mostrar(A):
    s = ""
    for i in range(len(A)):
        if A[i] == 1:
            s += "\33[42m  \33[0m  "
        elif A[i] == -1:
            s += "\33[43m  \33[0m  "
        else:
            s += "\33[47m  \33[0m  "
    print("\n" + s)


if __name__ == "__main__":
    A = [-1, -1, 0, 1, 1]
    print("Recursivo: ", Recursivo(A, 2, 1, 0))
    A = [1, 1, 0, -1, -1]
    print("Iterativo: ", Iterativo(A, True))
