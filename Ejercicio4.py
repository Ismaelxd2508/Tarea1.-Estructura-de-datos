# EJERCICIO 4: INVERSOR DE SECUENCIA

# ENTRADA:
# - Una o varias listas de elementos.

# PROCESO:
# 1. Crear la clase InversorSecuencia.
# 2. Crear invertir_lista(lista).
# 3. Crear una lista vacía para almacenar el resultado.
# 4. Recorrer la lista desde el último elemento hasta el primero.
# 5. Agregar cada elemento a la lista resultado.
# 6. Retornar la lista invertida.
# 7. Crear invertir_multiples(*listas).
# 8. Recorrer las listas recibidas.
# 9. Utilizar invertir_lista() para invertir cada lista.
# 10. Convertir la lista original y la invertida en tuplas.
# 11. Guardar ambas tuplas en un diccionario.

# SALIDA:
# - Una lista invertida.
# - Un diccionario con varias listas invertidas.

#BOSQUEJO:
# INICIO

#     Crear clase InversorSecuencia

#         Método invertir_lista(lista)

#             Crear lista vacía llamada resultado

#             Recorrer la lista desde el último elemento
#             hasta el primer elemento

#                 Agregar cada elemento a resultado

#             Retornar la lista invertida

#         Método invertir_multiples(*listas)

#             Crear diccionario vacío

#             Recibir varias listas

#             Recorrer cada lista

#                 Utilizar invertir_lista()

#                 Obtener la lista invertida

#                 Convertir la lista original en tupla

#                 Convertir la lista invertida en tupla

#                 Guardar ambas tuplas en el diccionario

#             Retornar el diccionario

#     Crear objeto InversorSecuencia

#     Invertir una lista

#     Mostrar la lista invertida

#     Invertir varias listas

#     Mostrar el diccionario con los resultados

# FIN

class InversorSecuencia:
   
        
    def  invertir_lista(self, lista):
        resultado=[]
        
        for i in range(len(lista) -1, -1, -1):
            resultado.append(lista[i])
        
        return resultado
    
    def invertir_multiples(self, *listas):
        
        dic={}
        
        for c in listas:
            
            Invertido = self.invertir_lista(c)
            dic[tuple(c)]= tuple(Invertido)
        
        return dic
            
Is= InversorSecuencia()


print(f"lista invertida: {Is.invertir_lista([1,2,3,4])}")
print(f"Diccionario Multiple: {Is.invertir_multiples([1, 2, 3, 4], [2, 3, 4])}")
