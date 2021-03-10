import math
limite_superior = float('inf')

def crearFinal(camino_actual):
    camino_final[:numero_nodos + 1] = camino_actual[:]
    camino_final[numero_nodos] = camino_actual[0]

def primerMinimo(adj, i):
    min = limite_superior
    for k in range(numero_nodos):
        if adj[i][k] < min and i != k:
            min = adj[i][k]
    return min

def segundoMinimo(adj, i):
    primero, segundo = limite_superior, limite_superior
    for j in range(numero_nodos):
        if i == j:
            continue
        if adj[i][j] <= primero:
            segundo = primero
            primero = adj[i][j]

        elif (adj[i][j] <= segundo and
              adj[i][j] != primero):
            segundo = adj[i][j]
    return segundo

def rec(adj, bound_actual, peso_actual, profundidad, camino_actual, visitado):
    global costo

    if profundidad == numero_nodos:
        if adj[camino_actual[profundidad - 1]][camino_actual[0]] != 0:
            curr_res = peso_actual + adj[camino_actual[profundidad - 1]] \
                [camino_actual[0]]
            if curr_res < costo:
                crearFinal(camino_actual)
                costo = curr_res
        return

    for i in range(numero_nodos):

        if (adj[camino_actual[profundidad - 1]][i] != 0 and visitado[i] == False):
            temp = bound_actual
            peso_actual += adj[camino_actual[profundidad - 1]][i]


            if profundidad == 1:
                bound_actual -= ((primerMinimo(adj, camino_actual[profundidad - 1]) + primerMinimo(adj, i)) / 2)
            else:
                bound_actual -= ((segundoMinimo(adj, camino_actual[profundidad - 1]) + primerMinimo(adj, i)) / 2)

            if bound_actual + peso_actual < costo:
                camino_actual[profundidad] = i
                visitado[i] = True

                rec(adj, bound_actual, peso_actual, profundidad + 1, camino_actual, visitado)

            peso_actual -= adj[camino_actual[profundidad - 1]][i]
            bound_actual = temp

            visitado = [False] * len(visitado)
            for j in range(profundidad):
                if camino_actual[j] != -1:
                    visitado[camino_actual[j]] = True

def BranchBound(adj):
    bound_actual = 0
    camino_actual = [-1] * (numero_nodos + 1)
    visitados = [False] * numero_nodos

    for i in range(numero_nodos):
        bound_actual += (primerMinimo(adj, i) +
                         segundoMinimo(adj, i))

    bound_actual = math.ceil(bound_actual / 2)

    visitados[0] = True
    camino_actual[0] = 0

    rec(adj, bound_actual, 0, 1, camino_actual, visitados)


adj_matrix = [[0, 10, 15, 20],
              [10, 0, 35, 25],
              [15, 35, 0, 30],
              [20, 25, 30, 0]]

#adj_matrix = [[0, 10, 15, 20],
#              [10, 0, 35, 25],
#              [15, 35, 0, 30],
#              [20, 25, 30, 0]]

#adj_matrix = [[0, 10, 15, 20],
#              [10, 0, 35, 25],
#              [15, 35, 0, 30],
#              [20, 25, 30, 0]]

numero_nodos = 4

camino_final = [None] * (numero_nodos + 1)

visitados = [False] * numero_nodos

costo = limite_superior

BranchBound(adj_matrix)

print("Minimum cost :", costo)
print("Path Taken : ", end=' ')
for i in range(numero_nodos + 1):
    print(camino_final[i], end=' ')
