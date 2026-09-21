# EJERCICIO 7: GESTOR DE INVENTARIO
#
# ENTRADA:
# - Productos y sus precios.
# - Precio máximo.
#
# PROCESO:
# 1. Crear un diccionario para almacenar los productos.
# 2. Registrar cada producto con su precio.
# 3. Recorrer las claves y consultar sus valores.
# 4. Seleccionar los productos que no superen el precio máximo.
# 5. Calcular el promedio de los precios.
#
# SALIDA:
# - Productos económicos.
# - Promedio de precios.
#
# BOSQUEJO:
# INICIO
#     Crear clase GestorInventario
#         Crear diccionario inventario
#
#         Método agregar_producto(nombre, precio)
#             Guardar producto y precio
#
#         Método productos_economicos(precio_maximo)
#             Crear lista económicos
#             Recorrer nombres del inventario
#                 Obtener precio
#                 Si precio <= precio_maximo
#                     Agregar nombre
#             Retornar lista
#
#         Método precio_promedio()
#             Si no existen productos
#                 Retornar 0
#             Obtener todos los precios
#             Sumar precios
#             Dividir para cantidad
#             Retornar promedio
#
#     Crear objeto
#     Registrar productos
#     Mostrar resultados
# FIN

class GestorInventario:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, nombre, precio):
        self.inventario[nombre] = precio

    def productos_economicos(self, precio_maximo):
        economicos = []

        for nombre in self.inventario:
            precio = self.inventario[nombre]

            if precio <= precio_maximo:
                economicos.append(nombre)

        return economicos

    def precio_promedio(self):
        precios = list(self.inventario.values())

        if len(precios) == 0:
            return 0

        total = 0
        for precio in precios:
            total += precio

        return total / len(precios)


inventario = GestorInventario()
inventario.agregar_producto("Pan", 2.50)
inventario.agregar_producto("Leche", 3.00)
inventario.agregar_producto("Arroz", 5.00)
inventario.agregar_producto("Carne", 8.00)

print("Productos económicos:", inventario.productos_economicos(6))
print("Precio promedio:", inventario.precio_promedio())
