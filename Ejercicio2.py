# EJERCICIO 2: ANALIZADOR DE TEXTO

# ENTRADA:
# - Varias palabras.

# PROCESO:
# 1. Crear la clase Analizadortexto.
# 2. Crear una lista para almacenar las palabras.
# 3. Crear un conjunto para almacenar las palabras únicas.
# 4. Crear agregar_palabra(conjunto).
# 5. Agregar la palabra a la lista.
# 6. Agregar la palabra al conjunto.
# 7. Crear contar_pal().
# 8. Obtener la cantidad de elementos del conjunto.
# 9. Crear agregar_multiples(*args).
# 10. Recorrer todas las palabras recibidas.
# 11. Utilizar agregar_palabra() para guardar cada palabra.

# SALIDA:
# - Cantidad de palabras únicas.
# - Conjunto de palabras únicas.

#BOSQUEJO:
# INICIO

#     Crear clase Analizadortexto

#         Crear constructor __init__()

#             Crear lista vacía para almacenar las palabras

#             Crear conjunto vacío para almacenar las palabras únicas

#         Método agregar_palabra(conjunto)

#             Recibir una palabra

#             Agregar la palabra a la lista

#             Agregar la palabra al conjunto

#         Método contar_pal()

#             Obtener la cantidad de elementos del conjunto

#             Retornar la cantidad de palabras únicas

#         Método agregar_multiples(*args)

#             Recibir varias palabras

#             Recorrer cada palabra

#                 Utilizar agregar_palabra()

#     Crear objeto Analizadortexto

#     Agregar varias palabras

#     Contar las palabras únicas

#     Mostrar la cantidad de palabras únicas

#     Mostrar el conjunto de palabras únicas

# FIN

class Analizadortexto:
    
    def __init__(self):
        self.palabra= []
        self.unico= set()
    
  
       
    def agregar_palabra(self, conjunto):
        
            self.palabra.append(conjunto)
            self.unico.add(conjunto)
    
    def contar_pal(self):
       return len(self.unico)
    
    def agregar_multiples(self, *args):
       
        for pal in args:
            self.agregar_palabra(pal)

at= Analizadortexto()

at.agregar_multiples("Hola", "Estudiar", "jugar","Hola")

print(at.contar_pal())
print(f"Las palabras unicas son: {at.unico}")
  
