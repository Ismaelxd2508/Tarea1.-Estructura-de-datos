# EJERCICIO 9: ANALIZADOR DE TEXTO POR TIPO DE CARÁCTER

# ENTRADA:
# - Un texto.

# PROCESO:
# 1. Crear la clase AnalizadorString.
# 2. Crear un atributo para almacenar el texto.
# 3. Crear solo_vocales(letra).
# 4. Crear una cadena con las vocales.
# 5. Comprobar si la letra pertenece a las vocales.
# 6. Crear contar_por_tipo(texto).
# 7. Crear un diccionario con contadores de vocales, consonantes y dígitos.
# 8. Recorrer cada carácter del texto.
# 9. Comprobar si el carácter es una vocal.
# 10. Si no es vocal, comprobar si es un dígito.
# 11. Si no es ninguna de las anteriores, aumentar el contador de consonantes.
# 12. Comparar la longitud del texto con el atributo texto_largo.
# 13. Guardar el texto si tiene mayor longitud.
#
# SALIDA:
# - Diccionario con vocales, consonantes y dígitos.
# - Texto más largo analizado.

#BOSQUEJO:
# INICIO

#     Crear clase AnalizadorString

#         Crear constructor __init__()

#             Crear atributo texto vacío

#         Método solo_vocales(letra)

#             Crear cadena con las vocales

#             Recibir una letra

#             Verificar si pertenece a las vocales

#             Si pertenece

#                 Retornar verdadero

#             Si no

#                 Retornar falso

#         Método contar_por_tipo(texto)

#             Crear diccionario resultado

#                 Crear contador de vocales = 0

#                 Crear contador de consonantes = 0

#                 Crear contador de dígitos = 0

#             Recorrer cada carácter del texto

#                 Utilizar solo_vocales()

#                 Si es vocal

#                     Aumentar contador de vocales

#                 Si no es vocal y es dígito

#                     Aumentar contador de dígitos

#                 Si no

#                     Aumentar contador de consonantes

#             Comparar la longitud del texto con texto_largo

#             Si el texto es más largo

#                 Guardar el texto como texto_largo

#             Retornar el diccionario resultado

#     Crear objeto AnalizadorString

#     Analizar un texto

#     Mostrar las cantidades de cada tipo de carácter

#     Mostrar el texto más largo

# FIN

class AnalizadorString:
    def __init__(self):
        self.texto=""
        
    def  solo_vocales(self,letra):
        
        vocales="aeiouAEIOU"
        
        if letra in vocales:
            return True
        else:
            return False
    
    def contar_por_tipo(self, texto):
        resultado = {
            "vocales": 0,
            "consonantes": 0,
            "digitos": 0
        }

        for i in texto:
            if self.solo_vocales(i):
                resultado["vocales"] += 1
            elif i.isdigit():
                resultado["digitos"] += 1
            else:
                resultado["consonantes"] += 1

        if len(texto) > len(self.texto_largo):
            self.texto_largo = texto

        return resultado


astr = AnalizadorString()

print(astr.contar_por_tipo("Holaa12346"))
print(f"Texto más largo: {astr.texto_largo}")
