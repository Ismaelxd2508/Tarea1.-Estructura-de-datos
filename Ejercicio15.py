# EJERCICIO 15: BUSCADOR DE DIVISORES

# ENTRADA:
# - Uno o varios números.

# PROCESO:
# 1. Crear la clase DivisorFinder.
# 2. Crear encontrar_divisores(numero).
# 3. Crear una lista vacía para los divisores.
# 4. Recorrer los números desde 1 hasta el número recibido.
# 5. Comprobar si el número divide exactamente al valor.
# 6. Agregar los divisores encontrados.
# 7. Convertir la lista en una tupla.
# 8. Crear es_perfecto(numero).
# 9. Obtener los divisores del número.
# 10. Sumar los divisores excepto el mismo número.
# 11. Comparar la suma con el número.
# 12. Crear encontrar_multiples_divisores(*numeros).
# 13. Obtener los divisores de cada número.
# 14. Guardarlos en un diccionario.

# SALIDA:
# - Tupla de divisores.
# - Verdadero o falso según la comprobación de número perfecto.
# - Diccionario con números y sus divisores.

#BOSQUEJO:
# INICIO

#     Crear clase DivisorFinder

#         Método encontrar_divisores(numero)

#             Crear lista vacía

#             Recorrer desde 1 hasta el número

#                 Verificar si el número es divisible por el valor actual

#                 Si es divisible

#                     Agregar el valor a la lista

#             Convertir la lista en tupla

#             Retornar la tupla

#         Método es_perfecto(numero)

#             Obtener los divisores utilizando encontrar_divisores()

#             Crear variable suma = 0

#             Recorrer los divisores

#                 Ignorar el mismo número

#                 Sumar los demás divisores

#             Comparar la suma con el número

#             Si son iguales

#                 Retornar verdadero

#             Si no

#                 Retornar falso

#         Método encontrar_multiples_divisores(*numeros)

#             Crear diccionario vacío

#             Recorrer los números recibidos

#                 Obtener sus divisores

#                 Guardarlos asociados al número

#             Retornar el diccionario

#     Crear objeto DivisorFinder

#     Buscar los divisores de un número

#     Mostrar los divisores

#     Comprobar si un número es perfecto

#     Buscar divisores de varios números

#     Mostrar el diccionario resultante

# FIN

class DivisorFinder:
  
    def encontrar_divisores(self,numero):
        lista=[]
        for i in range(1,numero +1):
            if numero %i==0:
                lista.append(i)
        return tuple(lista)
    def  es_perfecto(self, numero):
        div= self.encontrar_divisores(numero)
        suma=0
        
        for c in div:
            if c != numero:
                suma+= c
        
        if suma == numero:
            return True
        else:
            return False
    def  encontrar_multiples_divisores(self,*numeros):
        resultado={}
        
        for i in numeros:
            resultado[i]= self.encontrar_divisores(i)
            
        return resultado
        
Df=DivisorFinder()
print(f"{Df.encontrar_divisores(12)}")
print(f"{Df.es_perfecto(6)}")       
print(f"{Df.encontrar_multiples_divisores(15,6,10)}")        
