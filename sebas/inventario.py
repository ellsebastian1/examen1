from funcion import *
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():

   while True:
        clear()
        print("INVENTARIO")
        print("")
        print("1-Ingrese el producto: ")
        print("2-Buscar producto: ")
        print("3-Mostrar producto: ")
        print("4-Cambiar cantidad: ")
        print("5-salir")

        opc=input("ingrese una opcion: ")

        if not opc.isdigit:
            print('')
            print("intraduzca un valor valido")
            input("presione enter para continuar")
            continue
        opc=int(opc)
        if opc > 5:
            print('')
            print("intraduzca un valor valido")
            input("presione enter para continuar")
            continue

        if opc==1:
            clear()
            print("**INGRESAR PRODUCTO**")
            agregar()
            input("ingrese enter para continuar")
            continue
        elif opc==3:
            clear()
            print("**Mostrar**")
            mostrar()
            input("ingrese enter para continuar")
            continue
        elif opc==2:
            clear()
            print("**Buscar*")
            buscar_producto(input("ingrese nombre: "))
            input("enter para continuar")
            continue
        elif opc==4:
            clear()
            print("**Actualizar**")
            actualizar_cantidad()
            input("enter para continuar")
            continue
        else:
            print("Velva pronto")
            break
        
            
            
            
main()

