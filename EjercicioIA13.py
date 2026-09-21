# EJERCICIO 13: COMBINADOR DE NOMBRES
#
# ENTRADA:
# - Dos o más listas de nombres.
#
# PROCESO:
# 1. Crear una lista resultado.
# 2. Intercalar los elementos de dos listas mediante índices.
# 3. Permitir listas con diferentes tamaños.
# 4. Para varias listas, reutilizar intercalar().
#
# SALIDA:
# - Lista de nombres intercalados.
#
# BOSQUEJO:
# INICIO
#     Crear clase CombinadorNombres
#
#         Método intercalar(lista1, lista2)
#             Crear lista resultado
#             Determinar la lista más larga
#             Recorrer posiciones
#                 Si existe posición en lista1
#                     Agregar elemento
#                 Si existe posición en lista2
#                     Agregar elemento
#             Retornar resultado
#
#         Método intercalar_multiples(*listas)
#             Si no existen listas
#                 Retornar lista vacía
#             Copiar primera lista
#             Recorrer las demás listas
#                 Utilizar intercalar()
#                 Guardar nuevo resultado
#             Retornar resultado
#
#     Crear objeto
#     Crear listas
#     Mostrar combinaciones
# FIN

class CombinadorNombres:
    def intercalar(self, lista1, lista2):
        resultado = []
        posicion = 0

        while posicion < len(lista1) or posicion < len(lista2):
            if posicion < len(lista1):
                resultado.append(lista1[posicion])

            if posicion < len(lista2):
                resultado.append(lista2[posicion])

            posicion += 1

        return resultado

    def intercalar_multiples(self, *listas):
        if len(listas) == 0:
            return []

        resultado = list(listas[0])

        for lista in listas[1:]:
            resultado = self.intercalar(resultado, lista)

        return resultado


combinador = CombinadorNombres()

nombres1 = ["Ana", "Luis"]
nombres2 = ["Pedro", "Sofia"]
nombres3 = ["Carlos", "Maria"]

print("Dos listas:", combinador.intercalar(nombres1, nombres2))
print("Varias listas:", combinador.intercalar_multiples(
    nombres1, nombres2, nombres3
))
