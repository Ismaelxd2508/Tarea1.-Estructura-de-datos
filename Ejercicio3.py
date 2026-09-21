# EJERCICIO 3: CARRO DE COMPRAS

# ENTRADA:
# - Nombre del artículo.
# - Precio del artículo.
# - Precio mínimo y máximo para realizar una búsqueda.

# PROCESO:
# 1. Crear la clase CarroCompras.
# 2. Crear un diccionario para almacenar los artículos y sus precios.
# 3. Crear agregar_articulo(nombre, precio).
# 4. Guardar el nombre y precio del artículo.
# 5. Crear total_carrito().
# 6. Recorrer los precios almacenados.
# 7. Sumar todos los precios.
# 8. Crear articulos_por_rango(minimo, maximo).
# 9. Recorrer los artículos y sus precios.
# 10. Comprobar si cada precio está dentro del rango.
# 11. Guardar los artículos que cumplen el rango.

# SALIDA:
# - Total del carrito.
# - Artículos que se encuentran dentro del rango indicado.

#BOSQUEJO:
# INICIO

#     Crear clase CarroCompras

#         Crear constructor __init__()

#             Crear diccionario vacío para almacenar los artículos

#         Método agregar_articulo(nombre, precio)

#             Recibir nombre y precio

#             Guardar el artículo y su precio en el diccionario

#         Método total_carrito()

#             Crear variable total = 0

#             Recorrer los precios de los artículos

#                 Sumar cada precio a total

#             Retornar el total

#         Método articulos_por_rango(minimo, maximo)

#             Crear diccionario vacío para guardar los resultados

#             Recorrer los nombres y precios

#                 Verificar si el precio es mayor o igual al mínimo
#                 y menor o igual al máximo

#                 Si cumple el rango

#                     Guardar el artículo y su precio en el resultado

#             Retornar el resultado

#     Crear objeto CarroCompras

#     Agregar varios artículos

#     Calcular y mostrar el total del carrito

#     Buscar artículos entre un precio mínimo y máximo

#     Mostrar los artículos encontrados

# FIN

class CarroCompras:
    def __init__(self):
        self.articulos = {}
     
    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio
    
    def total_carrito(self):
        total = 0
        for precio in self.articulos.values():
            total += precio
        return total

    def articulos_por_rango(self, minimo, maximo):
        resultado = {}
        
       
        for nombre, precio in self.articulos.items(): 
            
           
            if minimo <= precio <= maximo:
                resultado[nombre] = precio   
        
        return resultado
        

carrito = CarroCompras()

carrito.agregar_articulo("Mouse", 15)
carrito.agregar_articulo("Teclado", 30) 
carrito.agregar_articulo("Monitor", 200)
carrito.agregar_articulo("Audífonos", 25)

print("Total del carrito:", carrito.total_carrito()) 
print("Artículos entre $20 y $50:") 
print(carrito.articulos_por_rango(20, 50))

    
    
    
    
