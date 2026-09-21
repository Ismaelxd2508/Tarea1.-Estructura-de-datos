# EJERCICIO 5: CLASIFICADOR DE NÚMEROS
#
# ENTRADA:
# - Varios números.
#
# PROCESO:
# 1. Crear listas para positivos y negativos.
# 2. Utilizar es_positivo() para clasificar cada número.
# 3. Guardar los resultados en las listas correspondientes.
# 4. Devolver las categorías en un diccionario.
# 5. Contar la cantidad de elementos de cada categoría.
#
# SALIDA:
# - Diccionario de positivos y negativos.
# - Tupla con sus cantidades.
#
# BOSQUEJO:
# INICIO
#     Crear clase ClasificadorNumeros
#         Crear lista positivos
#         Crear lista negativos
#
#         Método es_positivo(numero)
#             Si numero > 0
#                 Retornar True
#             Si no
#                 Retornar False
#
#         Método separar(*numeros)
#             Reiniciar listas
#             Recorrer números
#                 Si es_positivo(numero)
#                     Guardar en positivos
#                 Si no
#                     Guardar en negativos
#             Crear diccionario
#             Retornar diccionario
#
#         Método cantidad_positivos_negativos()
#             Contar cada lista
#             Retornar una tupla
#
#     Crear objeto
#     Separar números
#     Mostrar resultados
# FIN

class ClasificadorNumeros:
    def __init__(self):
        self.positivos = []
        self.negativos = []

    def es_positivo(self, numero):
        if numero > 0:
            return True
        return False

    def separar(self, *numeros):
        self.positivos.clear()
        self.negativos.clear()

        for numero in numeros:
            destino = self.positivos if self.es_positivo(numero) else self.negativos
            destino.append(numero)

        return {
            "positivos": self.positivos,
            "negativos": self.negativos
        }

    def cantidad_positivos_negativos(self):
        cantidades = (len(self.positivos), len(self.negativos))
        return cantidades


clasificador = ClasificadorNumeros()

print(clasificador.separar(5, -2, 8, -7, 3, -1))
print("Cantidades:", clasificador.cantidad_positivos_negativos())
print("¿5 es positivo?:", clasificador.es_positivo(5))
