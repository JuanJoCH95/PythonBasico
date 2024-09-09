'''Realizar una función que reciba un texto y esta cuente cada palabra cuantas veces está
dentro de dicho texto y retorne la información en un diccionario'''

def contar_palabras(texto):
  palabras = {}
  texto = texto.lower()
  oraciones = texto.split(" ")
  count = 0

  for i in oraciones:
    for f in oraciones:
      if i == f:
        count += 1

    palabras[i] = count
    count = 0
  
  return palabras

texto = input("Ingrese un texto: ")
conteo = contar_palabras(texto)
print(sorted(conteo.items()))