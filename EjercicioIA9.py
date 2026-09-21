# EJERCICIO 9: ANALIZADOR DE TEXTO
#
# ENTRADA:
# - Un texto.
#
# PROCESO:
# 1. Crear la clase AnalizadorTexto.
# 2. Comprobar las mayúsculas con es_mayuscula().
# 3. Recorrer carácter por carácter.
# 4. Contar mayúsculas, minúsculas y dígitos.
# 5. Comparar la longitud con el texto más largo guardado.
#
# SALIDA:
# - Diccionario de cantidades.
# - Texto más largo analizado.
#
# BOSQUEJO:
# INICIO
#     Crear clase AnalizadorTexto
#         Crear atributo texto_mas_largo
#
#         Método es_mayuscula(caracter)
#             Si caracter es una letra y está en mayúscula
#                 Retornar True
#             Si no
#                 Retornar False
#
#         Método contar_por_tipo(texto)
#             Crear diccionario contadores
#             Recorrer cada carácter
#                 Si es mayúscula
#                     Aumentar mayúsculas
#                 Si es letra
#                     Aumentar minúsculas
#                 Si es dígito
#                     Aumentar dígitos
#             Comparar longitud
#             Actualizar texto_mas_largo si corresponde
#             Retornar diccionario
#
#     Crear objeto
#     Analizar texto
#     Mostrar resultados
# FIN

class AnalizadorTexto:
    def __init__(self):
        self.texto_mas_largo = ""

    def es_mayuscula(self, caracter):
        return caracter.isalpha() and caracter.isupper()

    def contar_por_tipo(self, texto):
        conteo = {
            "mayusculas": 0,
            "minusculas": 0,
            "digitos": 0
        }

        for caracter in texto:
            if self.es_mayuscula(caracter):
                conteo["mayusculas"] += 1
            elif caracter.islower():
                conteo["minusculas"] += 1
            elif caracter.isdigit():
                conteo["digitos"] += 1

        if len(self.texto_mas_largo) < len(texto):
            self.texto_mas_largo = texto

        return conteo


analizador = AnalizadorTexto()

print("¿H es mayúscula?:", analizador.es_mayuscula("H"))
print("Conteo:", analizador.contar_por_tipo("Hola Mundo 2026!"))
print("Texto más largo:", analizador.texto_mas_largo)
