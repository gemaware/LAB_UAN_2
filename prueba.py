import numpy as np


matriz_productos = np.empty((0,2), int)
def main():
    opcion = 0
    while (opcion != 3):
        print("<<< Bienvenido/a Gestion System >>>")
        print("¡¿Qué desea hacer?!")
        print("(1) - Registrar Producto Nuevo")
        print("(2) - Ordenar Productos")
        print("(3) - Clasificar Productos")
        print("(4) - Salir")
        opcion = int(input())

        if opcion == 1:
            registrar()
        if opcion == 2:
            ordenar()
        if opcion == 3:
            print("<<< Ha salido del sistema exitosamente, gracias por usar Gestion System >>>")

    ############################################
    # # # Funcion de Registro de Productos # # #
    ############################################

def registrar():
    global matriz_productos
    try:
        print("<<< Registro de Producto Nuevo >>>")
        print("- Ingrese nombre del producto")
        nombre_producto = input()
        print("- Ingrese precio del producto")
        precio_producto = int(input())
        matriz_productos = np.append(matriz_productos, [[nombre_producto,precio_producto]], axis=0)
        print("<<< Producto registrado correctamente >>>")
        for arr_productos in matriz_productos:
            print("*****************************")
            print("Nombre:", arr_productos[0])
            print("Precio:","$", arr_productos[1],"\n")
            print("*****************************")
    except:
        print("!!! ERROR: Por favor Ingrese un formato de precio sin puntos !!!")

    ############################################
    # # # Funcion de Ordenado de Productos # # #  ######## AQUI ESTA LO DE ORDENAR.
    ############################################
def ordenar():
        print("Seleccione en que orden quiere ordenar:")
        print("(1) - Ordenar de forma descendente")   
        op_ordenar = int(input())
        
        global matriz_productos
        if(op_ordenar == 1):
            ordenado = np.argsort(matriz_productos[::,1])
            desc = ordenado[::-1]
            matriz_ordenada = matriz_productos[desc]
            for arr_productos in matriz_ordenada:
                print("*****************************")
                print("Nombre:", arr_productos[0])
                print("Precio:","$", arr_productos[1],"\n")
                print("*****************************")
main()    