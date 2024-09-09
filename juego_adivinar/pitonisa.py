import funciones as fun

print("Bienvenido al juego de Pitonisa")
print("Piensa en un numero entre 1 y 100")

num = fun.generar_num()

for i in range(5):
    print("Creo que tu numero es:", num)
    respuesta = input("¿Es mayor, menor o igual? ")

    if respuesta == "igual":
        print("¡Genial he ganado! :D")
        break
    elif respuesta == "menor":
        num = fun.generar_num_menor(num)
    elif respuesta == "mayor":
        num = fun.generar_num_mayor(num)
    
    if i == 4:
        print("Creo que he agotado mis 5 intentos. Perdí :(")