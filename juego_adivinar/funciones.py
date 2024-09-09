import random

#Funcion que genera un numero aleatorio entre 1 y 100
def generar_num():
    num = random.randint(1, 100)
    return num

#Funcion que genera un numero aleatorio entre 1 y 100
def generar_num_menor(valor):
    num = random.randint(1, valor)
    return num

#Funcion que genera un numero aleatorio entre 1 y 100
def generar_num_mayor(valor):
    num = random.randint(valor, 100)
    return num

#Funcion que valida si el numero es mayor, menor o igual
def validar(num_usuario, num_maquina):
    if num_usuario == num_maquina:
        print("Felicidades, adivinaste el numero secreto, era ", num_maquina)
        return True
    elif num_usuario < num_maquina:
        print("El numero secreto es mayor a ", num_usuario)
        return False
    elif num_usuario > num_maquina:
        print("El numero secreto es menor a ", num_usuario)
        return False