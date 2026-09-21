# EJERCICIO 15: ANALIZADOR DE MÚLTIPLOS
#
# ENTRADA:
# - Número base.
# - Límite.
# - Varios números.
#
# PROCESO:
# 1. Crear una tupla con los múltiplos de un número.
# 2. Comprobar si un valor es divisible exactamente por el número.
# 3. Crear un diccionario para varios números.
# 4. Reutilizar encontrar_multiplos() en el diccionario.
#
# SALIDA:
# - Tupla de múltiplos.
# - Resultado booleano.
# - Diccionario de múltiplos.
#
# BOSQUEJO:
# INICIO
#     Crear clase AnalizadorMultiplos
#
#         Método encontrar_multiplos(numero, limite)
#             Crear lista vacía
#             Recorrer desde numero hasta numero * limite
#                 Avanzar de numero en numero
#                 Agregar cada valor
#             Convertir lista a tupla
#             Retornar tupla
#
#         Método es_multiplo(numero, valor)
#             Si numero no es cero
#                 Comprobar residuo
#                 Retornar True si es cero
#             Retornar False
#
#         Método encontrar_multiples_numeros(*numeros)
#             Crear diccionario
#             Recorrer números
#                 Llamar a encontrar_multiplos(numero, 10)
#                 Guardar resultado
#             Retornar diccionario
#
#     Crear objeto
#     Mostrar resultados
# FIN

class AnalizadorMultiplos:
    def encontrar_multiplos(self, numero, limite):
        valores = []

        for valor in range(numero, numero * limite + 1, numero):
            valores.append(valor)

        return tuple(valores)

    def es_multiplo(self, numero, valor):
        if numero == 0:
            return False

        return valor % numero == 0

    def encontrar_multiples_numeros(self, *numeros):
        resultado = {}

        for numero in numeros:
            resultado[numero] = self.encontrar_multiplos(numero, 10)

        return resultado


multiplos = AnalizadorMultiplos()

print("Múltiplos de 3:", multiplos.encontrar_multiplos(3, 10))
print("¿9 es múltiplo de 3?:", multiplos.es_multiplo(3, 9))
print("Varios:", multiplos.encontrar_multiples_numeros(2, 3, 5))
