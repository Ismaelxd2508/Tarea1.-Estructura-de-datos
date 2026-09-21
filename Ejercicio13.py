# EJERCICIO 13: COMBINADOR DE LISTAS

# ENTRADA:
# - Dos listas.
# - Varias listas del mismo tamaño.

# PROCESO:
# 1. Crear la clase CombinadorListas.
# 2. Crear intercalar(lista1, lista2).
# 3. Crear una lista vacía para el resultado.
# 4. Recorrer las posiciones de la primera lista.
# 5. Agregar el elemento correspondiente de lista1.
# 6. Agregar el elemento correspondiente de lista2.
# 7. Crear intercalar_multiples(*listas).
# 8. Recorrer las posiciones de la primera lista.
# 9. Recorrer todas las listas recibidas.
# 10. Agregar el elemento de cada lista en la posición actual.

# SALIDA:
# - Lista con los elementos intercalados.

#BOSQUEJO:
# INICIO

#     Crear clase CombinadorListas

#         Método intercalar(lista1, lista2)

#             Crear lista vacía llamada lista

#             Recorrer las posiciones de lista1

#                 Agregar el elemento de lista1

#                 Agregar el elemento de lista2

#             Retornar la lista intercalada

#         Método intercalar_multiples(*listas)

#             Crear lista vacía llamada resultado

#             Recibir varias listas

#             Recorrer las posiciones de la primera lista

#                 Recorrer cada lista recibida

#                     Obtener el elemento de la posición actual

#                     Agregarlo a resultado

#             Retornar el resultado

#     Crear objeto CombinadorListas

#     Intercalar dos listas

#     Intercalar varias listas

#     Mostrar la lista intercalada

# FIN

class CombinadorListas:
    def  intercalar(self,lista1, lista2):
        lista=[]
        
        for i in range(len(lista1)):
            lista.append(lista1[i])
            lista.append(lista2[i])
        
        return lista
    
    def intercalar_multiples(self, *listas):
        resultado=[]
        
        for c in range(len(listas[0])):
            for num in listas:
                resultado.append(num[c])
        
        return resultado
    
cl= CombinadorListas()

cl.intercalar([1, 2], [3, 4])

print(f"El intercalado queda asi: {cl.intercalar_multiples([1, 2],[3, 4],[5, 6])}")
