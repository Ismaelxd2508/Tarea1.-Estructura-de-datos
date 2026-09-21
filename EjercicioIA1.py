# EJERCICIO 1: CONTROL DE EDADES
#
# ENTRADA:
# - Varias edades.
#
# PROCESO:
# 1. Crear la clase ControlEdades.
# 2. Guardar las edades aceptadas en una lista.
# 3. Validar cada edad mediante validar_edad().
# 4. Recorrer las edades recibidas con *args.
# 5. Calcular el promedio de las edades guardadas.
#
# SALIDA:
# - Lista de edades válidas.
# - Promedio de las edades válidas.
#
# BOSQUEJO:
# INICIO
#     Crear clase ControlEdades
#         Crear lista edades_validas
#
#         Método validar_edad(edad)
#             Si edad es mayor o igual a 0 Y menor o igual a 120
#                 Retornar True
#             En caso contrario
#                 Retornar False
#
#         Método cargar_edades(*edades)
#             Vaciar la lista de edades válidas
#             Recorrer las edades recibidas
#                 Si validar_edad(edad) es verdadero
#                     Agregar edad a la lista
#             Retornar lista
#
#         Método promedio()
#             Si no existen edades
#                 Retornar 0
#             Obtener la suma de las edades
#             Dividir suma para cantidad de edades
#             Retornar resultado
#
#     Crear objeto
#     Cargar edades
#     Mostrar lista y promedio
# FIN

class ControlEdades:
    def __init__(self):
        self.edades_validas = []

    def validar_edad(self, edad):
        return 0 <= edad <= 120

    def cargar_edades(self, *edades):
        self.edades_validas = []

        for edad in edades:
            if self.validar_edad(edad):
                self.edades_validas.append(edad)

        return self.edades_validas

    def promedio(self):
        if not self.edades_validas:
            return 0

        total = sum(self.edades_validas)
        return total / len(self.edades_validas)


control = ControlEdades()

print("Edades válidas:", control.cargar_edades(1, 45, 32, 52, 22, 18, 150, -3))
print("Promedio:", control.promedio())
