def ruta_viajante_vecino_cercano(ciudades, matriz_distancias, ciudad_inicio=0):
    """
    Encuentra una solución al problema del viajante de comercio usando la heurística del vecino más cercano.
    
    Args:
        ciudades: Lista de ciudades (nombres o coordenadas)
        matriz_distancias: Matriz donde matriz_distancias[i][j] es la distancia entre la ciudad i y j
        ciudad_inicio: Índice de la ciudad de inicio
        
    Returns:
        Tupla (ruta, distancia_total) donde:
        - ruta: Lista con el orden de visita de las ciudades
        - distancia_total: Distancia total del recorrido
    """
    n = len(ciudades)
    visitadas = [False] * n
    ruta = [ciudad_inicio]
    visitadas[ciudad_inicio] = True
    distancia_total = 0
    
    # Seleccionamos n-1 ciudades más (ya tenemos la primera)
    for _ in range(n - 1):
        ciudad_actual = ruta[-1]
        siguiente_ciudad = None
        menor_distancia = float('inf')
        
        # Buscamos la ciudad no visitada más cercana a la ciudad actual
        for candidata in range(n):
            if not visitadas[candidata] and matriz_distancias[ciudad_actual][candidata] < menor_distancia:
                siguiente_ciudad = candidata
                menor_distancia = matriz_distancias[ciudad_actual][candidata]
        
        # Agregamos la ciudad más cercana a la ruta
        ruta.append(siguiente_ciudad)
        visitadas[siguiente_ciudad] = True
        distancia_total += menor_distancia
    
    # Agregamos la distancia de regreso a la ciudad inicial
    distancia_total += matriz_distancias[ruta[-1]][ciudad_inicio]
    ruta.append(ciudad_inicio)  # Completamos el ciclo
    
    return (ruta, distancia_total)

# Ejemplo de uso
if __name__ == "__main__":
    # Datos de ejemplo: 5 ciudades con sus coordenadas
    ciudades = [
        "Ciudad A", "Ciudad B", "Ciudad C", "Ciudad D", "Ciudad E"
    ]
    
    # Matriz de distancias entre ciudades
    matriz_distancias = [
        [0, 10, 15, 20, 25],
        [10, 0, 35, 25, 30],
        [15, 35, 0, 30, 40],
        [20, 25, 30, 0, 10],
        [25, 30, 40, 10, 0]
    ]
    
    ruta, distancia_total = ruta_viajante_vecino_cercano(ciudades, matriz_distancias)
    
    print("Ruta encontrada:")
    for i in ruta[:-1]:  # No imprimimos el último porque es igual al primero
        print(f" -> {ciudades[i]}", end="")
    print(f" -> {ciudades[ruta[0]]}")  # Regreso a la ciudad inicial
    
    print(f"Distancia total recorrida: {distancia_total}")