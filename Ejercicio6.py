# EJERCICIO 6: GESTOR DE TEMPERATURAS

# ENTRADA:
# - Varias temperaturas.

# PROCESO:
# 1. Crear la clase GestorTemperatura.
# 2. Crear una lista para almacenar las temperaturas.
# 3. Crear registrar_temperatura(temp).
# 4. Agregar la temperatura a la lista.
# 5. Crear minimo() para obtener la temperatura menor.
# 6. Crear maximo() para obtener la temperatura mayor.
# 7. Crear promedio() para calcular el promedio.
# 8. Recorrer las temperaturas y sumarlas.
# 9. Dividir la suma para la cantidad de temperaturas.
# 10. Crear registrar_multiples(*temps).
# 11. Recorrer las temperaturas recibidas.
# 12. Utilizar registrar_temperatura() para guardar cada una.

# SALIDA:
# - Temperatura mínima.
# - Temperatura máxima.
# - Promedio de las temperaturas.

#BOSQUEJO:
# INICIO

#     Crear clase GestorTemperatura

#         Crear constructor __init__()

#             Crear lista vacía para almacenar las temperaturas

#         Método registrar_temperatura(temp)

#             Recibir una temperatura

#             Agregar la temperatura a la lista

#         Método minimo()

#             Obtener la temperatura menor de la lista

#             Retornar la temperatura mínima

#         Método maximo()

#             Obtener la temperatura mayor de la lista

#             Retornar la temperatura máxima

#         Método promedio()

#             Crear variable suma = 0

#             Recorrer las temperaturas almacenadas

#                 Sumar cada temperatura a suma

#             Dividir suma para la cantidad de temperaturas

#             Retornar el promedio

#         Método registrar_multiples(*temps)

#             Recibir varias temperaturas

#             Recorrer cada temperatura

#                 Utilizar registrar_temperatura()

#     Crear objeto GestorTemperatura

#     Registrar varias temperaturas

#     Obtener la temperatura mínima

#     Obtener la temperatura máxima

#     Calcular el promedio

#     Mostrar los tres resultados

# FIN

class  GestorTemperatura:
    def __init__(self):
        self.temperaturas = []
        
    def registrar_temperatura(self, temp):
        
        self.temperaturas.append(temp)
        
    def minimo(self):
        return min(self.temperaturas)
    
    def maximo (self):
        return max(self.temperaturas)
    
    def promedio(self):
        suma=0
        for i in self.temperaturas:
            suma+= i
        return suma/len(self.temperaturas)
    def registrar_multiples(self, *temps):
        for c in temps:
            self.registrar_temperatura(c)

gt= GestorTemperatura()

gt.registrar_multiples(10, 34, 54, 67)

print(f"El minimo es: {gt.minimo()}")
print(f"El maximo es: {gt.maximo()}")
print(f"El promedio es: {gt.promedio()}")
             
