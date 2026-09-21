# EJERCICIO 5: ANALIZADOR DE NÚMEROS

# ENTRADA:
# - Varios números.

# PROCESO:
# 1. Crear la clase AnalizadorNumeros.
# 2. Crear una lista para números pares.
# 3. Crear una lista para números impares.
# 4. Crear es_par(numero).
# 5. Comprobar si el número es divisible entre 2.
# 6. Crear separar(*numeros).
# 7. Reiniciar las listas de pares e impares.
# 8. Recorrer todos los números recibidos.
# 9. Utilizar es_par() para clasificar cada número.
# 10. Guardar cada número en su lista correspondiente.
# 11. Crear cantidad_pares_impares().
# 12. Obtener la cantidad de elementos de cada lista.

# SALIDA:
# - Diccionario con números pares e impares.
# - Tupla con la cantidad de pares e impares.

#BOSQUEJO:
# INICIO

#     Crear clase AnalizadorNumeros

#         Crear constructor __init__()

#             Crear lista vacía para los números pares

#             Crear lista vacía para los números impares

#         Método es_par(numero)

#             Recibir un número

#             Verificar si el número es divisible entre 2

#             Si es divisible

#                 Retornar verdadero

#             Si no

#                 Retornar falso

#         Método separar(*numeros)

#             Vaciar la lista de pares

#             Vaciar la lista de impares

#             Recibir varios números

#             Recorrer cada número

#                 Utilizar es_par()

#                 Si es par

#                     Agregar a la lista de pares

#                 Si no

#                     Agregar a la lista de impares

#             Crear diccionario con pares e impares

#             Retornar el diccionario

#         Método cantidad_pares_impares()

#             Obtener la cantidad de números pares

#             Obtener la cantidad de números impares

#             Crear una tupla con ambas cantidades

#             Retornar la tupla

#     Crear objeto AnalizadorNumeros

#     Separar varios números

#     Mostrar los números pares e impares

#     Calcular las cantidades

#     Mostrar la tupla con las cantidades

# FIN

class AnalizadorNumeros:
    
    def __init__(self):
        
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        
          if numero %2==0 :
                    return True
                
          else: 
                    return False
        
    def separar(self, *numeros):
      
        self.pares = []
        self.impares = []
        
        for num in numeros:
            
            if self.es_par(num):
                self.pares.append(num)
            else:
                self.impares.append(num)
                
        
        return {'pares': self.pares, 'impares': self.impares}
         
    def cantidad_pares_impares(self):
       
        cant_pares = len(self.pares)
        cant_impares = len(self.impares)
        return (cant_pares, cant_impares)
        

an = AnalizadorNumeros()

print(f"Separar {an.separar(1, 2, 3, 4, 5)}")
print(f"Cantidades (pares, impares): {an.cantidad_pares_impares()}")
