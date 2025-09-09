def maximizar_inversion(precios, retornos, presupuesto):
    """
    Determina cuántas acciones de cada tipo comprar para maximizar el retorno total.
    
    Args:
        precios: Lista con el precio de cada acción
        retornos: Lista con el retorno de inversión (ROI) esperado de cada acción
        presupuesto: Presupuesto total disponible
        
    Returns:
        Tupla (acciones_compradas, retorno_total) donde:
        - acciones_compradas: Lista donde acciones_compradas[i] es el número de acciones compradas del tipo i
        - retorno_total: El retorno total esperado de la inversión
    """
    n = len(precios)
    
    # Calculamos el ROI por unidad de inversión para cada acción
    roi_unitario = [(i, retornos[i] / precios[i]) for i in range(n)]
    
    # Ordenamos las acciones por ROI unitario (de mayor a menor)
    roi_unitario.sort(key=lambda x: x[1], reverse=True)
    
    acciones_compradas = [0] * n
    retorno_total = 0
    presupuesto_restante = presupuesto
    
    # Compramos primero las acciones con mayor ROI unitario
    for i, _ in roi_unitario:
        # Calculamos cuántas acciones podemos comprar
        cantidad_posible = presupuesto_restante // precios[i]
        
        # Compramos tantas acciones como sea posible
        acciones_compradas[i] = cantidad_posible
        retorno_total += cantidad_posible * retornos[i]
        presupuesto_restante -= cantidad_posible * precios[i]
    
    return (acciones_compradas, retorno_total)

# Ejemplo de uso
if __name__ == "__main__":
    # Datos de ejemplo
    precios = [10, 20, 30, 40, 50]
    retornos = [1, 3, 4, 5, 7]  # ROI por acción
    presupuesto = 500
    
    acciones, retorno = maximizar_inversion(precios, retornos, presupuesto)
    
    print("Plan de inversión:")
    for i in range(len(acciones)):
        if acciones[i] > 0:
            inversion = acciones[i] * precios[i]
            retorno_tipo = acciones[i] * retornos[i]
            print(f"Acción tipo {i+1}: Comprar {acciones[i]} acciones por ${inversion} (Retorno esperado: ${retorno_tipo})")
    
    presupuesto_usado = sum(acciones[i] * precios[i] for i in range(len(acciones)))
    print(f"\nPresupuesto utilizado: ${presupuesto_usado}/{presupuesto}")
    print(f"Retorno total esperado: ${retorno}")