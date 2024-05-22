lista_inventario=[]


def agregar():

    producto=input("ingrese el producto: ")
    cantidad=input("ingrese la cantidad: ")
    precio=input("ingrese el precio: ")
    codigo=input("ingrese el codigo: ")


    inventariolist={
        1:{
            'producto':producto,
            'cantidad':cantidad,
            'precio':precio,
            'codigo':codigo
            
        }
    }
    lista_inventario.append(inventariolist)

def mostrar():
    for inventariolist in lista_inventario:
        print(f'CODIGO: {inventariolist[1]["codigo"]}-Producto: {inventariolist[1]["producto"]} - Cantidad: {inventariolist[1]["cantidad"]} -Precio: {inventariolist[1]["precio"]}$')

def buscar_producto(nombre_producto):
    for inventariolist in lista_inventario:
        if inventariolist[1]['producto'] == nombre_producto:
            print(f'Producto: {inventariolist[1]["producto"]}')
            print(f'Cantidad: {inventariolist[1]["cantidad"]}')
            print(f'Precio: {inventariolist[1]["precio"]}$')
            return
    print(f'El producto "{nombre_producto}" no está registrado en el inventario.')

def actualizar_cantidad():
    nombre_producto=input("ingrese el producto: ")  
    nueva_cantidad=input("ingrese la nueva cantidad: ")
    for inventariolist in lista_inventario: 
        if inventariolist[1]['producto'] == nombre_producto:
            inventariolist[1]['cantidad'] = nueva_cantidad
            print(f'Se ha actualizado la cantidad del producto "{nombre_producto}" a {nueva_cantidad}.')
            return
    print(f'El producto "{nombre_producto}" no está registrado en el inventario.')