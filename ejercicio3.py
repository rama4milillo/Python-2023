jupyter_info = """ JupyterLab is a web-based interactive development
environment for Jupyter notebooks,
code, and data. JupyterLab is flexible: configure and arrange the user
interface to support a wide range
of workflows in data science, scientific computing, and machine learning.
JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing
ones.
"""

letra = input("Ingresa una letra para buscar las palabras que comienzan con ella: ")

if len(letra) != 1:
    print("Error: debes ingresar una sola letra.")
else:
    palabras = jupyter_info.split()
    palabras_con_letra = []
    for palabra in palabras:
        # Convertir la palabra y la letra en minúsculas y verificar si la palabra comienza con la letra deseada
        if palabra.lower().startswith(letra.lower()):
            # Si la palabra cumple la condición, agregarla a la lista de palabras con la letra deseada
            palabras_con_letra.append(palabra)

    if len(palabras_con_letra) == 0:
        print(f"No hay palabras que comiencen con la letra {letra}.")
    else:
        print(f"Palabras que comienzan con la letra {letra}:")
        for palabra in palabras_con_letra:
            print(palabra)