# EJERCICIO 17: AGRUPADOR DE EDADES

# ENTRADA:
# - Varias edades.
# - Una categoría para consultar su promedio.

# PROCESO:
# 1. Crear la clase AgrupadorEdades.
# 2. Crear un diccionario para almacenar las categorías.
# 3. Crear clasificar_edad(edad).
# 4. Comprobar las condiciones de edad.
# 5. Retornar niño, adolescente, adulto o mayor.
# 6. Crear agrupar_por_categoria(*edades).
# 7. Reiniciar el diccionario de grupos.
# 8. Recorrer las edades recibidas.
# 9. Clasificar cada edad.
# 10. Crear una lista para una categoría si todavía no existe.
# 11. Agregar la edad a su categoría.
# 12. Crear edad_promedio_categoria(categoria).
# 13. Obtener las edades de la categoría.
# 14. Sumarlas y dividir para su cantidad.

# SALIDA:
# - Diccionario con las edades agrupadas.
# - Promedio de una categoría.

#BOSQUEJO:
# INICIO

#     Crear clase AgrupadorEdades

#         Crear constructor __init__()

#             Crear diccionario vacío para almacenar los grupos

#         Método clasificar_edad(edad)

#             Recibir una edad

#             Si la edad es menor que 12

#                 Retornar "niño"

#             Si no, si la edad es menor que 18

#                 Retornar "adolescente"

#             Si no, si la edad es menor que 60

#                 Retornar "adulto"

#             Si no

#                 Retornar "mayor"

#         Método agrupar_por_categoria(*edades)

#             Reiniciar el diccionario de grupos

#             Recibir varias edades

#             Recorrer cada edad

#                 Utilizar clasificar_edad()

#                 Obtener la categoría

#                 Si la categoría no existe

#                     Crear una lista vacía

#                 Agregar la edad a la lista de su categoría

#             Retornar los grupos

#         Método edad_promedio_categoria(categoria)

#             Obtener las edades de la categoría indicada

#             Crear variable suma = 0

#             Recorrer las edades

#                 Sumar cada edad

#             Dividir la suma para la cantidad de edades

#             Retornar el promedio

#     Crear objeto AgrupadorEdades

#     Agrupar varias edades

#     Mostrar los grupos

#     Calcular el promedio de una categoría

#     Mostrar el promedio

# FIN

class AgrupadorEdades:
    def __init__(self):
        self.grupos = {}
        
    def clasificar_edad(self, edad):
        if edad < 12:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 60:
            return "adulto"
        else:
            return "mayor"
    def agrupar_por_categoria(self, *edades):
        self.grupos={}
        
        for i in edades:
            categoria = self.clasificar_edad(i)

            if categoria not in self.grupos:
                self.grupos[categoria] = []

            self.grupos[categoria].append(i)

        return self.grupos
    
    def edad_promedio_categoria(self, categoria):
        edades = self.grupos[categoria]
        suma = 0

        for i in edades:
            suma += i

        return suma / len(edades)


ae = AgrupadorEdades()

print(ae.agrupar_por_categoria(5, 15, 30, 70))
print(ae.edad_promedio_categoria("adulto"))
            
