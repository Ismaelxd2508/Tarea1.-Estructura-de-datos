# EJERCICIO 18: CÁLCULO DE DISTANCIAS

# ENTRADA:
# - Dos puntos representados como tuplas (x, y).
# - Un punto de referencia y varios puntos para comparar.

# PROCESO:
# 1. Crear la clase CalculadorDistancia.
# 2. Crear una lista para almacenar las distancias calculadas.
# 3. Crear distancia_euclidiana(p1, p2).
# 4. Obtener las coordenadas x e y del primer punto.
# 5. Obtener las coordenadas x e y del segundo punto.
# 6. Aplicar la fórmula de distancia euclidiana.
# 7. Guardar la distancia calculada.
# 8. Crear punto_mas_cercano(referencia, *puntos).
# 9. Recorrer los puntos recibidos.
# 10. Calcular la distancia entre la referencia y cada punto.
# 11. Comparar las distancias.
# 12. Guardar el punto cuya distancia sea menor.

# SALIDA:
# - Distancia entre dos puntos.
# - Punto más cercano a la referencia.

#BOSQUEJO:
# INICIO

#     Crear clase CalculadorDistancia

#         Crear constructor __init__()

#             Crear lista vacía para almacenar las distancias

#         Método distancia_euclidiana(p1, p2)

#             Recibir dos puntos

#             Obtener x1 e y1 del primer punto

#             Obtener x2 e y2 del segundo punto

#             Aplicar la fórmula de distancia euclidiana

#             Guardar la distancia en la lista

#             Retornar la distancia

#         Método punto_mas_cercano(referencia, *puntos)

#             Crear punto_cercano = None

#             Crear distancia_menor = None

#             Recibir varios puntos

#             Recorrer cada punto

#                 Calcular su distancia respecto a la referencia

#                 Si no existe una distancia menor
#                 o la distancia actual es menor

#                     Actualizar distancia_menor

#                     Guardar el punto como punto_cercano

#             Retornar el punto_cercano

#     Crear objeto CalculadorDistancia

#     Calcular la distancia entre dos puntos

#     Mostrar la distancia

#     Buscar el punto más cercano a la referencia

#     Mostrar el punto encontrado

# FIN

class CalculadorDistancia:
    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]

        x2 = p2[0]
        y2 = p2[1]

        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        punto_cercano = None
        distancia_menor = None

        for c in puntos:
            distancia = self.distancia_euclidiana(referencia, c)

            if distancia_menor is None or distancia < distancia_menor:
                distancia_menor = distancia
                punto_cercano = c

        return punto_cercano


cd = CalculadorDistancia()

print(cd.distancia_euclidiana((0, 0), (3, 4)))

print(cd.punto_mas_cercano((0, 0),(3, 4),(1, 1),(5, 5)))
