nombres = ['Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
           'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
           'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
           'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
           'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
           'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
           'Yanina']

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
           85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

#A. Generar una estructura con todas las notas relacionando el nombre del estudiante con las notas.
def generar_estructura_notas(nombres, notas_1, notas_2):
    """
    Genera un diccionario con el nombre del estudiante como clave y una lista con sus 2 notas como valor
    """
    dicci_notas = {}
    for i in range(len(nombres)):
        dicci_notas[nombres[i]] = [notas_1[i], notas_2[i]]
    return dicci_notas

dicci_notas = generar_estructura_notas(nombres, notas_1, notas_2)
print("----------------------")
print("Estructura de notas:")
for estudiante, notas in dicci_notas.items():           #en cada iteración, las variables estudiante y notas tomarán los valores de la clave y el valor del dicci_notas
    print(f"{estudiante}: --> {notas[0]} - {notas[1]}")


# B. Calcular el promedio de notas de cada estudiante.
def promedio_notas_estudiante(estudiante_notas):
    """
    Calcula el promedio de notas de un estudiante dada su lista de notas
    """
    promedio = sum(estudiante_notas) / len(estudiante_notas)
    return promedio

def promedios_notas_estudiantes(dicci_notas):
    """
    Calcula los promedios de notas de cada estudiante en un diccionario de notas.
    """
    #utiliza map para calcular los promedios de notas de cada estudiante en dicci_notas y los almacena en una lista promedios
    promedios = map(promedio_notas_estudiante, dicci_notas.values())

    #creo otra lista con las claves (nombre de estudiante) del dicci_notas
    estudiantes = list(dicci_notas.keys())
    
    #retorno un diccionario combinando las listas de estudiantes y sus promedios
    return dict(zip(estudiantes, promedios))

promedios = promedios_notas_estudiantes(dicci_notas)
for estudiante, promedio in promedios.items():
    print(f"El promedio de notas de {estudiante} es: {promedio}")




#C. Calcular el promedio general del curso.

def promedio_general_curso(notas):
    """
    Calcula el promedio general del curso a partir de la estructura de notas
    """
    suma_notas = 0
    total_estudiantes = len(notas)

    for estudiante in notas:                # por cada estudiante voy sumando sus notas y guardando en una suma total 
        suma_notas += sum(notas[estudiante])      

    promedio = suma_notas / (total_estudiantes * 2)     #se multiplica *2 porque cada estudiante tiene 2 notas
    return promedio


promedio = promedio_general_curso(dicci_notas)
print("----------------------")
print("El promedio general del curso es: {:.2f}".format(promedio))


#D. Identificar al estudiante con la nota promedio más alta.

estudiante_con_promedio_mas_alto = max(promedios, key=promedios.get)
promedio_mas_alto = promedios[estudiante_con_promedio_mas_alto]

print(f"La materia con el promedio más alto es {estudiante_con_promedio_mas_alto} con un promedio de {promedio_mas_alto}")


#E. Identificar al estudiante con la nota más baja.

def estudiante_peor_nota(notas):
    """
    Identifica al estudiante con la nota más baja a partir de la estructura de notas
    """
    peor_nota = 100
    peor_estudiante = ""
    for estudiante in notas:
        nota_minima = min(notas[estudiante])
        if nota_minima < peor_nota:
            peor_nota = nota_minima
            peor_estudiante = estudiante
    return peor_estudiante

print("----------------------")
print(f"El estudiante con la nota mas baja es:{estudiante_peor_nota(dicci_notas)} ")
print("----------------------")



