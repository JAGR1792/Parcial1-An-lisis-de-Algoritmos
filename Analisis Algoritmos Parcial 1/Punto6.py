"""Cobertura de Conjuntos (Set Cover)"""

def set_cover(universo, conjuntos):
    """
    universo: conjunto de elementos a cubrir
    conjuntos: diccionario {nombre_conjunto: conjunto_elementos}
    """
    elementos_por_cubrir = set(universo)
    seleccionados = []

    while elementos_por_cubrir:
        # Encontrar el conjunto que cubre más elementos no cubiertos
        mejor_conjunto = None
        elementos_cubiertos = set()

        for nombre, conjunto in conjuntos.items():
            cubiertos = conjunto & elementos_por_cubrir
            if len(cubiertos) > len(elementos_cubiertos):
                mejor_conjunto = nombre
                elementos_cubiertos = cubiertos

        if mejor_conjunto is None:
            break

        seleccionados.append(mejor_conjunto)
        elementos_por_cubrir -= elementos_cubiertos

    return seleccionados

# Ejemplo de uso
universo = {1, 2, 3, 4, 5}
conjuntos = {
    'A': {1, 2, 3},
    'B': {2, 4},
    'C': {3, 4, 5},
    'D': {4, 5}
}

cobertura = set_cover(universo, conjuntos)
print(f"Cobertura mínima: {cobertura}")
