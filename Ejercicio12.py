# EJERCICIO 12: RANGOS SIN DUPLICADOS

# ENTRADA:
# - Pares de números que representan inicio y fin de cada rango.

# PROCESO:
# 1. Crear la clase SelectorRange.
# 2. Crear crear_rango(inicio, fin).
# 3. Crear una lista vacía para el resultado.
# 4. Recorrer los números desde inicio hasta fin.
# 5. Agregar cada número a la lista.
# 6. Convertir la lista en una tupla.
# 7. Crear elementos_en_multiples_rangos(*rango).
# 8. Crear un conjunto vacío para evitar duplicados.
# 9. Recorrer todos los rangos recibidos.
# 10. Crear la tupla correspondiente a cada rango.
# 11. Agregar sus números al conjunto.
# 12. Convertir el conjunto en una lista.

# SALIDA:
# - Tupla con los números de un rango.
# - Lista con los números de varios rangos sin duplicados.

#BOSQUEJO:
# INICIO

#     Crear clase SelectorRange

#         Método crear_rango(inicio, fin)

#             Crear lista vacía llamada resultado

#             Recorrer los números desde inicio hasta fin

#                 Agregar cada número a resultado

#             Convertir resultado en tupla

#             Retornar la tupla

#         Método elementos_en_multiples_rangos(*rango)

#             Crear conjunto vacío llamado resultado_rangos

#             Recibir varios rangos

#             Recorrer cada rango

#                 Obtener inicio

#                 Obtener fin

#                 Utilizar crear_rango()

#                 Recorrer los números del rango

#                     Agregar cada número al conjunto

#             Convertir el conjunto en lista

#             Retornar la lista sin duplicados

#     Crear objeto SelectorRange

#     Crear y mostrar un rango

#     Combinar varios rangos

#     Eliminar los números repetidos mediante el conjunto

#     Mostrar la lista resultante

# FIN

class SelectorRange:
      
    def crear_rango(self,inicio,fin):
        resultado=[]
        
        for i in (range(inicio,fin +1)):
            resultado.append(i)
        
        return tuple(resultado)
        
        
    def elementos_en_multiples_rangos(self,*rango):
        resultado_rangos= set()
        
        for c in rango:
            inicio=c[0]
            fin=c[1]
            
            num_rangos=self.crear_rango(inicio, fin)
            
            for numero in num_rangos:
                resultado_rangos.add(numero)
                
        return list(resultado_rangos)
                
sr= SelectorRange()

print(f"el rango es: {sr.crear_rango(1,5)}")

print(f"Elementos combinados sin duplicacion:{sr.elementos_en_multiples_rangos((1,3),(2,4))}")           
