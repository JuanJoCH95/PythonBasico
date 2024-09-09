def login():
    listUsuarios = {'admin':'admin123', 'admin2':'admin01+', 'juanjo':'juanjo02'}
    usuarioCorrecto = False
    intentos = 0

    while intentos != 3:
        usuario = input("Usuario: ")
        clave = input("Contraseña: ")

        if usuario in listUsuarios:
            psw = listUsuarios[usuario]

            if psw == clave:
                usuarioCorrecto = True
                break
            else:
                intentos += 1
        else:
            intentos += 1
        
        if intentos == 3:
            print("Ha agotado el limite de intentos. Por favor intentelo mas tarde.")
        else:
            print("Usuario y/o contraseña incorrectos. Por favor intente nuevamente.")
    
    return usuarioCorrecto