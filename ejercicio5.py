frase = input("Ingrese una frase: ")
string = input("Ingrese un string: ")

# Convertir todo a minúsculas para no distinguir entre mayúsculas y minúsculas
frase = frase.lower()
string = string.lower()

# Dividir la frase en una lista de palabras
palabras = frase.split()

# Contar la cantidad de palabras que contienen el string
contador = 0
for palabra in palabras:
    if string in palabra:
        contador += 1

print("La cantidad de palabras que contienen el string es:", contador)