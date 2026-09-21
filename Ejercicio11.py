# EJERCICIO 11: CONTADOR DE FRECUENCIA

# ENTRADA:
# - Elementos individuales.

# PROCESO:
# 1. Crear la clase ContadorFrecuencia.
# 2. Crear un diccionario para almacenar elementos y frecuencias.
# 3. Crear agregar_elemento(elemento).
# 4. Comprobar si el elemento ya existe.
# 5. Si existe, aumentar su frecuencia.
# 6. Si no existe, iniciar su frecuencia en 1.
# 7. Crear elemento_mas_frecuente().
# 8. Recorrer los elementos y sus frecuencias.
# 9. Comparar las frecuencias para encontrar la mayor.
# 10. Crear frecuencia_elemento(elemento).
# 11. Consultar la frecuencia de un elemento.
# 12. Retornar 0 si el elemento no existe.

# SALIDA:
# - Elemento con mayor frecuencia.
# - Frecuencia de un elemento consultado.

#BOSQUEJO:
# INICIO

#     Crear clase ContadorFrecuencia

#         Crear constructor __init__()

#             Crear diccionario vacío para almacenar elementos y frecuencias

#         Método agregar_elemento(elemento)

#             Recibir un elemento

#             Verificar si el elemento ya existe

#             Si existe

#                 Aumentar su frecuencia en 1

#             Si no existe

#                 Crear el elemento con frecuencia 1

#         Método elemento_mas_frecuente()

#             Crear variable elemento_mayor = ""

#             Crear variable frecuencia_mayor = 0

#             Recorrer los elementos y sus frecuencias

#                 Comparar la frecuencia actual con frecuencia_mayor

#                 Si es mayor

#                     Actualizar frecuencia_mayor

#                     Guardar el elemento

#             Retornar el elemento_mayor

#         Método frecuencia_elemento(elemento)

#             Verificar si el elemento existe

#             Si existe

#                 Retornar su frecuencia

#             Si no

#                 Retornar 0

#     Crear objeto ContadorFrecuencia

#     Agregar varios elementos

#     Buscar el elemento más frecuente

#     Mostrar el elemento más frecuente

#     Consultar la frecuencia de un elemento

#     Mostrar su frecuencia

# FIN

class ContadorFrecuencia:
    def __init__(self):
        self.diccionario={}
    
    def  agregar_elemento(self, elemento):
        
        if elemento in self.diccionario:
            self.diccionario[elemento] += 1
        else:
            self.diccionario[elemento] = 1
    def elemento_mas_frecuente(self):
        
        elemento_mayor=""
        frecuencia_mayor=0
        
        for elementoM, frecuenciaM in  self.diccionario.items():
            if frecuenciaM > frecuencia_mayor:
                frecuencia_mayor= frecuenciaM
                elemento_mayor= elementoM
        
        return elemento_mayor
    def frecuencia_elemento(self, elemento):
        if elemento in self.diccionario:
            return self.diccionario[elemento]
        else:
            return 0
        
cf= ContadorFrecuencia()

cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("c")

print(f"El elemento mas frecuente es {cf.elemento_mas_frecuente()}")
print(f"la frecuencia es: {cf.frecuencia_elemento("a")}")
