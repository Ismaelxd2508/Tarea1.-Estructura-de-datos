# EJERCICIO 16: CODIFICADOR CÉSAR

# ENTRADA:
# - Una letra o palabra en minúsculas.
# - Un número de desplazamiento.

# PROCESO:
# 1. Crear la clase CodificadorCesar.
# 2. Crear un diccionario para almacenar las codificaciones.
# 3. Crear codificar_letra(letra, desplazamiento).
# 4. Obtener el código ASCII de la letra mediante ord().
# 5. Calcular el nuevo código utilizando el desplazamiento.
# 6. Utilizar módulo 26 para mantener el resultado dentro del alfabeto.
# 7. Convertir el nuevo código en letra mediante chr().
# 8. Crear codificar_palabra(palabra, desplazamiento).
# 9. Recorrer la palabra letra por letra.
# 10. Codificar cada letra.
# 11. Guardar la palabra original y su resultado en el diccionario.

# SALIDA:
# - Palabra codificada.
# - Diccionario con el historial de codificaciones.

#BOSQUEJO:
# INICIO

#     Crear clase CodificadorCesar

#         Crear constructor __init__()

#             Crear diccionario vacío para almacenar las codificaciones

#         Método codificar_letra(letra, desplazamiento)

#             Recibir una letra y un desplazamiento

#             Obtener el código ASCII de la letra

#             Calcular el nuevo código usando el desplazamiento

#             Aplicar módulo 26

#             Convertir el nuevo código en una letra

#             Retornar la letra codificada

#         Método codificar_palabra(palabra, desplazamiento)

#             Crear cadena vacía llamada string

#             Recorrer cada letra de la palabra

#                 Utilizar codificar_letra()

#                 Agregar la letra codificada a string

#             Guardar la palabra original y la codificada en el diccionario

#             Retornar la palabra codificada

#     Crear objeto CodificadorCesar

#     Codificar una palabra con un desplazamiento

#     Mostrar la palabra codificada

#     Mostrar el historial de codificaciones

# FIN

class CodificadorCesar:
    def __init__(self):
        self.codigo= {}

    def codificar_letra(self, letra, desplazamiento):
        codigo = ord(letra)

        nuevo_codigo = (codigo - ord("a") + desplazamiento) % 26 + ord("a")

        return chr(nuevo_codigo)
    
    def codificar_palabra(self,palabra, desplazamiento):
        
        string= ""
        
        for i in palabra:
            string += self.codificar_letra(i, desplazamiento)
        
        self.codigo[palabra]= string
        
        return string 


cc = CodificadorCesar()

print(f"la palabra codificada: {cc.codificar_palabra("hola", 3)}")
print(f"El historial es: {cc.codigo}")
