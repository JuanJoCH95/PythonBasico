#Ejercicio para crear correo y contraseña
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
fechaNacimiento = input("Ingrese su año de nacimiento: ")

correo = nombre.lower() + apellido.lower() + "@udea.edu.co"
clave = nombre.lower()[0:3] + fechaNacimiento[2:4]

print("Bienvenido", nombre, apellido)
print("Su correo electronico institucional es:", correo)
print("Su contraseña es:", clave)


#Ejemplo de funciones en Python
def batidos(banana, manzana):
    if manzana > banana and banana != 0:
        orden = "Batido de manzana con banana"
    elif banana > manzana and manzana != 0:
        orden = "Batido de banana con manzana"
    else:
        orden = "Batido de frutas"
    
    return orden

bananas = int(input("Ingrese la cantidad de bananas que desea incluir: "))
manzanas = int(input("Ingrese la cantidad de manzanas que desea incluir: "))

resultado = batidos(bananas, manzanas)

print(resultado)