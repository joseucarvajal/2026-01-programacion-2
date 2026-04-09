from typing import List
from producto import Producto

# lista = arreglo = colección
lista_productos: list[Producto] = [ ]

def agregar_producto():
    nombre_producto = input("Ingrese el nombre del producto: ")
    if(nombre_producto == ""):
        print("ERROR: El nombre del producto no puede ser vacio")
    else:
        precio_producto = float(input("Ingrese el precio del producto: "))
        descuento_producto = float(input("Ingrese el descuento del producto: "))
        producto = Producto() #Creo el objeto producto a partir de la clase Producto
        producto.nombre = nombre_producto
        producto.precio = precio_producto
        producto.descuento = descuento_producto
        lista_productos.append(producto)

def mostrar_total_venta():
    total_venta = 0
    for producto in lista_productos:
        total_producto = producto.precio - producto.descuento 
        total_venta = total_venta + total_producto
    print(f"El total de la venta es: {total_venta}")

def mostrar_productos():
    lista_productos.sort(key=lambda producto: producto.precio, reverse=True)
    for producto in lista_productos:
        print(f"{producto.nombre}: $ {producto.precio}")

def consultar_producto_mas_costoso():
    producto_mas_costoso = max(lista_productos, key=lambda producto: producto.precio)
    print(f"El producto más costos es: {producto_mas_costoso.nombre} con un precio de $ {producto_mas_costoso.precio}")


def buscar_producto():
    producto_a_buscar = input("Ingrese el nombre del producto a buscar: ")
    producto_encontrado = None
    for producto in lista_productos:
        if(producto.nombre == producto_a_buscar):
            producto_encontrado = producto
            
    if producto_encontrado == None:
        print("Producto no encontrado")
    else:
        print(f"Producto: {producto_encontrado.nombre}: ${producto_encontrado.precio}")

def main():
    continuar = True
    while continuar == True:
        print("...... Menú de opciones ......")
        print("1. Agregar producto")
        print("2. Mostrar el total de la venta")
        print("3. Mostrar todos los productos ordenados por precio")
        print("4. Consultar el producto más costoso")
        print("5. Buscar producto")
        print("6. Salir")
        opcion = input("Ingrese la opción: ")
        if opcion == "1":
            agregar_producto()
        if opcion == "2":
            mostrar_total_venta()
        if opcion == "3":
            mostrar_productos()
        if opcion == "4":
            consultar_producto_mas_costoso()
        if opcion == "5":
            buscar_producto()
        if opcion == "6":
            continuar = False


if __name__ == "__main__":
    main()