def cargar_contenedores(pesos, beneficios, capacidad_maxima):
    """
    Decide qué contenedores cargar en el barco para maximizar el beneficio.
    
    Args:
        pesos: Lista con el peso de cada contenedor
        beneficios: Lista con el beneficio de cada contenedor
        capacidad_maxima: Capacidad máxima de peso del barco
        
    Returns:
        Tupla (contenedores_seleccionados, beneficio_total) donde:
        - contenedores_seleccionados: Lista de índices de los contenedores seleccionados
        - beneficio_total: Beneficio total obtenido
    """
    n = len(pesos)
    
    # Calculamos la relación beneficio/peso para cada contenedor
    relaciones = [(i, beneficios[i] / pesos[i]) for i in range(n)]
    
    # Ordenamos los contenedores por su relación beneficio/peso (de mayor a menor)
    relaciones.sort(key=lambda x: x[1], reverse=True)
    
    contenedores_seleccionados = []
    beneficio_total = 0
    peso_actual = 0
    
    # Intentamos incluir cada contenedor en orden de mejor relación beneficio/peso
    for i, _ in relaciones:
        if peso_actual + pesos[i] <= capacidad_maxima:
            contenedores_seleccionados.append(i)
            beneficio_total += beneficios[i]
            peso_actual += pesos[i]
    
    return (contenedores_seleccionados, beneficio_total)

# Ejemplo de uso
if __name__ == "__main__":
    # Datos de ejemplo
    pesos = [10, 20, 30, 40, 50]
    beneficios = [50, 120, 150, 210, 240]
    capacidad_maxima = 100
    
    contenedores, beneficio = cargar_contenedores(pesos, beneficios, capacidad_maxima)
    
    print("Contenedores seleccionados:")
    for i in contenedores:
        print(f"Contenedor {i+1}: Peso = {pesos[i]}, Beneficio = {beneficios[i]}")
    
    peso_total = sum(pesos[i] for i in contenedores)
    print(f"Peso total cargado: {peso_total}/{capacidad_maxima}")
    print(f"Beneficio total obtenido: {beneficio}")
