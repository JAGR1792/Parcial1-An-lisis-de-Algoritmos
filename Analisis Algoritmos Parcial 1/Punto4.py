""" Selección de Actividades"""

def seleccion_actividades(actividades):
    """
    actividades: lista de tuplas (inicio, fin)
    """
    # Ordenar por hora de finalización
    actividades.sort(key=lambda x: x[1])

    seleccionadas = []
    ultimo_fin = 0

    for inicio, fin in actividades:
        if inicio >= ultimo_fin:
            seleccionadas.append((inicio, fin))
            ultimo_fin = fin

    return seleccionadas

# Ejemplo de uso
actividades = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (7, 9)]
seleccion = seleccion_actividades(actividades)
print(f"Actividades seleccionadas: {seleccion}")
print(f"Total: {len(seleccion)} actividades")

