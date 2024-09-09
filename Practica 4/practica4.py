#Funcion 1
def generar():
    import random

    while True:
        repetidos = 0
        num = random.randint(1000, 9999)
        num = str(num)

        for i in range(len(num)):
            if num[i] in num[i+1:]:
                repetidos += 1
        
        if repetidos == 0:
            break
    
    return num

#Funcion 2
def leer_num():
    num = int(input("Ingrese un número de 4 digitos no repetidos: "))
    num = str(num)

    if len(num) != 4:
        respuesta = 0
    else:
        for i in range(len(num)):
            if num[i] in num[i+1:]:
                respuesta = 0
                break
            else:
                respuesta = num
    
    return respuesta

#Funcion 3
def verificar(num_u, num_m):
    picas = 0
    fijas = 0

    for i in range(len(num_m)):
        if num_u[i] in num_m:
            picas += 1
    
    for i in range(len(num_m)):
        if num_u[i] == num_m[i]:
            fijas += 1
    
    return (picas, fijas)

#Funcion 4
def bienvenida(nombre_archivo):
    file = open(nombre_archivo)
    print(file.read())
    file.close()

#Main
bienvenida("bienvenida.txt")
intentos = int(input("Ingrese el número de intentos que desea realizar: "))
numMaquina = generar()
i = 0

while i < intentos:
    numUsuario = leer_num()

    if numUsuario == 0:
        print("El número no es válido")
    else:
        (picas, fijas) = verificar(numUsuario, numMaquina)
        print("Picas: ", picas)
        print("Fijas: ", fijas)

        if fijas == 4:
            print("¡Felicidades! ha adivinado el numero")
            break
    
    i += 1

    if i == intentos:
        print("Se acabaron sus intentos. El número era: ", numMaquina)