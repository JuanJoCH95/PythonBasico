import funciones as fun

usuario = input("Usuario: ")
clave = input("Contraseña: ")

if fun.login(usuario, clave) == True:
    print("¡Bienvenido!")
    factura = fun.compra()
    print(factura)
    fun.factura(factura)
    print("Factura imprimida con exito")
else:
    print("Usuario y/o contraseña incorrectos")