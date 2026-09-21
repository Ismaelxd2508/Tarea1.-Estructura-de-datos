# EJERCICIO 19: GESTOR DE INVENTARIO

# ENTRADA:
# - Nombre del producto.
# - Cantidad de productos.
# - Cantidad mínima de stock.

# PROCESO:
# 1. Crear la clase Inventario.
# 2. Crear un diccionario para almacenar productos y cantidades.
# 3. Crear agregar_stock(producto, cantidad).
# 4. Comprobar si el producto ya existe.
# 5. Si existe, aumentar su cantidad.
# 6. Si no existe, crear el producto con su cantidad.
# 7. Crear restar_stock(producto, cantidad).
# 8. Comprobar si el producto existe y tiene suficiente stock.
# 9. Restar la cantidad cuando se cumplen las condiciones.
# 10. Retornar verdadero o falso según el resultado.
# 11. Crear productos_bajo_stock(minimo).
# 12. Recorrer los productos y sus cantidades.
# 13. Guardar los productos cuya cantidad sea menor al mínimo.

# SALIDA:
# - Verdadero o falso al realizar una resta de stock.
# - Lista de productos con bajo stock.

#BOSQUEJO:
# INICIO

#     Crear clase Inventario

#         Crear constructor __init__()

#             Crear diccionario vacío para almacenar el stock

#         Método agregar_stock(producto, cantidad)

#             Recibir producto y cantidad

#             Verificar si el producto ya existe

#             Si existe

#                 Aumentar su cantidad

#             Si no existe

#                 Crear el producto con la cantidad recibida

#         Método restar_stock(producto, cantidad)

#             Recibir producto y cantidad

#             Verificar si el producto existe

#             Verificar si hay suficiente stock

#             Si ambas condiciones se cumplen

#                 Restar la cantidad del stock

#                 Retornar verdadero

#             Si no

#                 Retornar falso

#         Método productos_bajo_stock(minimo)

#             Crear lista vacía llamada resultado

#             Recorrer productos y cantidades

#                 Comparar la cantidad con el mínimo

#                 Si la cantidad es menor

#                     Agregar el producto a resultado

#             Retornar la lista

#     Crear objeto Inventario

#     Agregar stock de un producto

#     Restar una cantidad del stock

#     Mostrar el resultado de la operación

#     Buscar productos con stock menor al mínimo

#     Mostrar los productos encontrados

# FIN

class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] += cantidad
        else:
            self.stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True
        else:
            return False

    def productos_bajo_stock(self, minimo):
        resultado = []

        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                resultado.append(producto)

        return resultado


inv = Inventario()

inv.agregar_stock("pan", 50)

print(inv.restar_stock("pan", 30))

print(inv.productos_bajo_stock(25))
