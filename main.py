import json #llamar al json
from os import system #Limpiar pantalla
from datetime import datetime


#Guardar los datos del json en una variable
with open("venta.json", "r") as openfile:
    ventajson= json.load(openfile)
with open("compras.json", "r") as openfile:
    compraJson= json.load(openfile)

variable={}

print("------------------------------------------------")# MENU
print("                 PanCamp :)                    ")
print("------------------------------------------------\n")

print("1. Registrar venta")
print("2. Registrar compra")
print("3. Informe de Ventas")
print("4. Informe de Stock")
print("")
opcion=int(input("Ingrese el número de la opción que deseas ver: "))

if opcion==1:

    print("|Registrar venta|")

    fechaventa=str(input("Ingrese la fecha"))
    print("")
    print("|Por favor ingresar los datos del cliente|")
    print("")
    nombreCliente=str(input("Nombre:\n"))
    direccionCliente= str(input("Dirección:\n"))
    print("")
    print("|Ingrese los datos del Empleado|\n")
    nombreEmpleado=str(input("Nombre\n"))
    empleado=str(input("Cargo:\n"))
    print("")
    producto=str(input("Ingrese el nombre del producto vendido"))


    variable={
        "fecha": fechaventa,
        "nombre": nombreCliente,
        "empleado": nombreEmpleado,
        "productoVendido": producto
    }

    ventajson +=[variable]
    with open("venta.json", "w") as outfile:
        json.dump(ventajson, outfile, indent=4)

    print("venta realizada")
    # Imprimir los datos de la variable
    print("Datos de la última compra:")
    print(f"Fecha: {variable['fecha']}")
    print(f"Cliente: {variable['nombre']}")
    print(f"Empleado: {variable['empleado']}")
    print(f"Producto vendido: {variable['productoVendido']}")

if opcion==2:

    print("|Registrar Compras|")
    print("")

    fechaCompra= str(input("Fecha de Compra: \n"))
    print("")
    print("Ingrese los datos del provedor")
    print("")
    nombreprovedor= str(input("Nombre: \n"))
    print("")
    contacto= int(input("Contacto: \n"))
    print("")
    print("Ingrese los datos del producto")
    print("")
    prodname= str(input("Nombre: \n"))
    cantidad= str(input("Cantidad: \n"))
    precioCompra= int(input("precio de compra: \n"))

    #Añadir datos al json
    compras={
        "fechaCompra": fechaCompra,
        "nombreProvedor": nombreprovedor,
        "contacto": contacto,
        "nombreProducto": prodname,
        "cantidad": cantidad,
        "precioCompra": precioCompra
    }
    compraJson +=[compras]
    with open("compras.json", "w") as outfile:
        json.dump(compraJson, outfile, indent=4)
    print("")
    print("|Compra Realizada|")
    print("")
    # Imprimir los datos de la variable
    print("Datos de la última compra:")
    print(f"Fecha: {compras['fechaCompra']}")
    print(f"Nombre del provedor: {compras['nombreProvedor']}")
    print(f"contacto: {compras['contacto']}")
    print(f"Nombre del producto: {compras['nombreProducto']}")
    print(f"Cantidad: {compras['cantidad']}")
    print(f"Precio de la compra: {compras['precioCompra']}")

if opcion==3:

    system("cls")
    print("|Registro de Ventas|")
    cell=0
    print("Ingrese la fecha de las ventas que busca")
    fordate=input()
    print("")
    for i in ventajson:
        if i["fecha"]==fordate:
            print("Datos de la última compra:")
            print(f"Fecha: {i['fecha']}")
            print(f"Cliente: {i['nombre']}")
            print(f"Empleado: {i['empleado']}")
            print(f"Producto vendido: {i['productoVendido']}")
        else:
            print("No hay ventas con esa fecha")

if opcion==4:
    system("cls")
    print("")
    print("|Registro de Compras|")
    print("")

    contador=1
    for i in compraJson:
        print("|Compra", contador,"|")
        print(f"Fecha: {i['fechaCompra']}")
        print(f"Provedor: {i['nombreProvedor']}")
        print(f"Producto: {i['nombreProducto']}")
        print(f"Cantidad: {i['cantidad']}")
        print(f"Precio de compra: ${i['precioCompra']}")
        print("")
        contador=contador+1