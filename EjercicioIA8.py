# EJERCICIO 8: CURSOS
#
# ENTRADA:
# - Nombres de cursos.
# - Nombres de estudiantes.
#
# PROCESO:
# 1. Crear un diccionario de cursos.
# 2. Cada curso tendrá una lista de estudiantes.
# 3. Registrar estudiantes en el curso correspondiente.
# 4. Contar estudiantes de cada curso.
# 5. Conservar el curso con la cantidad más alta.
#
# SALIDA:
# - Curso con mayor cantidad de estudiantes.
#
# BOSQUEJO:
# INICIO
#     Crear clase Cursos
#         Crear diccionario cursos
#
#         Método crear_curso(nombre_curso)
#             Crear lista vacía
#             Asociarla al nombre del curso
#
#         Método agregar_estudiante(curso, estudiante)
#             Si curso existe
#                 Agregar estudiante a su lista
#
#         Método curso_mayor_estudiantes()
#             Crear curso_mayor vacío
#             Crear cantidad_mayor = -1
#             Recorrer cursos
#                 Contar estudiantes
#                 Si cantidad > cantidad_mayor
#                     Actualizar cantidad_mayor
#                     Guardar nombre del curso
#             Retornar curso_mayor
#
#     Crear objeto
#     Crear cursos
#     Registrar estudiantes
#     Mostrar curso con mayor cantidad
# FIN

class Cursos:
    def __init__(self):
        self.cursos = {}

    def crear_curso(self, nombre_curso):
        self.cursos[nombre_curso] = list()

    def agregar_estudiante(self, curso, estudiante):
        estudiantes = self.cursos.get(curso)

        if estudiantes is not None:
            estudiantes.append(estudiante)

    def curso_mayor_estudiantes(self):
        curso_mayor = ""
        cantidad_mayor = -1

        for nombre, estudiantes in self.cursos.items():
            cantidad = len(estudiantes)

            if cantidad > cantidad_mayor:
                cantidad_mayor = cantidad
                curso_mayor = nombre

        return curso_mayor


cursos = Cursos()
cursos.crear_curso("Matemáticas")
cursos.crear_curso("Física")
cursos.crear_curso("Programación")

cursos.agregar_estudiante("Matemáticas", "Juan")
cursos.agregar_estudiante("Matemáticas", "Pedro")
cursos.agregar_estudiante("Física", "Ana")
cursos.agregar_estudiante("Programación", "Carlos")
cursos.agregar_estudiante("Programación", "Luis")
cursos.agregar_estudiante("Programación", "María")

print("Curso con más estudiantes:", cursos.curso_mayor_estudiantes())
