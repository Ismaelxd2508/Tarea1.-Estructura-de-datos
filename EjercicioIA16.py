# EJERCICIO 16: TRANSFORMADOR DE CARACTERES
#
# ENTRADA:
# - Un carácter.
# - Una palabra.
#
# PROCESO:
# 1. Obtener el código numérico con ord().
# 2. Incrementar el código en una posición.
# 3. Convertir el nuevo código con chr().
# 4. Aplicar la función a cada letra de una palabra.
# 5. Unir los caracteres obtenidos.
#
# SALIDA:
# - Carácter siguiente.
# - Nueva palabra transformada.
#
# BOSQUEJO:
# INICIO
#     Crear clase TransformadorCaracteres
#         Crear diccionario transformaciones
#
#         Método convertir_caracter(caracter)
#             Obtener código con ord()
#             Incrementar código
#             Convertir con chr()
#             Retornar carácter
#
#         Método convertir_palabra(palabra)
#             Crear lista caracteres
#             Recorrer palabra
#                 Convertir cada carácter
#                 Agregar resultado
#             Unir caracteres
#             Guardar transformación
#             Retornar palabra nueva
#
#     Crear objeto
#     Transformar carácter
#     Transformar palabra
#     Mostrar resultados
# FIN

class TransformadorCaracteres:
    def __init__(self):
        self.transformaciones = {}

    def convertir_caracter(self, caracter):
        codigo = ord(caracter)
        return chr(codigo + 1)

    def convertir_palabra(self, palabra):
        caracteres = []

        for caracter in palabra:
            caracteres.append(self.convertir_caracter(caracter))

        nueva_palabra = "".join(caracteres)
        self.transformaciones[palabra] = nueva_palabra

        return nueva_palabra


transformador = TransformadorCaracteres()

print("Siguiente:", transformador.convertir_caracter("a"))
print("Palabra:", transformador.convertir_palabra("abc"))
