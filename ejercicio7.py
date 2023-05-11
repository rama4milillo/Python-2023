texto = """
 El salario promedio de un hombre en Argentina es de $60.000, mientras que
el de una mujer es de $45.000. Además, las mujeres tienen menos
posibilidades de acceder a puestos de liderazgo en las empresas.
 """

# Identificar mayúsculas, minúsculas y caracteres no letras en la frase
mayusculas = 0
minusculas = 0
no_letras = 0

for caracter in texto:
    if caracter.isupper():
        mayusculas += 1
    elif caracter.islower():
        minusculas += 1
    elif not caracter.isalpha():
        no_letras += 1

# Dividir la frase en una lista de palabras
palabras = texto.lower().split()

# Contar la cantidad de palabras
cantidad_palabras = len(palabras)

print("Mayúsculas:", mayusculas)
print("Minúsculas:", minusculas)
print("No letras:", no_letras)
print("Cantidad de palabras:", cantidad_palabras)
