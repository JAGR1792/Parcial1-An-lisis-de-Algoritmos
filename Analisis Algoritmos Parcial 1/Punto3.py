"""Problema de la Mochila Fraccional"""

def mochila_fraccional(pesos, valores, capacidad):
    """
    pesos: lista de pesos de los items
    valores: lista de valores de los items
    capacidad: capacidad máxima de la mochila
    """
    # Calcular ratio valor/peso
    items = [(valores[i] / pesos[i], pesos[i], valores[i], i)
             for i in range(len(pesos))]

    # Ordenar por ratio descendente
    items.sort(key=lambda x: x[0], reverse=True)

    valor_total = 0
    mochila = [0] * len(pesos)

    for ratio, peso, valor, idx in items:
        if capacidad >= peso:
            # Tomar el item completo
            mochila[idx] = 1
            valor_total += valor
            capacidad -= peso
        else:
            # Tomar fracción del item
            fraccion = capacidad / peso
            mochila[idx] = fraccion
            valor_total += valor * fraccion
            break

    return mochila, valor_total

# Ejemplo de uso
pesos = [10, 20, 30]
valores = [60, 100, 120]
capacidad = 50
mochila, valor = mochila_fraccional(pesos, valores, capacidad)
print(f"Mochila: {mochila}")
print(f"Valor total: {valor}")

