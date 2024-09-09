nombre = input("Ingrese su nombre: ")
documento = input("Ingrese su numero de documento: ")

print("* Sistema de Estímulos Académicos (SEA) *")
print("Bienvenido", nombre)
print("Ingrese la categoría del estímulo al cual desea aplicar:")

categoria = input("A - Auxiliar administrativo \nM - Monitor de curos \nP - Auxiliar de programación \nD - Docente cátedra semillero \n")
creditos = int(input("Ingrese el total de creditos del programa: "))
creditos_aprobados = int(input("Ingrese el numero de creditos aprobados: "))
creditos_requeridos = 0
elegible = "Usted es elegible para el estímulo seleccionado"
no_elegible = "Lo sentimos, usted no es elegible para el estimulo"

if categoria == "A":
    if creditos_aprobados >= 20:
        print(elegible)
    else:
        print(no_elegible)
elif categoria == "M" or categoria == "P":
    creditos_requeridos = creditos * 0.40
    if creditos_aprobados >= creditos_requeridos:
        print(elegible)
    else:
        print(no_elegible)
elif categoria == "D":
    creditos_requeridos = creditos * 0.50
    if creditos_aprobados >= creditos_requeridos:
        print(elegible)
    else:
        print(no_elegible)
else:
    print("Categoría no valida")