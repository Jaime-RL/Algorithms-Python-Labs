# Algoritmo para encontrar un candidato en un arreglo de enteros
# que aparece más de la mitad de las veces (si existe).
# Se implementan dos versiones: una recursiva y otra iterativa.


def Candidato_recursivo(B, i, j):
    # Caso base: si el subarreglo tiene un solo elemento
    if i == j:
        return B[i]

    if i > j:
        return None

    temp = []  # Lista para almacenar los candidatos
    # Recorremos el rango formando pares
    for k in range(i, j, 2):
        if k + 1 <= j and B[k] == B[k + 1]:
            temp.append(B[k])
    # Si la cantidad de elementos es impar, se agrega el último elemento
    if (j - i + 1) % 2 != 0:
        temp.append(B[j])

    # Si no quedan candidatos, se retorna None
    if len(temp) == 0:
        return None

    # Se llama recursivamente usando el arreglo temporal completo, con índices 0 hasta len(temp)-1
    return Candidato_recursivo(temp, 0, len(temp) - 1)


def Candidato_iterativo(B, i, j):
    while (j - i + 1) > 1:
        temp = []  # Lista para la ronda actual de candidatos
        for k in range(i, j, 2):
            if k + 1 <= j and B[k] == B[k + 1]:
                temp.append(B[k])
        if (j - i + 1) % 2 != 0:
            temp.append(B[j])

        if len(temp) == 0:
            return None

        # Se actualiza B con los candidatos obtenidos y se redefinen los índices
        B = temp
        i = 0
        j = len(B) - 1

    return B[i]  # Al finalizar, i == j y ese es el candidato


# Ejemplo de uso:
B = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4]
cr = Candidato_recursivo(B, 0, len(B) - 1)
ci = Candidato_iterativo(B, 0, len(B) - 1)

if cr == ci:
    print(f"Candidato encontrado: {cr}")
else:
    print("No se encontró un candidato iterativo.")
