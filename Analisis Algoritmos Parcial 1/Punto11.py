# Problema del Camino más Corto en un Grafo (Algoritmo de Dijkstra)

import heapq
import collections

def dijkstra(grafo, fuente):
    """
    Implementa el Algoritmo de Dijkstra para encontrar el camino más corto
    desde un nodo fuente a todos los demás nodos en un grafo con pesos no negativos.

    Args:
        grafo: Diccionario que representa el grafo. Las claves son los nodos.
               Los valores son diccionarios de vecinos y el peso de la arista:
               grafo[u] = {v: peso_uv, w: peso_uw, ...}
        fuente: El nodo de inicio.

    Returns:
        Un diccionario con las distancias más cortas desde la fuente a cada nodo.
        distancias[nodo] = distancia_mas_corta
    """
    # Diccionario para almacenar las distancias más cortas desde la fuente.
    # Inicializamos todas las distancias como infinito, excepto la de la fuente que es 0.
    distancias = {nodo: float('infinity') for nodo in grafo}
    distancias[fuente] = 0

    # Cola de prioridad para almacenar nodos y sus distancias.
    # heapq implementa una min-heap, por lo que el elemento con la distancia más pequeña
    # estará siempre en la parte superior. Almacenamos (distancia, nodo).
    cola_prioridad = [(0, fuente)]

    # Conjunto para llevar un registro de los nodos visitados.
    visitados = set()

    while cola_prioridad:
        # Extraer el nodo con la menor distancia conocida de la cola de prioridad.
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        # Si el nodo ya ha sido visitado, lo ignoramos (esto maneja entradas duplicadas en la heap)
        if nodo_actual in visitados:
            continue

        # Marcar el nodo actual como visitado
        visitados.add(nodo_actual)

        # Si el nodo actual no está en el grafo (puede ocurrir con nodos aislados no en las claves principales)
        if nodo_actual not in grafo:
             continue


        # Explorar los vecinos del nodo actual
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso

            # Si se encuentra un camino más corto al vecino
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                # Añadir el vecino a la cola de prioridad con la nueva distancia
                heapq.heappush(cola_prioridad, (distancia, vecino))

    return distancias

# --- Ejemplo de uso ---

# Definir el grafo de la ciudad
# grafo[interseccion_origen] = {interseccion_destino: tiempo_viaje}
grafo_ciudad = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3}
}

# Definir la intersección de inicio
inicio = 'A'

# Calcular las distancias más cortas desde el inicio
distancias_mas_cortas = dijkstra(grafo_ciudad, inicio)

# Imprimir los resultados
print(f"Distancias más cortas desde la intersección {inicio}:")
for nodo, distancia in distancias_mas_cortas.items():
    print(f"A {nodo}: {distancia}")