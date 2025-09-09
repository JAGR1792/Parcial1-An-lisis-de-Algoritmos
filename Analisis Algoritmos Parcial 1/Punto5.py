"""Codificación de Huffman"""

import heapq
from collections import defaultdict

class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierdo = None
        self.derecho = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def construir_arbol_huffman(frecuencias):
    heap = [NodoHuffman(car, freq) for car, freq in frecuencias.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        izquierdo = heapq.heappop(heap)
        derecho = heapq.heappop(heap)

        merged = NodoHuffman(None, izquierdo.frecuencia + derecho.frecuencia)
        merged.izquierdo = izquierdo
        merged.derecho = derecho

        heapq.heappush(heap, merged)

    return heap[0]

def generar_codigos(raiz, codigo_actual="", codigos={}):
    if raiz is None:
        return

    if raiz.caracter is not None:
        codigos[raiz.caracter] = codigo_actual

    generar_codigos(raiz.izquierdo, codigo_actual + "0", codigos)
    generar_codigos(raiz.derecho, codigo_actual + "1", codigos)

    return codigos

# Ejemplo de uso
texto = "abracadabra"
frecuencias = defaultdict(int)
for char in texto:
    frecuencias[char] += 1

arbol = construir_arbol_huffman(frecuencias)
codigos = generar_codigos(arbol)
print("Códigos Huffman:", codigos)

