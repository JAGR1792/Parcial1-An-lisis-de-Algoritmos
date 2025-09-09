# Optimización de Flujo en una Red de Tuberías (Método Ford-Fulkerson con DFS)

import collections

def dfs(grafo_residual, s, t, camino, capacidad_minima):
    """
    Realiza una búsqueda en profundidad (DFS) para encontrar un camino de aumento
    desde la fuente 's' al sumidero 't' en el grafo residual.

    Args:
        grafo_residual: Diccionario que representa el grafo con capacidades residuales.
                        grafo_residual[u][v] = capacidad residual de u a v.
        s: Nodo fuente.
        t: Nodo sumidero.
        camino: Lista para almacenar el camino encontrado.
        capacidad_minima: La capacidad mínima encontrada hasta ahora en el camino actual.

    Returns:
        La capacidad mínima del camino encontrado, o 0 si no se encontró camino.
    """
    # Marca el nodo actual como visitado en este camino DFS
    visitados.add(s)

    # Si llegamos al sumidero, hemos encontrado un camino de aumento
    if s == t:
        return capacidad_minima

    # Explora los vecinos del nodo actual
    if s in grafo_residual:
        for v, capacidad in grafo_residual[s].items():
            # Si el vecino no ha sido visitado en este DFS y hay capacidad residual
            if v not in visitados and capacidad > 0:
                # Añade el vecino al camino actual
                camino.append((s, v))

                # Continúa la búsqueda en profundidad desde el vecino
                nueva_capacidad_minima = dfs(grafo_residual, v, t, camino, min(capacidad_minima, capacidad))

                # Si se encontró un camino desde el vecino hasta el sumidero
                if nueva_capacidad_minima > 0:
                    return nueva_capacidad_minima

                # Si no se encontró un camino desde el vecino, retrocede
                camino.pop()

    # Si no se encontró un camino desde este nodo
    return 0


def ford_fulkerson_dfs(grafo, s, t):
    """
    Implementa el método de Ford-Fulkerson utilizando DFS para encontrar caminos de aumento.

    Args:
        grafo: Diccionario que representa el grafo con capacidades iniciales.
               grafo[u][v] = capacidad de u a v.
        s: Nodo fuente.
        t: Nodo sumidero.

    Returns:
        El flujo máximo de la red.
    """
    # Inicializar el grafo residual con las capacidades iniciales
    # Usamos deepcopy para no modificar el grafo original si es necesario
    # Pero un defaultdict anidado simple también funciona para este caso
    grafo_residual = collections.defaultdict(lambda: collections.defaultdict(int))
    for u in grafo:
        for v, capacidad in grafo[u].items():
            grafo_residual[u][v] = capacidad

    flujo_maximo = 0

    # Buscar caminos de aumento mientras existan
    while True:
        # Conjunto para llevar el registro de nodos visitados en cada DFS
        global visitados # Usamos una variable global para resetear en cada DFS
        visitados = set()

        camino = []
        # Encontrar un camino de aumento desde la fuente al sumidero
        # Empezamos con una capacidad mínima muy grande (infinita conceptualmente)
        capacidad_aumento = dfs(grafo_residual, s, t, camino, float('inf'))

        # Si no se encontró un camino de aumento, hemos alcanzado el flujo máximo
        if capacidad_aumento == 0:
            break

        # Si se encontró un camino, aumentar el flujo a lo largo del camino
        flujo_maximo += capacidad_aumento

        # Actualizar las capacidades residuales a lo largo del camino encontrado
        for u, v in camino:
            grafo_residual[u][v] -= capacidad_aumento  # Reducir capacidad en arista de avance
            grafo_residual[v][u] += capacidad_aumento  # Aumentar capacidad en arista de retroceso

    return flujo_maximo

# --- Ejemplos de uso ---

# Ejemplo 1: Grafo pequeño
grafo_ejemplo1 = {
    's': {'a': 10, 'b': 8},
    'a': {'c': 5, 'd': 5},
    'b': {'c': 4, 'd': 7},
    'c': {'t': 9},
    'd': {'t': 10}
}
fuente1 = 's'
sumidero1 = 't'

print("Datos del Ejemplo 1:")
print(grafo_ejemplo1)
print("-" * 20)

# Calcular y mostrar el flujo máximo para el Ejemplo 1
flujo_max1 = ford_fulkerson_dfs(grafo_ejemplo1, fuente1, sumidero1)
print(f"El flujo máximo para el Ejemplo 1 (fuente {fuente1} al sumidero {sumidero1}) es: {flujo_max1}")

print("-" * 20) # Separador

# Ejemplo 2: Otro grafo
grafo_ejemplo2 = {
    1: {2: 10, 3: 5, 4: 10},
    2: {3: 10, 5: 15},
    3: {4: 10, 5: 10},
    4: {5: 10},
    5: {} # El sumidero no tiene aristas salientes en este ejemplo
}
fuente2 = 1
sumidero2 = 5

print("Datos del Ejemplo 2:")
print(grafo_ejemplo2)
print("-" * 20)

# Calcular y mostrar el flujo máximo para el Ejemplo 2
flujo_max2 = ford_fulkerson_dfs(grafo_ejemplo2, fuente2, sumidero2)
print(f"El flujo máximo para el Ejemplo 2 (fuente {fuente2} al sumidero {sumidero2}) es: {flujo_max2}")
