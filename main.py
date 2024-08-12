import json #llamar al json
from os import system #Limpiar pantalla
from datetime import datetime


#Guardar los datos del json en una variable
with open("venta.json", "r") as openfile:
    ventajson= json.load(openfile)
with open("compras.json", "r") as openfile:
    compraJson= json.load(openfile)

variable={}

print("────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────")# MENU
print("                 PanCamp                    ")
print("────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────\n")

print("1. Registrar venta")
print("2. Registrar compra")
print("3. Informe de Ventas")
print("4. Informe de Stock")
print("")
opcion=int(input("Ingrese el número de la opción que deseas ver: "))

if opcion==1:
    
    system("cls")
    print("────୨ৎ────────୨ৎ──── Registrar venta ────୨ৎ────────୨ৎ────")
    print("")
    fechaventa=str(input("Ingrese la fecha"))
    print("")
    print("|Por favor ingresar los datos del cliente|")
    print("")
    nombreCliente=str(input("Nombre: "))
    direccionCliente= str(input("Dirección: "))
    print("")
    print("|Ingrese los datos del Empleado|\n")
    nombreEmpleado=str(input("Nombre "))
    empleado=str(input("Cargo: "))
    print("")
    producto=str(input("Ingrese el nombre del producto vendido: "))
    cantidadvendido=str(input("Ingrese la cantidad del producto vendido: "))
    preciovendido=str(input("Ingrese el precio total del producto: "))


    variable={
        "fecha": fechaventa,
        "nombre": nombreCliente,
        "empleado": nombreEmpleado,
        "productoVendido": producto,
        "cantidad": cantidadvendido,
        "total": preciovendido
    }

    ventajson +=[variable]
    with open("venta.json", "w") as outfile:
        json.dump(ventajson, outfile, indent=4)

    print("Registro de venta exitosa ")
    system("cls")


    # Imprimir los datos de la variable
    print("────୨ৎ────────୨ৎ────Datos de la última compra────୨ৎ────────୨ৎ────")
    print("")
    print(f"Fecha: {variable['fecha']}")
    print(f"Cliente: {variable['nombre']}")
    print(f"Empleado: {variable['empleado']}")
    print(f"Producto vendido: {variable['productoVendido']}")
    print(f"Cantidad vendida: {variable["cantidad"]}")
    print(f"Precio del producto: {variable["total"]}")

if opcion==2:

    system("cls")
    print("────୨ৎ────────୨ৎ────Registrar Compras────୨ৎ────────୨ৎ────")
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
    print("────୨ৎ────────୨ৎ────Compra Realizada────୨ৎ────────୨ৎ────")
    print("")
    # Imprimir los datos de la variable
    print("────୨ৎ────────୨ৎ────Datos de la última compra────୨ৎ────────୨ৎ────")
    print(f"Fecha: {compras['fechaCompra']}")
    print(f"Nombre del provedor: {compras['nombreProvedor']}")
    print(f"contacto: {compras['contacto']}")
    print(f"Nombre del producto: {compras['nombreProducto']}")
    print(f"Cantidad: {compras['cantidad']}")
    print(f"Precio de la compra: {compras['precioCompra']}")

if opcion==3:

    system("cls")
    print("────୨ৎ────────୨ৎ────Registro de Ventas────୨ৎ────────୨ৎ────")
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
            print("✗")
            print("No hay ventas con esa fecha ")

if opcion==4:
    system("cls")
    print("")
    print("────୨ৎ────────୨ৎ────Registro de Compras────୨ৎ────────୨ৎ────")
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