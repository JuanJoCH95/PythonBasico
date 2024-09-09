contador = 0
nota_final = 0
total_creditos = 0
prom_semestre = 0
max_promedio = 0
min_promedio = 0

print("Bienvenido, seleccione una de las siguientes opciones:")
opcion = int(input("1 - Calcular nota final de una materia \n2 - Calcular el promedio del semestre \n3 - Calcular mejor y peor promedio historico \n"))

if opcion == 1:
    while(contador < 100):
        nota = float(input("Ingrese la nota de evaluación: "))
        porcentaje = int(input("Ingrese el porcentaje de la nota: "))
        nota_final = nota_final + (nota * (porcentaje / 100))
        contador = contador + porcentaje
    print("Nota final del 100%:", nota_final)
elif opcion == 2:
    n_cursos = int(input("Ingrese el numero de cursos finalizados en el semestre: "))

    while(contador < n_cursos):
        nota = float(input("Ingrese la nota final obtenida en el curso: "))
        n_creditos = int(input("Ingrese el numero de creditos correspondientes a dicho curso: "))
        nota_final = nota_final + (nota * n_creditos)
        total_creditos = total_creditos + n_creditos
        contador += 1
    prom_semestre = nota_final / total_creditos
    print("El promedio ponderado de su semetre fue:", prom_semestre)
elif opcion == 3:
    n_semestres = int(input("Ingrese el numero de semestres cursados: "))
    contador += 1
    prom_semestre = float(input("Ingrese el promedio del semestre: "))
    max_promedio = prom_semestre
    min_promedio = prom_semestre

    while(contador < n_semestres):
        contador += 1
        prom_semestre = float(input("Ingrese el promedio del semestre: "))

        if(prom_semestre > max_promedio):
            max_promedio = prom_semestre
        if(prom_semestre < min_promedio):
            min_promedio = prom_semestre
    print("El mejor promedio de su carrera fue:", max_promedio)
    print("El peor promedio de su carrera fue:", min_promedio)
else:
    print("Opción no valida")