# EJERCICIO 7: GESTOR DE PERSONAS

# ENTRADA:
# - Nombres de personas.
# - Edades.
# - Una edad mínima.

# PROCESO:
# 1. Crear la clase GestorPersonas.
# 2. Crear un diccionario para almacenar nombre y edad.
# 3. Crear agregar_persona(nombre, edad).
# 4. Guardar cada persona y su edad.
# 5. Crear personas_mayores(edad_minima).
# 6. Recorrer el diccionario.
# 7. Comparar cada edad con la edad mínima.
# 8. Guardar los nombres que cumplen la condición.
# 9. Crear edad_promedio().
# 10. Recorrer las edades almacenadas y sumarlas.
# 11. Dividir la suma para la cantidad de personas.

# SALIDA:
# - Lista de personas que cumplen la edad mínima.
# - Promedio de edades.

#BOSQUEJO:
# INICIO

#     Crear clase GestorPersonas

#         Crear constructor __init__()

#             Crear diccionario vacío para almacenar personas y edades

#         Método agregar_persona(nombre, edad)

#             Recibir nombre y edad

#             Guardar la persona y su edad en el diccionario

#         Método personas_mayores(edad_minima)

#             Crear lista vacía llamada resultado

#             Recorrer nombres y edades

#                 Comparar la edad con la edad mínima

#                 Si la edad es mayor o igual

#                     Agregar el nombre a resultado

#             Retornar la lista de personas

#         Método edad_promedio()

#             Crear variable suma = 0

#             Recorrer las edades almacenadas

#                 Sumar cada edad

#             Dividir la suma para la cantidad de personas

#             Retornar el promedio

#     Crear objeto GestorPersonas

#     Agregar varias personas

#     Buscar personas que cumplen la edad mínima

#     Mostrar las personas encontradas

#     Calcular y mostrar la edad promedio

# FIN

class GestorPersonas:
    def __init__(self):
        self.personas = {}
    
    def agregar_persona(self,nombre, edad):
        self.personas[nombre]=edad
    
    def personas_mayores(self, edad_minima):
        resultado=[]
        
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)
        
        return resultado

    def edad_promedio(self):
        suma=0
        for i in self.personas.values():
            suma += i
        return suma/len(self.personas)
    
gp= GestorPersonas()

gp.agregar_persona("ismael",77)
gp.agregar_persona("israel",20)
gp.agregar_persona("Samuel",45)

print(f"personas mayores {gp.personas_mayores(25)}")

print(f"la edad promedio es{gp.edad_promedio()}")
