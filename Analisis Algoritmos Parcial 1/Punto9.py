# Implementación del algoritmo de Gale-Shapley
parejas = {} # Diccionario para almacenar las parejas: hombre -> mujer
hombres_solteros = list(preferencias_hombres.keys()) # Lista de hombres solteros
propuestas = {hombre: 0 for hombre in preferencias_hombres.keys()} # Índice de la próxima mujer a la que cada hombre propondrá

print("\nEjecutando el algoritmo de Gale-Shapley:")

while hombres_solteros:
    hombre = hombres_solteros[0] # Tomar el primer hombre soltero

    # Encontrar la mujer a la que este hombre quiere proponer ahora
    indice_mujer = propuestas[hombre]
    if indice_mujer >= n:
        # Esto no debería pasar en un caso típico si hay una solución
        print(f"Hombre {hombre} se ha quedado sin mujeres para proponer.")
        hombres_solteros.pop(0)
        continue

    mujer = preferencias_hombres[hombre][indice_mujer]
    print(f"Hombre {hombre} propone a Mujer {mujer}")

    # Incrementar el índice de propuestas de este hombre para la próxima vez
    propuestas[hombre] += 1

    # Verificar si la mujer está soltera
    if mujer not in parejas.values():
        # Si la mujer está soltera, se empareja con este hombre
        parejas[hombre] = mujer
        # Remover al hombre de la lista de solteros
        hombres_solteros.pop(0)
        print(f"Mujer {mujer} está soltera y acepta la propuesta de Hombre {hombre}.")
    else:
        # Si la mujer ya está emparejada, verificar si prefiere al nuevo hombre
        # Encontrar al hombre actual con el que está emparejada la mujer
        hombre_actual = [h for h, m in parejas.items() if m == mujer][0]

        # Usar el ranking inverso de la mujer para comparar preferencias
        # Si la mujer prefiere al nuevo hombre (ranking menor significa mayor preferencia)
        if ranking_mujeres[mujer][hombre] < ranking_mujeres[mujer][hombre_actual]:
            print(f"Mujer {mujer} prefiere a Hombre {hombre} sobre Hombre {hombre_actual}.")
            # La mujer acepta al nuevo hombre
            parejas[hombre] = mujer
            # El hombre anterior vuelve a estar soltero
            del parejas[hombre_actual]
            hombres_solteros.append(hombre_actual)
            # Remover al nuevo hombre de la lista de solteros
            hombres_solteros.pop(0)
            print(f"Mujer {mujer} acepta a Hombre {hombre}. Hombre {hombre_actual} vuelve a estar soltero.")
        else:
            # La mujer prefiere a su pareja actual
            print(f"Mujer {mujer} prefiere a Hombre {hombre_actual} sobre Hombre {hombre}. Hombre {hombre} es rechazado.")
            # El hombre que propuso sigue soltero y buscará a su siguiente preferencia en el próximo ciclo

# Imprimir las parejas estables
print("\nParejas Estables:")
for hombre, mujer in parejas.items():
    print(f"Hombre {hombre} - Mujer {mujer}")
