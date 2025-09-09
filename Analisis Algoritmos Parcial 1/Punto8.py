# Asignación de Frecuencias a Torres de Celular

import collections

# --- Ejemplo de uso  ---
t = 6 # Número de torres de telefonía
nF = 6 # Número de frecuencias disponibles (puede ser un número grande inicialmente)
interferencias = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (4, 6), (5, 6)] # Lista de pares de torres que interfieren
# --- Fin del ejemplo ---


# --- Para ingresar datos manualmente  ---
# t = int(input("Ingrese el número de torres de telefonía: "))
# nF = int(input("Ingrese el número de frecuencias disponibles (puede ser un número grande inicialmente): "))
# nI = int(input("Ingrese el número de interferencias (pares de torres): "))
# interferencias = []
# print(f"Ingrese las {nI} pares de torres que interfieren (ejemplo: 1 2):")
# for i in range(nI):
#     while True:
#         try:
#             torre1, torre2 = map(int, input().split())
#             interferencias.append((torre1, torre2))
#             break # Salir del bucle while si la entrada es válida
#         except ValueError:
#             print("Entrada inválida. Por favor ingrese dos números separados por un espacio.")
# --- Fin de la entrada manual ---

print("--- Datos del Ejemplo ---")
print(f"Número de torres (t): {t}")
print(f"Número de frecuencias disponibles (nF): {nF}")
print(f"Interferencias (pares de torres): {interferencias}")
print("-------------------------")


# Construir la lista de adyacencia a partir de las interferencias
grafo = collections.defaultdict(list)
for torre1, torre2 in interferencias:
    grafo[torre1].append(torre2)
    grafo[torre2].append(torre1) # La interferencia es mutua

# Diccionario para almacenar la frecuencia asignada a cada torre
asignacion_frecuencias = {}

# Conjunto de frecuencias disponibles (empezamos con frecuencias de 0 en adelante)
# Asumimos un número máximo de frecuencias igual al número de torres inicialmente
frecuencias_disponibles = set(range(t))

# Ordenar las torres (puedes usar cualquier orden, pero un orden fijo ayuda a la reproducibilidad)
# Aquí usamos el orden de las claves en el diccionario del grafo
torres = sorted(list(set([t for pair in interferencias for t in pair]))) # Get unique towers from interferences and sort

print("\nAsignando frecuencias usando el algoritmo greedy:")

# Iterar a través de las torres
for torre in torres:
    # Conjunto para almacenar las frecuencias utilizadas por los vecinos de la torre actual
    frecuencias_vecinos = set()

    # Recorrer los vecinos de la torre actual
    for vecino in grafo[torre]:
        # Si el vecino ya tiene una frecuencia asignada, añadirla al conjunto de frecuencias de vecinos
        if vecino in asignacion_frecuencias:
            frecuencias_vecinos.add(asignacion_frecuencias[vecino])

    # Encontrar la frecuencia más baja disponible para la torre actual
    frecuencia_asignada = -1
    # Ordenar las frecuencias disponibles para encontrar la más baja
    for freq in sorted(list(frecuencias_disponibles)):
        if freq not in frecuencias_vecinos:
            frecuencia_asignada = freq
            break

    # Asignar la frecuencia encontrada a la torre actual
    asignacion_frecuencias[torre] = frecuencia_asignada

# Imprimir la asignación de frecuencias
print("\nAsignación de frecuencias (usando algoritmo greedy):")
for torre, frecuencia in asignacion_frecuencias.items():
    print(f"Torre {torre}: Frecuencia {frecuencia}")

# Calcular el número total de frecuencias distintas utilizadas
num_frecuencias_utilizadas = len(set(asignacion_frecuencias.values()))
print(f"\nNúmero total de frecuencias distintas utilizadas: {num_frecuencias_utilizadas}")

# Emparejamiento Estable (Problema de Matrimonio Estable)
# n = int(input("Ingrese el número de hombres y mujeres: "))

# --- Ejemplo de uso  ---
n = 4 # Número de hombres y mujeres

# Preferencias de los hombres (hombre: [lista de mujeres en orden de preferencia])
preferencias_hombres = {
    1: [4, 1, 2, 3],
    2: [2, 4, 3, 1],
    3: [4, 2, 3, 1],
    4: [1, 3, 4, 2]
}

# Preferencias de las mujeres (mujer: [lista de hombres en orden de preferencia])
preferencias_mujeres = {
    1: [4, 2, 1, 3],
    2: [2, 4, 3, 1],
    3: [1, 2, 4, 3],
    4: [3, 2, 1, 4]
}
# --- Fin del ejemplo ---


# --- Para ingresar datos manualmente ---
# # Leer preferencias de los hombres
# preferencias_hombres = {}
# print(f"\nIngrese las preferencias de los {n} hombres (del 1 al {n}).")
# print("Para cada hombre, ingrese la lista de mujeres en orden de preferencia (ej: 2 1 3):")
# for i in range(1, n + 1):
#     while True:
#         try:
#             preferencias = list(map(int, input(f"Preferencias hombre {i}: ").split()))
#             if len(preferencias) == n and all(1 <= p <= n for p in preferencias) and len(set(preferencias)) == n:
#                 preferencias_hombres[i] = preferencias
#                 break
#             else:
#                 print("Entrada inválida. Asegúrese de ingresar los números del 1 al", n, "sin repetir y separados por espacios.")
#         except ValueError:
#             print("Entrada inválida. Por favor ingrese números separados por espacios.")


# # Leer preferencias de las mujeres
# preferencias_mujeres = {}
# print(f"\nIngrese las preferencias de las {n} mujeres (del 1 al {n}).")
# print("Para cada mujer, ingrese la lista de hombres en orden de preferencia (ej: 3 1 2):")
# # Para facilitar la búsqueda, crearemos un ranking inverso para las mujeres: mujer -> hombre -> ranking
# for i in range(1, n + 1):
#     while True:
#         try:
#             preferencias = list(map(int, input(f"Preferencias mujer {i}: ").split()))
#             if len(preferencias) == n and all(1 <= p <= n for p in preferencias) and len(set(preferencias)) == n:
#                 preferencias_mujeres[i] = preferencias
#                 break
#             else:
#                 print("Entrada inválida. Asegúrese de ingresar los números del 1 al", n, "sin repetir y separados por espacios.")
#         except ValueError:
#             print("Entrada inválida. Por favor ingrese números separados por espacios.")
# --- Fin de la entrada manual ---

# Para facilitar la búsqueda, crearemos un ranking inverso para las mujeres: mujer -> hombre -> ranking
ranking_mujeres = {}
for mujer, prefs in preferencias_mujeres.items():
     ranking_mujeres[mujer] = {hombre: rank for rank, hombre in enumerate(prefs)}


print("--- Datos del Ejemplo ---")
print(f"Número de hombres y mujeres (n): {n}")
print(f"Preferencias de los hombres: {preferencias_hombres}")
print(f"Preferencias de las mujeres: {preferencias_mujeres}")
print("-------------------------")


