# EJERCICIO 20: ANALIZADOR DE PALABRAS
#
# ENTRADA:
# - Texto.
# - Inicio que deben tener las palabras buscadas.
#
# PROCESO:
# 1. Separar el texto en palabras.
# 2. Buscar las palabras que comiencen con el texto indicado.
# 3. Agrupar palabras utilizando su cantidad de caracteres como clave.
# 4. Crear un conjunto para eliminar palabras repetidas.
#
# SALIDA:
# - Lista de palabras que comienzan con el inicio.
# - Diccionario agrupado por longitud.
# - Conjunto de palabras únicas.
#
# BOSQUEJO:
# INICIO
#     Crear clase AnalizadorPalabras
#         Crear lista palabras
#
#         Método buscar_palabras(texto, inicio)
#             Separar texto
#             Crear lista resultado
#             Recorrer palabras
#                 Si comienza con inicio
#                     Agregar palabra
#             Retornar resultado
#
#         Método agrupar_por_longitud(texto)
#             Crear diccionario grupos
#             Recorrer palabras
#                 Obtener longitud
#                 Crear lista si no existe
#                 Agregar palabra al grupo
#             Retornar grupos
#
#         Método palabras_unicas(texto)
#             Separar palabras
#             Crear conjunto
#             Agregar cada palabra
#             Retornar conjunto
#
#     Crear objeto
#     Probar los métodos
#     Mostrar resultados
# FIN

class AnalizadorPalabras:
    def __init__(self):
        self.palabras = []

    def buscar_palabras(self, texto, inicio):
        resultado = []
        palabras = texto.split()

        for palabra in palabras:
            if palabra.startswith(inicio):
                resultado.append(palabra)

        return resultado

    def agrupar_por_longitud(self, texto):
        grupos = {}

        for palabra in texto.split():
            longitud = len(palabra)
            grupos.setdefault(longitud, [])
            grupos[longitud].append(palabra)

        return grupos

    def palabras_unicas(self, texto):
        unicas = set()

        for palabra in texto.split():
            unicas.add(palabra)

        return unicas


palabras = AnalizadorPalabras()

texto = "casa carro camino perro casa"

print("Comienzan con 'ca':", palabras.buscar_palabras(texto, "ca"))
print("Por longitud:", palabras.agrupar_por_longitud(texto))
print("Únicas:", palabras.palabras_unicas(texto))
