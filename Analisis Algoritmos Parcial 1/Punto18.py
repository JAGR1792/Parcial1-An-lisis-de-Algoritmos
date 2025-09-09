def calcular_solapamiento(s1, s2):
    """
    Encuentra el solapamiento máximo entre el final de s1 y el inicio de s2.
    
    Args:
        s1, s2: Dos cadenas de texto
        
    Returns:
        La longitud del solapamiento máximo
    """
    max_solapamiento = 0
    
    # Probamos todas las posibles longitudes de solapamiento
    for i in range(1, min(len(s1), len(s2)) + 1):
        if s1[-i:] == s2[:i]:
            max_solapamiento = i
    
    return max_solapamiento

def construir_supercadena_minima(cadenas):
    """
    Construye una supercadena mínima que contiene todas las cadenas dadas.
    
    Args:
        cadenas: Lista de cadenas de texto
        
    Returns:
        La supercadena construida
    """
    # Trabajamos con una copia para no modificar la entrada original
    cadenas_restantes = cadenas.copy()
    
    # Mientras haya más de una cadena, fusionamos las que tengan el mayor solapamiento
    while len(cadenas_restantes) > 1:
        max_solapamiento = -1
        mejor_par = (-1, -1)
        
        # Buscamos el par con el mayor solapamiento
        for i in range(len(cadenas_restantes)):
            for j in range(len(cadenas_restantes)):
                if i != j:
                    solapamiento = calcular_solapamiento(cadenas_restantes[i], cadenas_restantes[j])
                    if solapamiento > max_solapamiento:
                        max_solapamiento = solapamiento
                        mejor_par = (i, j)
        
        # Fusionamos las cadenas con mayor solapamiento
        i, j = mejor_par
        nueva_cadena = cadenas_restantes[i] + cadenas_restantes[j][max_solapamiento:]
        
        # Eliminamos las cadenas fusionadas y agregamos la nueva
        if i < j:
            cadenas_restantes.pop(j)
            cadenas_restantes.pop(i)
        else:
            cadenas_restantes.pop(i)
            cadenas_restantes.pop(j)
        
        cadenas_restantes.append(nueva_cadena)
    
    return cadenas_restantes[0]

# Ejemplo de uso
if __name__ == "__main__":
    # Datos de ejemplo
    cadenas = ["ABCD", "CDEF", "EFGH", "GHIJ"]
    
    supercadena = construir_supercadena_minima(cadenas)
    
    print(f"Cadenas originales: {cadenas}")
    print(f"Supercadena mínima: {supercadena}")
    
    # Verificamos que la supercadena contiene todas las cadenas originales
    print("\nVerificación:")
    for cadena in cadenas:
        if cadena in supercadena:
            print(f"'{cadena}' está contenida en la supercadena")
        else:
            print(f"ERROR: '{cadena}' no está contenida en la supercadena")
