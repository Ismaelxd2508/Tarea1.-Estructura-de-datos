# EJERCICIO 11: CONTADOR DE PRODUCTOS
#
# ENTRADA:
# - Nombres de productos registrados.
#
# PROCESO:
# 1. Crear un diccionario para contar repeticiones.
# 2. Al registrar un producto, obtener su cantidad actual.
# 3. Incrementar el contador.
# 4. Recorrer el diccionario para encontrar el mayor contador.
# 5. Consultar la cantidad de un producto.
#
# SALIDA:
# - Producto más registrado.
# - Cantidad de un producto específico.
#
# BOSQUEJO:
# INICIO
#     Crear clase ContadorProductos
#         Crear diccionario contador
#
#         Método agregar_producto(producto)
#             Obtener cantidad actual con get()
#             Sumar 1
#             Guardar nueva cantidad
#
#         Método producto_mas_registrado()
#             Crear nombre_mayor
#             Crear cantidad_mayor = 0
#             Recorrer contador
#                 Si cantidad > cantidad_mayor
#                     Actualizar nombre y cantidad
#             Retornar nombre_mayor
#
#         Método cantidad_producto(producto)
#             Buscar producto con get()
#             Si no existe
#                 Retornar 0
#             Retornar cantidad
#
#     Crear objeto
#     Registrar productos
#     Mostrar resultados
# FIN

class ContadorProductos:
    def __init__(self):
        self.contador = {}

    def agregar_producto(self, producto):
        cantidad = self.contador.get(producto, 0)
        self.contador[producto] = cantidad + 1

    def producto_mas_registrado(self):
        nombre_mayor = ""
        cantidad_mayor = 0

        for producto, cantidad in self.contador.items():
            if cantidad > cantidad_mayor:
                nombre_mayor = producto
                cantidad_mayor = cantidad

        return nombre_mayor

    def cantidad_producto(self, producto):
        return self.contador.get(producto, 0)


contador = ContadorProductos()

for producto in ("pan", "leche", "pan", "arroz", "pan", "leche"):
    contador.agregar_producto(producto)

print("Más registrado:", contador.producto_mas_registrado())
print("Cantidad de pan:", contador.cantidad_producto("pan"))
