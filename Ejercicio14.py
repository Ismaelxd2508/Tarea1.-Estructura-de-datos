# EJERCICIO 14: REGISTRO DE NOTAS

# ENTRADA:
# - Nombre del estudiante.
# - Nota.
# - Nota mínima para aprobar.

# PROCESO:
# 1. Crear la clase RegistroNotas.
# 2. Crear un diccionario para almacenar estudiante y nota.
# 3. Crear registrar(estudiante, nota).
# 4. Guardar el estudiante y su nota.
# 5. Crear estudiantes_aprobados(nota_minima).
# 6. Recorrer los estudiantes y sus notas.
# 7. Comparar cada nota con la nota mínima.
# 8. Guardar los estudiantes que cumplen la condición.
# 9. Crear mejor_estudiante().
# 10. Recorrer los registros.
# 11. Comparar la nota actual con mejor_nota.
# 12. Actualizar los valores cuando se cumple la condición del código.

# SALIDA:
# - Lista de estudiantes aprobados.
# - Tupla con el nombre y nota obtenidos por mejor_estudiante().

#BOSQUEJO:
# INICIO

#     Crear clase RegistroNotas

#         Crear constructor __init__()

#             Crear diccionario vacío para almacenar estudiantes y notas

#         Método registrar(estudiante, nota)

#             Recibir estudiante y nota

#             Guardar el estudiante y su nota en el diccionario

#         Método estudiantes_aprobados(nota_minima)

#             Crear lista vacía

#             Recorrer estudiantes y notas

#                 Comparar la nota con la nota mínima

#                 Si la nota es mayor o igual

#                     Agregar el estudiante a la lista

#             Retornar la lista de estudiantes aprobados

#         Método mejor_estudiante()

#             Crear variable mejor_est = ""

#             Crear variable mejor_nota = 0

#             Recorrer estudiantes y notas

#                 Comparar mejor_nota con la nota actual

#                 Si se cumple la condición del código

#                     Actualizar mejor_nota

#                     Actualizar mejor_est

#             Retornar una tupla con estudiante y nota

#     Crear objeto RegistroNotas

#     Registrar varios estudiantes con sus notas

#     Buscar estudiantes aprobados

#     Mostrar los estudiantes aprobados

#     Ejecutar mejor_estudiante()

#     Mostrar la tupla obtenida

# FIN

class  RegistroNotas:
    def __init__(self):
        self.registro={}
        
    def registrar(self,estudiante, nota):
        self.registro[estudiante]=nota
        
    def  estudiantes_aprobados(self, nota_minima):
        lista=[]
        for i, c in  self.registro.items():
            
            if c >= nota_minima:
                lista.append(i)
        return lista
            
            
    def mejor_estudiante(self):
       
        mejor_est= ""
        mejor_nota=0
        
        for est, mayor in self.registro.items():
            
            if mejor_nota > mayor:
                mejor_nota= mayor
                mejor_est= est
        
        return (mejor_est,mejor_nota)
    

rn = RegistroNotas()

rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
rn.registrar("Carlos", 85)

print(f"los estudiantes aprobados son: {rn.estudiantes_aprobados(70)}")
print(f"El mejor estudiantes es: {rn.mejor_estudiante()}")


    
