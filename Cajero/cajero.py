import autenticacion as autn
import operaciones as op

if autn.login():
    print("¡Bienvenido!")
    opcion = 0

    while opcion != 4:
        print("Seleccione una de las siguientes opciones:")
        opcion = int(input("1 - Consultar saldo \n2 - Retirar dinero \n3 - Depositar dinero \n4 - Salir \n"))

        if opcion == 1:
            op.consultar()
        elif opcion == 2:
            op.retirar()
        elif opcion == 3:
            op.depositar()
        elif opcion == 4:
            print("Gracias, vuelva pronto.")
            break
        else:
            print("Opción no valida. Por favor intente nuevamente")