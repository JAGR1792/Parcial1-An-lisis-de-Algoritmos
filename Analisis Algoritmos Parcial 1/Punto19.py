import heapq

def encontrar_ruta_optima(grafo, origen, destino):
    """
    Encuentra la ruta óptima maximizando el ancho de banda y minimizando la latencia.
    
    Args:
        grafo: Diccionario donde las claves son los nodos y los valores son diccionarios
               con los vecinos como claves y tuplas (ancho_banda, latencia) como valores
        origen: Nodo de origen
        destino: Nodo de destino
        
    Returns:
        Tupla (ruta, ancho_banda_minimo, latencia_total) donde:
        - ruta: Lista con la secuencia de nodos que forman la ruta
        - ancho_banda_minimo: El ancho de banda mínimo en la ruta (cuello de botella)
        - latencia_total: La latencia total acumulada en la ruta
    """
    # Inicializamos las estructuras de datos
    # Para cada nodo, almacenamos (ancho_banda_minimo, latencia_total, nodo_previo)
    mejor_ruta = {nodo: (0, float('inf'), None) for nodo in grafo}
    mejor_ruta[origen] = (float('inf'), 0, None)
    visitados = set()
    
    # Cola de prioridad para procesar los nodos
    # Ordenamos primero por ancho de banda (mayor primero), luego por latencia (menor primero)
    cola = [(-float('inf'), 0, origen)]  # (negativo del ancho de banda, latencia, nodo)
    
    while cola:
        # Obtenemos el nodo con mayor ancho de banda mínimo (o menor latencia en caso de empate)
        _, _, nodo_actual = heapq.heappop(cola)
        
        if nodo_actual == destino:
            break
        
        if nodo_actual in visitados:
            continue
        
        visitados.add(nodo_actual)
        
        ancho_banda_actual, latencia_actual, _ = mejor_ruta[nodo_actual]
        
        # Exploramos los vecinos del nodo actual
        for vecino, (ancho_banda_enlace, latencia_enlace) in grafo[nodo_actual].items():
            if vecino in visitados:
                continue
            
            # Calculamos el nuevo ancho de banda y latencia
            nuevo_ancho_banda = min(ancho_banda_actual, ancho_banda_enlace)
            nueva_latencia = latencia_actual + latencia_enlace
            
            # Actualizamos si encontramos una ruta con mayor ancho de banda o igual ancho de banda pero menor latencia
            ancho_banda_vecino, latencia_vecino, _ = mejor_ruta[vecino]
            if nuevo_ancho_banda > ancho_banda_vecino or (nuevo_ancho_banda == ancho_banda_vecino and nueva_latencia < latencia_vecino):
                mejor_ruta[vecino] = (nuevo_ancho_banda, nueva_latencia, nodo_actual)
                # Negamos el ancho de banda para que la cola de prioridad ordene de mayor a menor
                heapq.heappush(cola, (-nuevo_ancho_banda, nueva_latencia, vecino))
    
    # Reconstruimos la ruta
    ruta = []
    nodo = destino
    while nodo is not None:
        ruta.append(nodo)
        nodo = mejor_ruta[nodo][2]  # Nodo previo
    
    ruta.reverse()
    
    # Si no hay ruta al destino
    if not ruta or ruta[0] != origen:
        return ([], 0, float('inf'))
    
    # Devolvemos la ruta, el ancho de banda mínimo y la latencia total
    return (ruta, mejor_ruta[destino][0], mejor_ruta[destino][1])

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo de grafo: {nodo: {vecino: (ancho_banda, latencia), ...}, ...}
    grafo = {
        'A': {'B': (100, 10), 'C': (200, 20)},
        'B': {'A': (100, 10), 'D': (50, 5), 'E': (150, 15)},
        'C': {'A': (200, 20), 'E': (80, 8)},
        'D': {'B': (50, 5), 'F': (120, 12)},
        'E': {'B': (150, 15), 'C': (80, 8), 'F': (100, 10)},
        'F': {'D': (120, 12), 'E': (100, 10)}
    }
    
    origen = 'A'
    destino = 'F'
    
    ruta, ancho_banda, latencia = encontrar_ruta_optima(grafo, origen, destino)
    
    if ruta:
        print(f"Ruta óptima de {origen} a {destino}: {' -> '.join(ruta)}")
        print(f"Ancho de banda mínimo (cuello de botella): {ancho_banda}")
        print(f"Latencia total: {latencia}")
    else:
        print(f"No hay ruta disponible de {origen} a {destino}")