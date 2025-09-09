# Planificación de Paradas de un Vehículo (Problema de las Gasolineras)

# --- Ejemplo de uso  ---
d = 200 # distancia (kilometros) maxima que rinde el tanque del carro
d_T = 1000 # distancia total a recorrer
g = 7 # numero de gasolinerias
gasolinerias = [100, 150, 300, 450, 600, 750, 900] # arreglo con los kilometros donde se encuentra cada gasolineria
# --- Fin del ejemplo ---


# --- Para ingresar datos manualmente  ---
# d = int(input("Ingrese la distancia máxima que rinde el tanque: "))
# d_T = int(input("Ingrese la distancia total a recorrer: "))
# g = int(input("Ingrese el número de gasolineras: "))
# gasolinerias = []
# print(f"Ingrese las distancias de las {g} gasolineras:")
# for i in range(g):
#     gasolinerias.append(int(input()))
# --- Fin de la entrada manual ---

print("--- Datos del Ejemplo ---")
print(f"Distancia máxima del tanque (d): {d}")
print(f"Distancia total a recorrer (d_T): {d_T}")
print(f"Número de gasolineras (g): {g}")
print(f"Ubicaciones de las gasolineras: {gasolinerias}")
print("-------------------------")


# Plan de Viaje minimizando paradas
gasolinerias.sort() # Asegurarse de que las gasolineras estén ordenadas por distancia

distancia_actual = 0  # Empezar en el inicio (distancia 0)
paradas = []            # Lista para almacenar las ubicaciones de las paradas

# Añadir el destino como una parada potencial para simplificar la lógica
gasolinerias.append(d_T)

i = 0 # Índice para las gasolineras

while distancia_actual < d_T:
    # Encontrar la gasolinera más lejana alcanzable desde la distancia_actual
    alcanzable_mas_lejana = distancia_actual + d
    siguiente_parada = -1

    # Iterar a través de las gasolineras para encontrar la más lejana alcanzable
    while i < len(gasolinerias) and gasolinerias[i] <= alcanzable_mas_lejana:
        siguiente_parada = gasolinerias[i]
        i += 1

    # Si no hay gasolinera alcanzable y no hemos llegado al destino
    if siguiente_parada <= distancia_actual and distancia_actual < d_T:
        print("Es imposible llegar al destino.")
        paradas = [] # Limpiar las paradas ya que el viaje es imposible
        break

    # Si el punto más lejano alcanzable es el destino o más allá
    if siguiente_parada == d_T:
        distancia_actual = d_T
        break # Se llegó al destino

    # Añadir la gasolinera seleccionada a la lista de paradas
    paradas.append(siguiente_parada)
    distancia_actual = siguiente_parada # Moverse a la gasolinera seleccionada

print("\nParadas óptimas:", paradas)
