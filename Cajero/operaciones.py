import datetime

saldo = 0.0

def consultar():
    print("Su saldo actual es: ", saldo)

    accion = input("¿Desea imprimir factura? S/N: ")

    if accion == "S":
        factura(1)

def retirar():
    global saldo
    cantidad = float(input("¿Cuanto dinero desea retirar? "))

    if cantidad < saldo:
        print("Retiro exitoso")
        saldo = saldo - cantidad
        print("Su nuevo saldo es: ", saldo)
    else:
        print("No cuenta con fondos suficientes para realizar el retiro por la cantidad solicitada.")
    
    accion = input("¿Desea imprimir factura? S/N: ")

    if accion == "S":
        factura(2)

def depositar():
    global saldo
    cantidad = float(input("¿Cuanto dinero desea depositar? "))
    print("Deposito realizado con exito")
    saldo = saldo + cantidad
    print("Su nuevo saldo es: ", saldo)

    accion = input("¿Desea imprimir factura? S/N: ")

    if accion == "S":
        factura(3)

def factura(accion):
    file = open("Factura.txt", "w")
    fecha = obtenerFecha()

    if accion == 1:
        file.write("----------------------------------------")
        file.write('\n' + "COMPROBANTE - CONSULTA SALDO")
        file.write('\n' + "----------------------------------------")
        file.write('\n' + "Su saldo actual es: " + str(saldo))
        file.write('\n' + "Fecha y hora de consulta: " + fecha)
    elif accion == 2:
        file.write("----------------------------------------")
        file.write('\n' + "COMPROBANTE - RETIRO CUENTA DE AHORROS")
        file.write('\n' + "----------------------------------------")
        file.write('\n' + "Su saldo actual es: " + str(saldo))
        file.write('\n' + "Fecha y hora de retiro: " + fecha)
    elif accion == 3:
        file.write("----------------------------------------")
        file.write('\n' + "COMPROBANTE - DEPOSITO CUENTA DE AHORROS")
        file.write('\n' + "----------------------------------------")
        file.write('\n' + "Su saldo actual es: " + str(saldo))
        file.write('\n' + "Fecha y hora del deposito: " + fecha)

    file.close()

def obtenerFecha():
    fechaActual = datetime.datetime.now()

    dia = str(fechaActual.day)
    mes = str(fechaActual.month)
    year = str(fechaActual.year)
    hora = str(fechaActual.hour)
    minuto = str(fechaActual.minute)
    segundo = str(fechaActual.second)

    if fechaActual.hour >= 13:
        abrebiatura = "P.M."
    else:
        abrebiatura = "A.M."

    fecha = dia + "-" + mes + "-" + year + " " + hora + ":" + minuto + ":" + segundo + " " + abrebiatura

    return fecha