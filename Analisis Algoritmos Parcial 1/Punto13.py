# Secuenciación de Tareas con Penalización por Retraso

def secuenciar_tareas(tareas):
    """
    Encuentra el orden de ejecución de tareas para minimizar la penalización total
    por retraso, asumiendo que cada unidad de retraso después de un "ideal"
    tiene una penalización fija por tarea.

    Args:
        tareas: Una lista de tuplas, donde cada tupla es (id_tarea, duracion, penalizacion_por_unidad_de_retraso).
                Asumimos que la penalización_por_unidad_de_retraso es por unidad de tiempo
                después de que el trabajo *debería* haber terminado si se ejecutara idealmente
                al inicio del proceso, y la duración es cuánto tarda el trabajo en sí.
                Minimizar la suma total de penalizaciones se logra ordenando por penalización
                descendente.

    Returns:
        Una tupla: (orden_ejecucion, penalizacion_total).
        orden_ejecucion: Lista de ids de tareas en el orden óptimo.
        penalizacion_total: La suma mínima de penalizaciones.
    """
    # El algoritmo greedy: ordenar las tareas por penalización descendente.
    # La penalización está en el índice 2 de la tupla.
    tareas_ordenadas = sorted(tareas, key=lambda tarea: tarea[2], reverse=True)

    orden_ejecucion = []
    tiempo_actual = 0  # El tiempo en el que termina la tarea anterior
    penalizacion_total = 0

    print("Ordenando tareas por penalización descendente:")
    for tarea in tareas_ordenadas:
        tarea_id, duracion, penalizacion = tarea
        print(f"  Tarea {tarea_id}: Duración={duracion}, Penalización por unidad={penalizacion}")

        # Añadir la tarea al orden de ejecución
        orden_ejecucion.append(tarea_id)

        # Calcular el tiempo en que termina esta tarea
        tiempo_finalizacion = tiempo_actual + duracion

        # Calcular el retraso de esta tarea.
        # Asumiendo que la "fecha de entrega ideal" es 0 para todas
        # y la penalización es por cada unidad de tiempo que la tarea termina *después* de 0.
        # En este modelo simplificado, el retraso de una tarea es el tiempo_finalizacion
        retraso = tiempo_finalizacion

        # Calcular la penalización por retraso para esta tarea
        penalizacion_tarea = retraso * penalizacion
        penalizacion_total += penalizacion_tarea

        # Actualizar el tiempo actual para la siguiente tarea
        tiempo_actual = tiempo_finalizacion

    return orden_ejecucion, penalizacion_total

# --- Ejemplo de uso ---
# Lista de tareas: (id_tarea, duracion, penalizacion_por_unidad_de_retraso)
tareas_ejemplo = [
    ('A', 2, 10),  # Tarea A: duración 2, penalización 10 por unidad de retraso
    ('B', 1, 30),  # Tarea B: duración 1, penalización 30 por unidad de retraso
    ('C', 3, 5)   # Tarea C: duración 3, penalización 5 por unidad de retraso
]

orden, penalizacion = secuenciar_tareas(tareas_ejemplo)

print(f"\nOrden de ejecución óptimo: {orden}")
print(f"Penalización total mínima: {penalizacion}")

# --- Otro ejemplo ---
tareas_ejemplo2 = [
    ('T1', 5, 20),
    ('T2', 2, 30),
    ('T3', 8, 10)
]

orden2, penalizacion2 = secuenciar_tareas(tareas_ejemplo2)

print(f"\nOrden de ejecución óptimo: {orden2}")
print(f"Penalización total mínima: {penalizacion2}")