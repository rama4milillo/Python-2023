# Definir el artículo a evaluar
evaluar = """ título: Experiences in Developing a Distributed Agent-based
Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance
computing resources provides the promise of capturing unprecedented details
of large-scale complex systems. However, the specialized knowledge required
for developing such ABMs creates barriers to wider adoption and utilization.
Here we present our experiences in developing an initial implementation of
Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High
Performance Computing (Repast HPC), to identify the key elements of a useful
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages
and the Python C-API to create a scalable modeling system that can exploit
the largest HPC resources and emerging computing architectures.
"""

# Extraer el título del artículo, tomo la primer linea del articulo sacando la etiqueta "titulo"
titulo = evaluar.split("\n")[0].split(": ")[1]

# Contador de oraciones
facil = aceptable = dificil = muy_dificil = 0

# Extraer el resumen del artículo y dividirlo en oraciones, nuevamente saco la etiqueta "resumen"
resumen = evaluar.split("\n")[1].split(": ")[1]
oraciones = resumen.split(". ")

# Verificar cada oración y actualizar el contador correspondiente
for oracion in oraciones:
    palabras = oracion.split()
    if len(palabras) <= 12:
        facil += 1
    elif len(palabras) <= 17:
        aceptable += 1
    elif len(palabras) <= 25:
        dificil += 1
    else:
        muy_dificil += 1

# Imprimir los resultados
print("título:", "ok" if len(titulo.split()) <= 10 else "no cumple")
print("Cantidad de oraciones fáciles de leer:", facil)
print("Cantidad de oraciones aceptables para leer:", aceptable)
print("Cantidad de oraciones difíciles de leer:", dificil)
print("Cantidad de oraciones muy difíciles de leer:", muy_dificil)
