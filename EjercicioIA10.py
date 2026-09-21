# EJERCICIO 10: PELÍCULAS
#
# ENTRADA:
# - Título y género de películas.
# - Título que se desea eliminar.
#
# PROCESO:
# 1. Crear una lista para almacenar tuplas.
# 2. Registrar cada película como (titulo, genero).
# 3. Recorrer las películas y seleccionar las de género Acción.
# 4. Crear una nueva lista sin la película que se desea eliminar.
#
# SALIDA:
# - Películas de acción.
# - Lista de películas después de eliminar.
#
# BOSQUEJO:
# INICIO
#     Crear clase Peliculas
#         Crear lista peliculas
#
#         Método agregar_pelicula(titulo, genero)
#             Crear tupla
#             Agregar tupla a la lista
#
#         Método peliculas_accion()
#             Crear lista acciones
#             Recorrer peliculas
#                 Obtener género
#                 Si género es "Accion"
#                     Agregar película
#             Retornar acciones
#
#         Método eliminar_pelicula(titulo)
#             Crear lista actualizada
#             Recorrer peliculas
#                 Si título es diferente al indicado
#                     Agregar película
#             Reemplazar lista original
#
#     Crear objeto
#     Agregar películas
#     Mostrar acciones
#     Eliminar una película
#     Mostrar lista
# FIN

class Peliculas:
    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self, titulo, genero):
        pelicula = (titulo, genero)
        self.peliculas.append(pelicula)

    def peliculas_accion(self):
        acciones = []

        for pelicula in self.peliculas:
            titulo, genero = pelicula

            if genero.lower() == "accion":
                acciones.append((titulo, genero))

        return acciones

    def eliminar_pelicula(self, titulo):
        restantes = []

        for pelicula in self.peliculas:
            if pelicula[0] != titulo:
                restantes.append(pelicula)

        self.peliculas = restantes


peliculas = Peliculas()
peliculas.agregar_pelicula("It", "Terror")
peliculas.agregar_pelicula("Fast and Fury", "Accion")
peliculas.agregar_pelicula("Pokemon", "Aventura")

print("Películas de acción:", peliculas.peliculas_accion())
peliculas.eliminar_pelicula("It")
print("Películas restantes:", peliculas.peliculas)
