# EJERCICIO 14: REGISTRO DE PRECIOS
#
# ENTRADA:
# - Producto y precio.
# - Precio máximo permitido.
#
# PROCESO:
# 1. Crear un diccionario de precios.
# 2. Registrar cada producto.
# 3. Buscar los productos cuyo precio no supere el máximo.
# 4. Recorrer los precios para encontrar el mayor.
#
# SALIDA:
# - Lista de productos económicos.
# - Tupla con el producto más caro y su precio.
#
# BOSQUEJO:
# INICIO
#     Crear clase RegistroPrecios
#         Crear diccionario precios
#
#         Método registrar(producto, precio)
#             Guardar producto y precio
#
#         Método productos_economicos(precio_maximo)
#             Crear lista resultado
#             Recorrer precios
#                 Si precio <= precio_maximo
#                     Agregar producto
#             Retornar lista
#
#         Método producto_mas_caro()
#             Si diccionario está vacío
#                 Retornar tupla vacía
#             Tomar primer producto como referencia
#             Recorrer productos restantes
#                 Si precio actual es mayor
#                     Actualizar producto y precio
#             Retornar tupla
#
#     Crear objeto
#     Registrar productos
#     Mostrar resultados
# FIN

class RegistroPrecios:
    def __init__(self):
        self.precios = {}

    def registrar(self, producto, precio):
        self.precios[producto] = precio

    def productos_economicos(self, precio_maximo):
        resultado = []

        for producto, precio in self.precios.items():
            if precio <= precio_maximo:
                resultado.append(producto)

        return resultado

    def producto_mas_caro(self):
        if not self.precios:
            return ()

        productos = list(self.precios.items())
        producto_mayor, precio_mayor = productos[0]

        for producto, precio in productos[1:]:
            if precio > precio_mayor:
                producto_mayor = producto
                precio_mayor = precio

        return (producto_mayor, precio_mayor)


precios = RegistroPrecios()
precios.registrar("Pan", 2.50)
precios.registrar("Leche", 3.00)
precios.registrar("Carne", 8.00)

print("Económicos:", precios.productos_economicos(3))
print("Más caro:", precios.producto_mas_caro())
