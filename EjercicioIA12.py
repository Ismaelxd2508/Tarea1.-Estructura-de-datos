# EJERCICIO 12: SELECTOR DE EDADES
#
# ENTRADA:
# - Inicio y fin de rangos de edades.
# - Varios rangos representados por tuplas.
#
# PROCESO:
# 1. Crear una tupla con las edades de un rango.
# 2. Recibir varios rangos.
# 3. Unir las edades utilizando un conjunto.
# 4. Eliminar automáticamente las edades repetidas.
# 5. Convertir el conjunto final en lista.
#
# SALIDA:
# - Tupla de un rango.
# - Lista de edades sin repetir.
#
# BOSQUEJO:
# INICIO
#     Crear clase SelectorEdades
#
#         Método crear_rango(inicio, fin)
#             Crear lista de edades
#             Recorrer range(inicio, fin + 1)
#                 Agregar edad
#             Convertir lista en tupla
#             Retornar tupla
#
#         Método edades_en_multiples_rangos(*rangos)
#             Crear conjunto edades
#             Recorrer rangos
#                 Crear rango
#                 Actualizar conjunto con las edades
#             Convertir conjunto en lista
#             Retornar lista
#
#     Crear objeto
#     Probar rango individual
#     Probar varios rangos
#     Mostrar resultados
# FIN

class SelectorEdades:
    def crear_rango(self, inicio, fin):
        edades = []

        for edad in range(inicio, fin + 1):
            edades.append(edad)

        return tuple(edades)

    def edades_en_multiples_rangos(self, *rangos):
        edades = set()

        for rango in rangos:
            inicio, fin = rango
            edades.update(self.crear_rango(inicio, fin))

        return sorted(list(edades))


selector = SelectorEdades()

print("Rango:", selector.crear_rango(10, 20))
print("Sin repetir:", selector.edades_en_multiples_rangos((10, 13), (12, 15)))
