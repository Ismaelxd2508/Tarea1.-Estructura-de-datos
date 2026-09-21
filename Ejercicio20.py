# EJERCICIO 20: ANALIZADOR DE PATRONES

# ENTRADA:
# - Un texto.
# - Un patrón de búsqueda.

# PROCESO:
# 1. Crear la clase AnalizadorPatrones.
# 2. Crear una lista para almacenar las palabras.
# 3. Crear encontrar_palabras(texto, patron).
# 4. Separar el texto en palabras mediante split().
# 5. Recorrer las palabras.
# 6. Comprobar cuáles comienzan con el patrón mediante startswith().
# 7. Guardar las palabras que coinciden.
# 8. Crear agrupar_por_longitud(texto).
# 9. Separar el texto en palabras.
# 10. Obtener la longitud de cada palabra.
# 11. Crear una lista para cada longitud cuando sea necesario.
# 12. Guardar cada palabra según su longitud.
# 13. Guardar las palabras del texto en el atributo palabras.
# 14. Crear palabras_unicas().
# 15. Convertir las palabras almacenadas en un conjunto.

# SALIDA:
# - Lista de palabras que coinciden con el patrón.
# - Diccionario de palabras agrupadas por longitud.
# - Conjunto de palabras únicas.

#BOSQUEJO:
# INICIO

#     Crear clase AnalizadorPatrones

#         Crear constructor __init__()

#             Crear lista vacía para almacenar las palabras

#         Método encontrar_palabras(texto, patron)

#             Crear lista vacía llamada resultado

#             Separar el texto en palabras

#             Recorrer cada palabra

#                 Verificar si comienza con el patrón

#                 Si comienza con el patrón

#                     Agregar la palabra a resultado

#             Retornar la lista de palabras encontradas

#         Método agrupar_por_longitud(texto)

#             Crear diccionario vacío llamado resultado

#             Separar el texto en palabras

#             Recorrer cada palabra

#                 Obtener la longitud de la palabra

#                 Verificar si la longitud no existe en el diccionario

#                 Si no existe

#                     Crear una lista vacía para esa longitud

#                 Agregar la palabra a la lista correspondiente

#             Guardar las palabras en el atributo palabras

#             Retornar el diccionario

#         Método palabras_unicas()

#             Convertir el atributo palabras en un conjunto

#             Retornar el conjunto

#     Crear objeto AnalizadorPatrones

#     Buscar palabras que comienzan con un patrón

#     Mostrar las palabras encontradas

#     Agrupar las palabras según su longitud

#     Mostrar los grupos

#     Obtener las palabras únicas

#     Mostrar las palabras únicas

# FIN

class AnalizadorPatrones:
    def __init__(self):
        self.palabras = []

    def encontrar_palabras(self, texto, patron):
        resultado = []

        palabras = texto.split()

        for c in palabras:
            if c.startswith(patron):
                resultado.append(c)

        return resultado

    def agrupar_por_longitud(self, texto):
        resultado = {}

        palabras = texto.split()

        for palabra in palabras:
            longitud = len(palabra)

            if longitud not in resultado:
                resultado[longitud] = []

            resultado[longitud].append(palabra)

        self.palabras = palabras

        return resultado

    def palabras_unicas(self):
        return set(self.palabras)


ap = AnalizadorPatrones()

print(ap.encontrar_palabras("el gato está aquí", "ga"))

print(ap.agrupar_por_longitud("el gato está aquí"))

print(ap.palabras_unicas())
