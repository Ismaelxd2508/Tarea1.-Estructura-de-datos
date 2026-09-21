# EJERCICIO 2: REGISTRO DE NÚMEROS
#
# ENTRADA:
# - Varios números.
#
# PROCESO:
# 1. Crear una clase RegistroNumeros.
# 2. Mantener una lista con todos los números.
# 3. Mantener un conjunto con los números repetidos eliminados.
# 4. Registrar números individuales o varios a la vez.
# 5. Obtener la cantidad total.
#
# SALIDA:
# - Cantidad total de registros.
# - Conjunto de números únicos.
#
# BOSQUEJO:
# INICIO
#     Crear clase RegistroNumeros
#         Crear lista registros
#         Crear conjunto valores_unicos
#
#         Método agregar_numero(numero)
#             Agregar numero a registros
#             Agregar numero a valores_unicos
#
#         Método agregar_multiples(*numeros)
#             Recorrer numeros
#                 Llamar a agregar_numero()
#
#         Método contar_numeros()
#             Retornar longitud de registros
#
#         Método mostrar_unicos()
#             Retornar valores_unicos
#
#     Crear objeto
#     Agregar varios números
#     Mostrar cantidad y únicos
# FIN

class RegistroNumeros:
    def __init__(self):
        self.registros = []
        self.valores_unicos = set()

    def agregar_numero(self, numero):
        self.registros.append(numero)
        self.valores_unicos.add(numero)

    def agregar_multiples(self, *numeros):
        for numero in numeros:
            self.agregar_numero(numero)

    def contar_numeros(self):
        cantidad = len(self.registros)
        return cantidad

    def mostrar_unicos(self):
        return self.valores_unicos


registro = RegistroNumeros()
registro.agregar_multiples(4, 8, 4, 2, 9, 8, 1, 5)

print("Cantidad:", registro.contar_numeros())
print("Únicos:", registro.mostrar_unicos())
