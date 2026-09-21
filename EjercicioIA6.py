# EJERCICIO 6: GESTOR DE CALIFICACIONES
#
# ENTRADA:
# - Varias calificaciones.
#
# PROCESO:
# 1. Crear una lista de calificaciones.
# 2. Registrar cada nota mediante registrar_calificacion().
# 3. Permitir registrar varias notas.
# 4. Buscar manualmente la menor y la mayor.
# 5. Calcular el promedio.
#
# SALIDA:
# - Nota mínima.
# - Nota máxima.
# - Promedio.
#
# BOSQUEJO:
# INICIO
#     Crear clase GestorCalificaciones
#         Crear lista notas
#
#         Método registrar_calificacion(nota)
#             Agregar nota
#
#         Método registrar_multiples(*notas)
#             Recorrer notas
#                 Llamar a registrar_calificacion()
#
#         Método minima()
#             Tomar primera nota como menor
#             Recorrer notas restantes
#                 Si nota < menor
#                     Actualizar menor
#             Retornar menor
#
#         Método maxima()
#             Tomar primera nota como mayor
#             Recorrer notas restantes
#                 Si nota > mayor
#                     Actualizar mayor
#             Retornar mayor
#
#         Método promedio()
#             Sumar notas
#             Dividir para cantidad
#             Retornar resultado
#     Crear objeto
#     Registrar notas
#     Mostrar estadísticas
# FIN

class GestorCalificaciones:
    def __init__(self):
        self.notas = []

    def registrar_calificacion(self, nota):
        self.notas.append(nota)

    def registrar_multiples(self, *notas):
        for nota in notas:
            self.registrar_calificacion(nota)

    def minima(self):
        if not self.notas:
            return 0

        menor = self.notas[0]

        for nota in self.notas[1:]:
            if nota < menor:
                menor = nota

        return menor

    def maxima(self):
        if not self.notas:
            return 0

        mayor = self.notas[0]

        for nota in self.notas[1:]:
            if nota > mayor:
                mayor = nota

        return mayor

    def promedio(self):
        if not self.notas:
            return 0

        return sum(self.notas) / len(self.notas)


calificaciones = GestorCalificaciones()
calificaciones.registrar_multiples(10, 34, 54, 67)

print("Mínimo:", calificaciones.minima())
print("Máximo:", calificaciones.maxima())
print("Promedio:", calificaciones.promedio())
