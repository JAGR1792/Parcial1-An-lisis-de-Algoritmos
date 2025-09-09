def ubicar_almacenes(ubicaciones_potenciales, clientes, costos_construccion, costos_transporte, k):
    """
    Determina dónde construir K almacenes y qué clientes asignar a cada uno.
    
    Args:
        ubicaciones_potenciales: Lista de ubicaciones donde se pueden construir almacenes
        clientes: Lista de ubicaciones de los clientes
        costos_construccion: Lista con el costo de construcción en cada ubicación
        costos_transporte: Matriz donde costos_transporte[i][j] es el costo de transporte
                          desde el almacén i hasta el cliente j
        k: Número de almacenes a construir
    
    Returns:
        Tupla (ubicaciones_elegidas, asignaciones) donde:
        - ubicaciones_elegidas: Lista de índices de ubicaciones elegidas
        - asignaciones: Lista donde asignaciones[i] es el almacén asignado al cliente i
    """
    n_ubicaciones = len(ubicaciones_potenciales)
    n_clientes = len(clientes)
    
    # Estrategia: elegir las k ubicaciones con mejor relación costo/beneficio
    # donde el beneficio es la suma de los ahorros en transporte para los clientes cercanos
    
    # Calculamos el valor (ahorro) de cada ubicación potencial
    valores_ubicaciones = []
    for i in range(n_ubicaciones):
        # Para cada ubicación, calculamos cuánto ahorraríamos en transporte
        ahorro = 0
        for j in range(n_clientes):
            # Consideramos como ahorro la diferencia entre el máximo costo y el costo actual
            costo_max = max(costos_transporte[loc][j] for loc in range(n_ubicaciones))
            ahorro += costo_max - costos_transporte[i][j]
        
        # El valor es el ahorro dividido por el costo de construcción
        valor = ahorro / costos_construccion[i] if costos_construccion[i] > 0 else float('inf')
        valores_ubicaciones.append((i, valor))
    
    # Ordenamos las ubicaciones por su valor (de mayor a menor)
    valores_ubicaciones.sort(key=lambda x: x[1], reverse=True)
    
    # Elegimos las k mejores ubicaciones
    ubicaciones_elegidas = [valores_ubicaciones[i][0] for i in range(k)]
    
    # Asignamos cada cliente al almacén más cercano (menor costo de transporte)
    asignaciones = []
    for j in range(n_clientes):
        mejor_almacen = min(ubicaciones_elegidas, key=lambda i: costos_transporte[i][j])
        asignaciones.append(mejor_almacen)
    
    return (ubicaciones_elegidas, asignaciones)

# Ejemplo de uso
if __name__ == "__main__":
    # Datos de ejemplo
    ubicaciones_potenciales = [(0, 0), (10, 10), (20, 20), (30, 30)]
    clientes = [(5, 5), (15, 15), (25, 25), (35, 35), (0, 20), (10, 30)]
    costos_construccion = [100, 120, 150, 200]
    
    # Calculamos costos de transporte basados en la distancia euclidiana
    costos_transporte = []
    for ubi in ubicaciones_potenciales:
        costos = []
        for cli in clientes:
            distancia = ((ubi[0] - cli[0])**2 + (ubi[1] - cli[1])**2)**0.5
            costos.append(distancia)
        costos_transporte.append(costos)
    
    # Queremos construir 2 almacenes
    k = 2
    
    ubicaciones, asignaciones = ubicar_almacenes(ubicaciones_potenciales, clientes, 
                                                costos_construccion, costos_transporte, k)
    
    print(f"Ubicaciones elegidas para los almacenes: {ubicaciones}")
    print(f"Asignación de clientes a almacenes: {asignaciones}")
    
    # Calculamos el costo total
    costo_total = sum(costos_construccion[i] for i in ubicaciones)
    for j, almacen in enumerate(asignaciones):
        costo_total += costos_transporte[almacen][j]
    
    print(f"Costo total: {costo_total}")