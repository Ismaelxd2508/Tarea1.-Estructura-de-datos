# EJERCICIO 19: ALMACÉN DE MATERIALES
#
# ENTRADA:
# - Material y cantidad para agregar.
# - Material y cantidad para retirar.
# - Cantidad mínima.
#
# PROCESO:
# 1. Crear un diccionario de existencias.
# 2. Registrar un material nuevo o sumar cantidad si ya existe.
# 3. Comprobar que exista suficiente cantidad antes de retirar.
# 4. Restar la cantidad solicitada.
# 5. Buscar materiales por debajo del mínimo.
#
# SALIDA:
# - True o False al retirar.
# - Lista de materiales con poca existencia.
#
# BOSQUEJO:
# INICIO
#     Crear clase AlmacenMateriales
#         Crear diccionario existencias
#
#         Método agregar_material(material, cantidad)
#             Obtener cantidad actual
#             Si existe
#                 Sumar nueva cantidad
#             Si no existe
#                 Crear material
#
#         Método retirar_material(material, cantidad)
#             Obtener cantidad disponible
#             Si cantidad disponible >= cantidad solicitada
#                 Restar cantidad
#                 Retornar True
#             Retornar False
#
#         Método materiales_bajo_cantidad(minimo)
#             Crear lista
#             Recorrer existencias
#                 Si cantidad < minimo
#                     Agregar material
#             Retornar lista
#
#     Crear objeto
#     Registrar materiales
#     Retirar material
#     Buscar materiales bajos
# FIN

class AlmacenMateriales:
    def __init__(self):
        self.existencias = {}

    def agregar_material(self, material, cantidad):
        actual = self.existencias.get(material, 0)
        self.existencias[material] = actual + cantidad

    def retirar_material(self, material, cantidad):
        disponible = self.existencias.get(material)

        if disponible is None:
            return False

        if disponible < cantidad:
            return False

        self.existencias[material] = disponible - cantidad
        return True

    def materiales_bajo_cantidad(self, minimo):
        bajos = []

        for material, cantidad in self.existencias.items():
            if cantidad < minimo:
                bajos.append(material)

        return bajos


almacen = AlmacenMateriales()

almacen.agregar_material("cuadernos", 20)
almacen.agregar_material("lapices", 50)
almacen.agregar_material("borradores", 10)

print("Retiro:", almacen.retirar_material("cuadernos", 15))
print("Bajo mínimo:", almacen.materiales_bajo_cantidad(10))
