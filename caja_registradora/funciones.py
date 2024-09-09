def login(usuario, clave):
    listUsuarios = {'admin':'admin123', 'usuariocaja1':'caja456', 'usuariocaja2':'caja789'}
    usuarioCorrecto = False

    if usuario in listUsuarios:
        psw = listUsuarios[usuario]

        if psw == clave:
            usuarioCorrecto = True
    
    return usuarioCorrecto

def compra():
    tirilla = {}
    total = 0
    compra = "S"

    while compra == "S":
        producto = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))

        tirilla[producto] = precio
        total += precio
        
        compra = input("¿Desea registrar otro producto? S/N ")
    
    tirilla['TOTAL A PAGAR'] = total
    return tirilla

def factura(tirilla):
    file = open("Factura.txt", "w")
    file.write("COLILLA DE PAGO")
    file.write('\n' + "---------------------------------")

    for clave in tirilla:
        linea = '\n' + clave + ": " + str(tirilla[clave])
        file.write(linea)

    file.close()