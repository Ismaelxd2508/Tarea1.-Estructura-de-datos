# EJERCICIO 4: BÚSQUEDA DE NÚMEROS
#
# ENTRADA:
# - Varias listas de números.
# - Un límite.
#
# PROCESO:
# 1. Crear la clase BuscadorNumeros.
# 2. Filtrar los números que superen el límite.
# 3. Procesar varias listas reutilizando buscar_mayores().
# 4. Convertir cada lista en tupla para utilizarla como clave.
# 5. Guardar los resultados en un diccionario.
#
# SALIDA:
# - Lista de números mayores al límite.
# - Diccionario con las listas y sus resultados.
#
# BOSQUEJO:
# INICIO
#     Crear clase BuscadorNumeros
#
#         Método buscar_mayores(lista, limite)
#             Crear lista encontrados
#             Recorrer lista
#                 Si número > limite
#                     Agregar número
#             Retornar encontrados
#
#         Método buscar_multiples(limite, *listas)
#             Crear diccionario resultados
#             Recorrer cada lista
#                 Crear tupla con la lista
#                 Llamar a buscar_mayores()
#                 Guardar tupla y resultado
#             Retornar diccionario
#
#     Crear objeto
#     Buscar números de una lista
#     Buscar en varias listas
#     Mostrar resultados
# FIN

class BuscadorNumeros:
    def buscar_mayores(self, lista, limite):
        encontrados = []

        for numero in lista:
            if numero > limite:
                encontrados.append(numero)

        return encontrados

    def buscar_multiples(self, limite, *listas):
        resultados = {}

        for lista in listas:
            clave = tuple(lista)
            resultados[clave] = tuple(
                self.buscar_mayores(lista, limite)
            )

        return resultados


buscador = BuscadorNumeros()

datos1 = [2, 8, 5, 10, 3]
datos2 = [1, 6, 7, 4]

print("Mayores a 5:", buscador.buscar_mayores(datos1, 5))
print("Varias listas:", buscador.buscar_multiples(5, datos1, datos2))
