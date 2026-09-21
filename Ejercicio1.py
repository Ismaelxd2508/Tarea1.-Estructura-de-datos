# EJERCICIO 1: VALIDADOR DE NOTAS CON PROMEDIO

# ENTRADA:
# - Varias notas.

# PROCESO:
# 1. Crear la clase Calificador.
# 2. Crear una lista para almacenar las notas.
# 3. Crear validar_nota(nota).
# 4. Comprobar si la nota está entre 0 y 100.
# 5. Retornar verdadero si la nota es válida.
# 6. Retornar falso si la nota no es válida.
# 7. Crear cargar_notas(*args).
# 8. Recorrer todas las notas recibidas.
# 9. Utilizar validar_nota() para comprobar cada nota.
# 10. Agregar las notas válidas a la lista.
# 11. Crear promedio().
# 12. Recorrer las notas almacenadas y sumarlas.
# 13. Dividir la suma para la cantidad de notas.

# SALIDA:
# - Lista de notas válidas.
# - Promedio de las notas válidas.

#BOSQUEJO:
# INICIO

#     Crear clase Calificador

#         Crear constructor __init__()

#             Crear lista vacía para almacenar las notas

#         Método validar_nota(nota)

#             Recibir una nota

#             Verificar si la nota es mayor o igual a 0
#             y menor o igual a 100

#             Si la condición se cumple

#                 Retornar verdadero

#             Si no

#                 Retornar falso

#         Método cargar_notas(*args)

#             Recibir varias notas

#             Recorrer cada nota recibida

#                 Utilizar validar_nota()

#                 Si la nota es válida

#                     Agregar la nota a la lista

#             Retornar la lista de notas

#         Método promedio()

#             Crear variable suma = 0

#             Recorrer las notas almacenadas

#                 Sumar cada nota a suma

#             Dividir suma para la cantidad de notas

#             Retornar el promedio

#     Crear objeto Calificador

#     Cargar las notas

#     Mostrar las notas válidas

#     Calcular y mostrar el promedio

# FIN

class Calificador:
    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        if nota >= 0 and nota <= 100:
            return True
        else:
            return False

   
    def cargar_notas(self, *args):

        for nota in args:

            if self.validar_nota(nota):
                self.notas.append(nota)

        return self.notas

   
    def promedio(self):

        suma = 0

        for nota in self.notas:
            suma += nota

        return suma / len(self.notas)


c = Calificador()
print(c.cargar_notas(85, 92, 110, 78, -5, 88))
print(c.promedio())
 
