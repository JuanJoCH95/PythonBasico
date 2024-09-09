#Ordenamiento por selección
def seleccion(lista):
    for i in range(0, len(lista)):
        min = i

        for j in range(i + 1, len(lista)):
            if lista[min] > lista[j]:
                min = j
        
        temp = lista[i]
        lista[i] = lista[min]
        lista[min] = temp
    
    print(lista)

#Ordenamiento por burbuja
def burbuja(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
    
    print(lista)

def loadFromFile():
    archivo = open("data.txt", 'r')
    lista = []

    for linea in archivo:
        elemento = linea.split()
        elemento = float(elemento[0])
        lista.append(elemento)
    
    return lista

def listAleatoria(min, max, cant):
    lista = []

    for i in range(int(cant)):
        num = random.randint(int(min), int(max))
        lista.append(num)

    return lista

#Main
import random
'''lista = [8, 5, 2, 10, 1, 9, 12, 3]
print("¿Desea ordenar la lista por burbuja o por selección?")
opcion = int(input("1 - Burbuja \n2 - Selección \n"))

if opcion == 1:
    burbuja(lista)
else:
    seleccion(lista)'''

min = input("Digite el numero minimo: ")
max = input("Digite el numero maximo: ")
cant = input("Digite la cantidad de numeros: ")

lista = listAleatoria(min, max, cant)
print(lista)