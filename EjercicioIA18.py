# EJERCICIO 18: CALCULADOR DE TIEMPO
#
# ENTRADA:
# - Distancia y velocidad.
# - Varios viajes como tuplas.
#
# PROCESO:
# 1. Crear una lista para guardar los tiempos calculados.
# 2. Aplicar tiempo = distancia / velocidad.
# 3. Registrar cada resultado.
# 4. Revisar los viajes y comparar sus tiempos.
# 5. Guardar el viaje con el menor tiempo.
#
# SALIDA:
# - Tiempo calculado.
# - Viaje más corto.
# - Lista de tiempos.
#
# BOSQUEJO:
# INICIO
#     Crear clase CalculadorTiempo
#         Crear lista tiempos
#
#         Método calcular_tiempo(distancia, velocidad)
#             Si velocidad es 0
#                 Retornar 0
#             Calcular distancia / velocidad
#             Agregar tiempo a la lista
#             Retornar tiempo
#
#         Método viaje_mas_corto(referencia, *viajes)
#             Crear viaje_corto
#             Crear menor_tiempo
#             Recorrer viajes
#                 Separar distancia y velocidad
#                 Calcular tiempo
#                 Si es el primer viaje
#                     Guardarlo como menor
#                 Si tiempo actual < menor
#                     Actualizar menor
#             Retornar viaje_corto
#
#     Crear objeto
#     Calcular un tiempo
#     Buscar viaje más corto
#     Mostrar lista de tiempos
# FIN

class CalculadorTiempo:
    def __init__(self):
        self.tiempos = []

    def calcular_tiempo(self, distancia, velocidad):
        if velocidad == 0:
            return 0

        resultado = distancia / velocidad
        self.tiempos.append(resultado)
        return resultado

    def viaje_mas_corto(self, referencia, *viajes):
        viaje_corto = None
        menor_tiempo = None

        for distancia, velocidad in viajes:
            tiempo = self.calcular_tiempo(distancia, velocidad)

            if menor_tiempo is None:
                menor_tiempo = tiempo
                viaje_corto = (distancia, velocidad)
            elif tiempo < menor_tiempo:
                menor_tiempo = tiempo
                viaje_corto = (distancia, velocidad)

        return viaje_corto


tiempo = CalculadorTiempo()

print("Tiempo:", tiempo.calcular_tiempo(100, 50))
print("Viaje más corto:", tiempo.viaje_mas_corto(
    None, (100, 50), (120, 60), (200, 80)
))
print("Tiempos:", tiempo.tiempos)
