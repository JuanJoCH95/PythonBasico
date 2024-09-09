
def loadFromFile(name):
    archivo = open(name, 'r')
    lista = []

    for linea in archivo:
        elemento = linea.split()
        elemento = float(elemento[0])
        lista.append(elemento)
    
    return lista

def sortBurbuja(L):
    cantidad = 0

    for i in range(len(L)):
        for j in range(len(L) - i - 1):
            if L[j] > L[j + 1]:
                temp = L[j]
                L[j] = L[j + 1]
                L[j + 1] = temp
            cantidad += 1
    
    return cantidad

def sortSeleccion(L):
    cantidad = 0

    for i in range(0, len(L)):
        min = i

        for j in range(i + 1, len(L)):
            if L[min] > L[j]:
                min = j
            cantidad += 1
        temp = L[i]
        L[i] = L[min]
        L[min] = temp
    
    return cantidad