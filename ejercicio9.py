# Definir la tabla de valores en un diccionario
valores = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1, 
           'D': 2, 'G': 2, 
           'B': 3, 'C': 3, 'M': 3, 'P': 3, 
           'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 
           'K': 5, 
           'J': 8, 'X': 8, 
           'Q': 10, 'Z': 10}

# ingresar una palabra por teclado
palabra = input("Ingrese una palabra: ").upper()

# Calcular el valor de la palabra
valor = 0
for letra in palabra:
    if letra in valores:
        valor += valores[letra]

# Imprimir el valor de la palabra
print("El valor de la palabra", palabra, "es", valor)
