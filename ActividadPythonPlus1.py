#Solución
from datetime import datetime
import json
import csv


def actividad_usuario(nombre_usuario, filtro="FACULTAD"):
        archivo =  open('log_catedras.csv', 'r')
        lector_csv = csv.reader(archivo)
        encabezado = next(lector_csv) # Saltar la primera fila con los encabezados
        actividad = []            # lista que contiene los registros de actividad del usuario solicitado
        for fila in lector_csv:  # la variable fila contiene una lista con los valores de cada columna de la fila actual del archivo CSV
            hora = fila[0]
            usuario = fila[1]
            usuario_afectado = fila[2]
            contexto = fila[3]
            nombre_evento = fila[4]
            descripcion = fila[5]
            direccion_ip = fila[6]

            # Filtrar por dirección IP
            if filtro == "FACULTAD" and not direccion_ip.startswith("163.10"):
                continue
            elif filtro == "EXTERIOR" and direccion_ip.startswith("163.10"):
                continue

            # Filtrar por usuario
            if usuario == nombre_usuario:
                actividad.append(fila)

        return actividad


def mostrar_actividad(usuario):
    print(f"Usuario: {usuario}")
    print("-" * 50)
    print("{:<10} {:<20} {:<15} {:<8}".format("Dia", "Recurso accedido", "Dir IP", "Hora"))
    print("-" * 50)
    actividades = actividad_usuario(usuario)     # lista que almacena todas las actividades del usuario seleccionado
    for actividad in actividades:     # itero esa lista y la imprimo con el formato pedido
        fecha = actividad[0].strftime("%d/%m/%y")
        recurso = actividad[1][:20] + "..." if len(actividad[1]) > 20 else actividad[1]   #si len es mayor a 20 solo imprimo 20
        ip = actividad[2]
        hora = actividad[0].strftime("%H:%M:%S")
        print("{:<10} {:<20} {:<15} {:<8}".format(fecha, recurso, ip, hora))
    
mostrar_actividad("Hypno")




