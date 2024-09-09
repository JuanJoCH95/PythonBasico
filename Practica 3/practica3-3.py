#Practica 3 punto 1
print("PUNTO #1")
vocales = ['a', 'e', 'i', 'o', 'u']
consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
caracter = input("Ingrese un caracter: ")

if caracter.lower() in vocales:
    print("Es una vocal")
elif caracter.lower() in consonantes:
    print("Es una consonante")

#Practica 3 punto 2
print("PUNTO #2")
frase = input("Escriba una palabra o frase: ")
letra = input("Ingrese una letra: ")
frase_final = ""

for i in range(len(frase)):
    if(frase[i] == letra):
        frase_final = frase_final + "*"
    else:
        frase_final = frase_final + frase[i]

print(frase_final)

#Practica 3 punto 3
print("PUNTO #3")
palabra = input("Ingrese una palabra: ")
inicio = -1
fin = len(palabra)
palindromo = True

while(inicio < fin):
    inicio += 1
    fin -= 1

    if(palabra[inicio] != palabra[fin]):
        palindromo = False
        break
    

if(palindromo == True):
    print("La palabra", palabra, "es palindroma")
else:
    print("La palabra", palabra, "NO es palindroma")

#Practica 3 punto 4
print("PUNTO #4")
cadena = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
palabra = input("Ingrese una palabra: ")
num = int(input("Ingrese un numero del 1 al 26: "))
palabra_nueva = ""

for i in range(len(palabra)):
    x = cadena.index(palabra[i])
    x += num
    palabra_nueva = palabra_nueva + cadena[x]

print(palabra_nueva)