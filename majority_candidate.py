"""Candidato a elemento mayoritario: versión recursiva y su equivalente iterativa.

Devuelve el único elemento que puede aparecer más de la mitad de las veces (si existe).
"""


def Candidato_recursivo(B, i, j):
    """Devuelve el candidato a mayoritario de B[i..j] (o None) de forma recursiva.

    Se emparejan elementos consecutivos: si son iguales se conserva uno, si no se
    descartan ambos. Si la longitud es impar, el último elemento solo se usa como
    desempate cuando la reducción no produce ningún candidato.
    """
    # Caso base: un único elemento es su propio candidato
    if i == j:
        return B[i]
    if i > j:
        return None

    temp = []  # Candidatos que sobreviven a esta ronda
    for k in range(i, j, 2):
        if B[k] == B[k + 1]:
            temp.append(B[k])

    resultado = Candidato_recursivo(temp, 0, len(temp) - 1)

    # Desempate con el elemento sobrante cuando la longitud es impar
    if resultado is None and (j - i + 1) % 2 != 0:
        return B[j]
    return resultado


def Candidato_iterativo(B, i, j):
    """Versión iterativa equivalente a Candidato_recursivo.

    La recursión se elimina guardando en una pila los elementos sobrantes de cada
    ronda impar: si la reducción termina sin candidato, el desempate válido es el
    del nivel más profundo, es decir, el último apilado.
    """
    sobrantes = []
    while i <= j:
        if i == j:
            return B[i]
        if (j - i + 1) % 2 != 0:
            sobrantes.append(B[j])
        temp = [B[k] for k in range(i, j, 2) if B[k] == B[k + 1]]
        B, i, j = temp, 0, len(temp) - 1

    return sobrantes[-1] if sobrantes else None


if __name__ == "__main__":
    B = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4]
    cr = Candidato_recursivo(B, 0, len(B) - 1)
    ci = Candidato_iterativo(B, 0, len(B) - 1)

    if cr == ci:
        print(f"Candidato encontrado: {cr}")
    else:
        print("Las versiones recursiva e iterativa no coinciden.")
