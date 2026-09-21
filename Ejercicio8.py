# EJERCICIO 8: EQUIPOS Y JUGADORES

# ENTRADA:
# - Nombres de equipos.
# - Nombres de jugadores.

# PROCESO:
# 1. Crear la clase Equipos.
# 2. Crear un diccionario para almacenar los equipos.
# 3. Crear crear_equipo(nombre_equipo).
# 4. Guardar cada equipo con una lista vacía.
# 5. Crear agregar_jugador(equipo, jugador).
# 6. Buscar el equipo indicado.
# 7. Agregar el jugador a la lista del equipo.
# 8. Crear equipo_mayor_integrantes().
# 9. Recorrer todos los equipos.
# 10. Obtener la cantidad de jugadores de cada equipo.
# 11. Comparar las cantidades.
# 12. Guardar el equipo con mayor cantidad de integrantes.

# SALIDA:
# - Nombre del equipo con mayor cantidad de jugadores.

#BOSQUEJO:
# INICIO

#     Crear clase Equipos

#         Crear constructor __init__()

#             Crear diccionario vacío para almacenar los equipos

#         Método crear_equipo(nombre_equipo)

#             Recibir el nombre del equipo

#             Crear una lista vacía para sus jugadores

#             Guardar el equipo en el diccionario

#         Método agregar_jugador(equipo, jugador)

#             Recibir el equipo y el nombre del jugador

#             Buscar el equipo en el diccionario

#             Agregar el jugador a su lista

#         Método equipo_mayor_integrantes()

#             Crear variable mayor = 0

#             Crear variable equipo_Mayor = ""

#             Recorrer los equipos y sus jugadores

#                 Obtener la cantidad de jugadores

#                 Comparar con la cantidad mayor

#                 Si la cantidad es mayor

#                     Actualizar mayor

#                     Guardar el nombre del equipo

#             Retornar equipo_Mayor

#     Crear objeto Equipos

#     Crear los equipos

#     Agregar jugadores a los equipos

#     Buscar el equipo con mayor cantidad de integrantes

#     Mostrar el equipo encontrado

# FIN

class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []
    
    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)
        
    def equipo_mayor_integrantes(self):
        mayor=0
        equipo_Mayor=""
        
        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > mayor:
                mayor= len(jugadores)
                equipo_Mayor= equipo
            
        return equipo_Mayor
    
Eq= Equipos()

Eq.crear_equipo("Rojo")
Eq.crear_equipo("Azul")

Eq.agregar_jugador("Rojo", "Karla")
Eq.agregar_jugador("Rojo", "Sam")
Eq.agregar_jugador("Azul", "Alex")

print(f"El equipo mayor es: {Eq.equipo_mayor_integrantes()}")


            
        
