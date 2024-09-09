import funciones as fun

print("Bienvenido")

while True:
    try:
        year = int(input("Escriba el año del cual desea conocer el reporte de precipitaciones: "))
        break
    except ValueError:
        print("El dato ingresado no es valido")

base_d = fun.leer_datos("precipitaciones.csv")

if year in base_d:
    promedio = fun.promedio(base_d, year)
    maximo = fun.valor_maximo(base_d, year)
    minimo = fun.valor_minimo(base_d, year)

    print("El promedio de precipitaciones para el año", year, "fue de:", promedio)
    print("El mes con el valor de precipitaciones mas alto en el año", year, "fue:", maximo)
    print("El mes con el valor de precipitaciones mas bajo en el año", year, "fue:", minimo)
else:
    print("El año seleccionado no se encuntra en el reporte de precipitaciones")