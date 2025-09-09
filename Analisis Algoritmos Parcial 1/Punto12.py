# Fusión Óptima de Archivos

import heapq

def fusion_optima_archivos(tamanios_archivos):
    """
    Calcula el costo mínimo para fusionar una lista de archivos.

    Args:
        tamanios_archivos: Una lista de enteros que representan los tamaños de los archivos.

    Returns:
        El costo total mínimo para fusionar todos los archivos.
    """
    # Usamos una cola de prioridad para mantener los tamaños de los archivos.
    # heapq en Python implementa una min-heap, lo cual es perfecto para obtener
    # los dos elementos más pequeños de manera eficiente.
    cola_prioridad = list(tamanios_archivos)
    heapq.heapify(cola_prioridad) # Convierte la lista en una cola de prioridad (heap)

    costo_total = 0

    # Continuamos fusionando mientras haya más de un archivo en la cola
    while len(cola_prioridad) > 1:
        # Extraer los dos archivos (o grupos) más pequeños
        archivo1 = heapq.heappop(cola_prioridad)
        archivo2 = heapq.heappop(cola_prioridad)

        # El costo de fusionar estos dos es la suma de sus tamaños
        costo_fusion_actual = archivo1 + archivo2

        # Añadir el costo de esta fusión al costo total
        costo_total += costo_fusion_actual

        # El resultado de la fusión es un nuevo "archivo" con el tamaño combinado
        # Añadir este nuevo "archivo" de vuelta a la cola de prioridad
        heapq.heappush(cola_prioridad, costo_fusion_actual)

    # Cuando solo queda un elemento en la cola, todos los archivos han sido fusionados.
    # El costo total acumulado es el costo mínimo.
    return costo_total

# --- Ejemplo de uso ---

# Tamaños de los archivos
tamanios = [4, 8, 2, 6]

# Calcular el costo mínimo de fusión
costo_minimo = fusion_optima_archivos(tamanios)

print(f"Tamaños de los archivos: {tamanios}")
print(f"Costo mínimo total para fusionar los archivos: {costo_minimo}")

# --- Otro ejemplo ---
tamanios2 = [1, 2, 3, 4, 5]
costo_minimo2 = fusion_optima_archivos(tamanios2)

print(f"\nTamaños de los archivos: {tamanios2}")
print(f"Costo mínimo total para fusionar los archivos: {costo_minimo2}")

