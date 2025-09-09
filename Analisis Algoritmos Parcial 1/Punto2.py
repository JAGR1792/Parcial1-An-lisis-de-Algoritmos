"""Planificador de Tareas con Plazos y Beneficios"""

def planificar_tareas(tareas):
    """
    tareas: lista de tuplas (beneficio, plazo)
    """
    # Ordenar por beneficio descendente
    tareas.sort(key=lambda x: x[0], reverse=True)

    # Encontrar el plazo máximo
    plazo_max = max(plazo for _, plazo in tareas)

    # Inicializar slots de tiempo
    slots = [False] * (plazo_max + 1)
    plan = []
    beneficio_total = 0

    for beneficio, plazo in tareas:
        # Buscar slot disponible desde el plazo hacia atrás
        for i in range(min(plazo, plazo_max), 0, -1):
            if not slots[i]:
                slots[i] = True
                plan.append((beneficio, plazo, i))
                beneficio_total += beneficio
                break

    return plan, beneficio_total

# Ejemplo de uso
tareas = [(100, 2), (19, 1), (27, 2), (25, 1), (15, 3)]
plan, beneficio = planificar_tareas(tareas)
print(f"Plan: {plan}")
print(f"Beneficio total: {beneficio}")

