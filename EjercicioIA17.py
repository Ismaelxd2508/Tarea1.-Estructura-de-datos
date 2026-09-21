# EJERCICIO 17: AGRUPADOR DE TEMPERATURAS
#
# ENTRADA:
# - Varias temperaturas.
# - Una categoría.
#
# PROCESO:
# 1. Clasificar cada temperatura según los rangos indicados.
# 2. Crear un diccionario con las cuatro categorías.
# 3. Agregar cada temperatura a su categoría.
# 4. Buscar las temperaturas de una categoría.
# 5. Calcular su promedio.
#
# SALIDA:
# - Diccionario de categorías.
# - Promedio de una categoría.
#
# BOSQUEJO:
# INICIO
#     Crear clase AgrupadorTemperaturas
#         Crear diccionario agrupadas
#
#         Método clasificar_temperatura(temp)
#             Si temp < 15
#                 Retornar "fria"
#             Si temp <= 24
#                 Retornar "templada"
#             Si temp <= 34
#                 Retornar "calida"
#             Si no
#                 Retornar "caliente"
#
#         Método agrupar_por_categoria(*temperaturas)
#             Crear cuatro listas dentro del diccionario
#             Recorrer temperaturas
#                 Obtener categoría
#                 Agregar temperatura
#             Retornar diccionario
#
#         Método temperatura_promedio_categoria(categoria)
#             Obtener lista de la categoría
#             Si está vacía
#                 Retornar 0
#             Sumar temperaturas
#             Dividir para cantidad
#             Retornar promedio
#
#     Crear objeto
#     Agrupar temperaturas
#     Consultar promedio
# FIN

class AgrupadorTemperaturas:
    def __init__(self):
        self.agrupadas = {}

    def clasificar_temperatura(self, temp):
        if temp < 15:
            return "fria"
        elif temp <= 24:
            return "templada"
        elif temp <= 34:
            return "calida"
        return "caliente"

    def agrupar_por_categoria(self, *temperaturas):
        self.agrupadas = {
            "fria": [],
            "templada": [],
            "calida": [],
            "caliente": []
        }

        for temperatura in temperaturas:
            categoria = self.clasificar_temperatura(temperatura)
            self.agrupadas[categoria].append(temperatura)

        return self.agrupadas

    def temperatura_promedio_categoria(self, categoria):
        lista = self.agrupadas.get(categoria, [])

        if not lista:
            return 0

        return sum(lista) / len(lista)


temperaturas = AgrupadorTemperaturas()

print("Agrupación:", temperaturas.agrupar_por_categoria(10, 20, 28, 38))
print("Promedio cálido:", temperaturas.temperatura_promedio_categoria("calida"))
