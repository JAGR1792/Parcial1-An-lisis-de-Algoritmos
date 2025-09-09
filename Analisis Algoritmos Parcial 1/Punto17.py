def distribuir_tareas(tareas, num_servidores):
    """
    Asigna tareas a servidores para minimizar la carga máxima
    
    Args:
        tareas: Lista con el peso o tiempo de ejecución de cada tarea
        num_servidores: Numero de servidores disponibles
        
    Returns:
        Tupla (asignaciones, carga_maxima) donde:
        - asignaciones: Lista donde asignaciones[i] es el servidor asignado a la tarea i
        - carga_maxima: Carga máxima en cualquier servidor después de la asignación
    """
    # Inicializamos la carga de cada servidor a 0
    cargas_servidores = [0] * num_servidores
    asignaciones = []
    
    # Para cada tarea, la asignamos al servidor menos cargado
    for i, peso_tarea in enumerate(tareas):
        # Encontramos el servidor con la menor carga actual
        servidor_min_carga = cargas_servidores.index(min(cargas_servidores))
        
        # Asignamos la tarea a ese servidor
        asignaciones.append(servidor_min_carga)
        cargas_servidores[servidor_min_carga] += peso_tarea
    
    # La carga máxima es la del servidor más cargado
    carga_maxima = max(cargas_servidores)
    
    return (asignaciones, carga_maxima)

# Ejemplo de uso
if __name__ == "__main__":
    # Datos de ejemplo: lista de tareas con sus tiempos de ejecución
    tareas = [10, 15, 30, 20, 5, 25, 40, 10]
    num_servidores = 3
    
    asignaciones, carga_maxima = distribuir_tareas(tareas, num_servidores)
    
    # Mostramos la asignación de tareas por servidor
    cargas_por_servidor = [[] for _ in range(num_servidores)]
    for i, servidor in enumerate(asignaciones):
        cargas_por_servidor[servidor].append((i, tareas[i]))
    
    print("Asignación de tareas por servidor:")
    for i, tareas_servidor in enumerate(cargas_por_servidor):
        carga_total = sum(tarea[1] for tarea in tareas_servidor)
        print(f"Servidor {i}: Tareas {[tarea[0] for tarea in tareas_servidor]}, Carga total = {carga_total}")
    
    print(f"Carga máxima en cualquier servidor: {carga_maxima}")