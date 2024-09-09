#Función para leer el archivo con los datos
def leer_datos(nombre_a):
    archivo = open(nombre_a, 'r')
    diccionario = {}
    encabezado = archivo.readline()
    claves = [etiqueta.strip(" \n") for etiqueta in encabezado.split(";")]

    for linea in archivo:
        lista = linea.split(';')
        elemento = {claves[i].strip(" \n"):float(lista[i].strip(" \n")) for i in range(1,len(lista))}
        diccionario[int(lista[0])] = elemento
    archivo.close()

    return diccionario

#Función que entrega el promedio de precipitaciones para un año especifico
def promedio(base_datos, year):
    diccionario = base_datos[year]
    promedio = 0.0
    suma = 0.0

    for clave in diccionario:
        suma += diccionario[clave]
        
    promedio = suma / 12
    promedio = round(promedio, 2)
    return promedio

#Función que entrga el mes donde se presentó el valor minimo de precipitaciones en un año especifico
def valor_minimo(base_datos, year):
    diccionario = base_datos[year]
    d_minimo = {}
    v_minimo = min(diccionario, key=diccionario.get)
    d_minimo = {v_minimo:diccionario[v_minimo]}

    return d_minimo

#Función que entrga el mes donde se presentó el valor maximo de precipitaciones en un año especifico
def valor_maximo(base_datos, year):
    diccionario = base_datos[year]
    d_maximo = {}
    v_maximo = max(diccionario, key=diccionario.get)
    d_maximo = {v_maximo:diccionario[v_maximo]}

    return d_maximo