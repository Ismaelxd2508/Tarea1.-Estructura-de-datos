# EJERCICIO 10: GESTOR DE TAREAS

# ENTRADA:
# - Descripción de una tarea.
# - Prioridad de la tarea.

# PROCESO:
# 1. Crear la clase Tareas.
# 2. Crear una lista para almacenar las tareas.
# 3. Guardar cada tarea como una tupla de descripción y prioridad.
# 4. Crear agregar_tarea(descripcion, prioridad).
# 5. Agregar la tupla a la lista.
# 6. Crear tareas_prioritarias().
# 7. Recorrer las tareas almacenadas.
# 8. Buscar las tareas cuya prioridad sea "Alta".
# 9. Crear eliminar_completada(descripcion).
# 10. Recorrer las tareas.
# 11. Buscar la tarea por su descripción.
# 12. Eliminar la tarea encontrada.

# SALIDA:
# - Lista de tareas con prioridad alta.
# - Lista de tareas actualizada después de eliminar.

#BOSQUEJO:
# INICIO

#     Crear clase Tareas

#         Crear constructor __init__()

#             Crear lista vacía para almacenar las tareas

#         Método agregar_tarea(descripcion, prioridad)

#             Recibir descripción y prioridad

#             Crear una tupla con descripción y prioridad

#             Agregar la tupla a la lista

#         Método tareas_prioritarias()

#             Crear lista vacía llamada resultado

#             Recorrer las tareas almacenadas

#                 Obtener la prioridad de cada tarea

#                 Si la prioridad es "Alta"

#                     Agregar la tarea a resultado

#             Retornar las tareas prioritarias

#         Método eliminar_completada(descripcion)

#             Recorrer las tareas almacenadas

#                 Comparar la descripción de la tarea

#                 Si coincide con la descripción recibida

#                     Eliminar la tarea

#                     Detener el recorrido

#     Crear objeto Tareas

#     Agregar varias tareas

#     Buscar las tareas prioritarias

#     Mostrar las tareas prioritarias

#     Eliminar una tarea mediante su descripción

#     Mostrar las tareas actualizadas

# FIN

class Tareas:
    def __init__(self):
        self.prioridades=[]
    
    def  agregar_tarea(self, descripcion, prioridad):
        
        tarea=(descripcion, prioridad)
        self.prioridades.append(tarea)
    
    def  tareas_prioritarias(self):
        resultado=[]
        
        for i in self.prioridades:
            if i[1]== "Alta":
                resultado.append(i)
        return resultado
    
    def  eliminar_completada(self,descripcion):
        
        for c in self.prioridades:
            if c[0] == descripcion:
                self.prioridades.remove(c)
                break

tr= Tareas()

tr.agregar_tarea("Estudiar", "Alta")
tr.agregar_tarea("Practicar", "Alta")
tr.agregar_tarea("Repasar", "Baja")

print(f"las tareas prioritarias son: {tr.tareas_prioritarias()}")

tr.eliminar_completada("Estudiar")

print(f"Tareas actualizadas: {tr.prioridades}")
