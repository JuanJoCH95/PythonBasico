import funciones as fun

print("Bienvenido al juego de Adivinanza")
num = fun.generar_num()
intentos = 0

while intentos != 5:
    numero = int(input("Escriba un numero del 1 al 100: "))

    if fun.validar(numero, num):
        break

    intentos += 1

    if intentos == 5:
        print("Lo sentimos, ha agotado los 5 intentos, el numero era ", num)