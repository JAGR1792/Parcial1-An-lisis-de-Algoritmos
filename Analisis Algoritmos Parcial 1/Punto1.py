"""Problema del Cambio de Monedas (Sistema No Canónico)"""

def dar_cambio_greedy(denominaciones, cantidad):
    denominaciones.sort(reverse=True)
    cambio = []
    restante = cantidad

    for moneda in denominaciones:
        while restante >= moneda:
            cambio.append(moneda)
            restante -= moneda

    return cambio if restante == 0 else "No es posible dar cambio exacto"

# Ejemplo de uso
monedas = [25, 10, 5, 1]
print(f"Cambio para 48: {dar_cambio_greedy(monedas, 48)}")
print(f"Cambio para 15 (sistema no canónico): {dar_cambio_greedy([10, 7, 1], 15)}")
