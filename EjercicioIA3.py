# EJERCICIO 3: GESTOR DE PRODUCTOS
#
# ENTRADA:
# - Nombre y precio de productos.
# - Precio mínimo.
#
# PROCESO:
# 1. Crear un diccionario para relacionar producto y precio.
# 2. Registrar productos usando un método individual.
# 3. Permitir registrar varios productos con *productos.
# 4. Recorrer el diccionario para encontrar productos que alcancen el precio mínimo.
# 5. Calcular el promedio de precios.
#
# SALIDA:
# - Productos cuyo precio cumple la condición.
# - Promedio de precios.
#
# BOSQUEJO:
# INICIO
#     Crear clase GestorProductos
#         Crear diccionario catalogo
#
#         Método agregar_producto(nombre, precio)
#             Guardar nombre como clave
#             Guardar precio como valor
#
#         Método agregar_multiples(*productos)
#             Recorrer productos
#                 Separar nombre y precio
#                 Llamar a agregar_producto()
#
#         Método productos_caros(precio_minimo)
#             Crear lista resultado
#             Recorrer catalogo
#                 Si precio >= precio_minimo
#                     Agregar nombre
#             Retornar resultado
#
#         Método precio_promedio()
#             Si no hay productos
#                 Retornar 0
#             Sumar todos los valores
#             Dividir para cantidad de productos
#             Retornar promedio
#     Crear objeto
#     Registrar productos
#     Mostrar resultados
# FIN

class GestorProductos:
    def __init__(self):
        self.catalogo = {}

    def agregar_producto(self, nombre, precio):
        self.catalogo[nombre] = precio

    def agregar_multiples(self, *productos):
        for datos in productos:
            nombre, precio = datos
            self.agregar_producto(nombre, precio)

    def productos_caros(self, precio_minimo):
        resultado = []

        for nombre in self.catalogo:
            if self.catalogo[nombre] >= precio_minimo:
                resultado.append(nombre)

        return resultado

    def precio_promedio(self):
        if len(self.catalogo) == 0:
            return 0

        return sum(self.catalogo.values()) / len(self.catalogo)


productos = GestorProductos()
productos.agregar_multiples(
    ("Cuaderno", 2.50),
    ("Mochila", 25.00),
    ("Calculadora", 12.00)
)

print("Productos desde $10:", productos.productos_caros(10))
print("Promedio:", productos.precio_promedio())
