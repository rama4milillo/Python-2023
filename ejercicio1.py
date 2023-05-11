import PySimpleGUI as sg
import json

#import funciones_agregar_perfil as funciones_agregar_perfil
# Definimos la lista de usuarios
usuarios = [
    {"Alias": "aaaa", "Nombre": "saaaa", "Edad": "32", "Genero": "Femenino", "Imagen": "0.png"},
    {"Alias": "bbbb", "Nombre": "bbbb", "Edad": "22", "Genero": "Masculino", "Imagen": "1.png"},
    {"Alias": "cccc", "Nombre": "bbbb", "Edad": "22", "Genero": "Masculino", "Imagen": "2.png"},
    {"Alias": "dddd", "Nombre": "cccc", "Edad": "30", "Genero": "Femenino", "Imagen": "3.png"},
    {"Alias": "eeee", "Nombre": "dddd", "Edad": "25", "Genero": "Masculino", "Imagen": "4.png"},
    {"Alias": "ffff", "Nombre": "dddd", "Edad": "25", "Genero": "Masculino", "Imagen": "5.png"},
]
def mostrar_todos_los_usuarios(usuarios):
    # Definimos los tamaños de los botones
    boton_tamanio = (10, 4)
    max_botones_por_fila = 4

    # Creamos la lista de botones
    botones = []
    fila_botones = []
    contador_botones_en_fila = 0

    # Mostramos los botones de usuario
    for usuario in usuarios:
        if contador_botones_en_fila == max_botones_por_fila:
            botones.append(fila_botones)
            fila_botones = []
            contador_botones_en_fila = 0

        fila_botones.append(sg.Button(usuario['Alias'], size=boton_tamanio, key=usuario["Alias"],enable_events = True))
        contador_botones_en_fila += 1

    # Si no se terminó de completar la última fila de botones, la agregamos a la lista de botones
    if fila_botones:
        botones.append(fila_botones)

    # Agregamos un botón de "Volver"
    botones.append([sg.Button('Volver', size=boton_tamanio, key='-VOLVER-', pad=((20, 0), (20, 10)))])

    # Creamos el layout con los botones
    layout = [
        [sg.Text('UNLPImage', font=('Helvetica', 20), pad=((20, 0), (20, 10)))],
        [sg.Column(botones, size=(800, 600), scrollable=True, vertical_scroll_only=True)],
    ]


    # Creamos la ventana
    window = sg.Window('Todos los usuarios', layout, size=(800, 600), resizable=True)

    # Mostramos la ventana y leemos eventos
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        # Manejamos los eventos según su key
        if event == '-VOLVER-':
            window.close()
            generar_pantalla_inicio()
        elif event in [usuario["Alias"] for usuario in usuarios]:
            window.close()
            usuario_seleccionado = next(usuario for usuario in usuarios if usuario["Alias"] == event)
            #mp.menu_principal(usuario_seleccionado)
            print(usuario_seleccionado)
            break

    # Cerramos la ventana y terminamos el programa
    window.close()


def generar_pantalla_inicio():
    # Definimos los tamaños de los botones
    boton_tamanio = (10, 4)
    max_botones_por_fila = 4

    # Creamos la lista de botones de usuario y botones adicionales
    botones_usuarios = []
    botones_adicionales = []

    # Si no hay usuarios, solo mostramos el botón de agregar perfil
    if not usuarios:
        botones_adicionales.append([sg.Button('Agregar perfil', size=boton_tamanio, key='-AGREGAR-PERFIL-')])
    else:
        # Mostramos los botones de usuario
        for i, usuario in enumerate(usuarios):
            if i < max_botones_por_fila:
                botones_usuarios.append(sg.Button(usuario['Alias'], size=boton_tamanio, key=usuario["Alias"],enable_events = True))
            else:
                break

        # Si hay menos de 4 usuarios, mostramos también el botón de agregar perfil
        if len(usuarios) < max_botones_por_fila:
            botones_adicionales.append(sg.Button('Agregar perfil', size=boton_tamanio, key='-AGREGAR-PERFIL-'))
        else:
            # Si hay más de 4 usuarios, agregamos un botón para mostrar todos los usuarios
            botones_adicionales.append(sg.Button('Mostrar todos los usuarios', size=boton_tamanio, key='-MOSTRAR-PERFILES-'))
            botones_adicionales.append(sg.Button('Agregar perfil', size=boton_tamanio, key='-AGREGAR-PERFIL-'))
        # Agregamos los botones de usuario y los botones adicionales a la lista de botones
        botones = botones_usuarios + botones_adicionales

    # Creamos el layout con los botones
    layout = [
        [sg.Text('UNLPImage', font=('Helvetica', 20), pad=((20, 0), (20, 10)))],
        [sg.Column([botones_usuarios], size=(800, None), expand_y=True, vertical_scroll_only=True, pad=((20, 20), (0, 0)))],
        [sg.Column([botones_adicionales], size=(800, None), pad=((20, 20), (0, 0)))]
    ]

    # Creamos la ventana
    window = sg.Window('UNLPImage', layout, size=(800, 600), resizable=True)


    # Mostramos la ventana y leemos eventos
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        # Manejamos los eventos según su key
        if event == '-AGREGAR-PERFIL-':
            window.close()
            #funciones_agregar_perfil.crear_ventana_agregar_perfil()
        elif event == '-MOSTRAR-PERFILES-':
            window.close()
            mostrar_todos_los_usuarios(usuarios)
        elif event in [usuario["Alias"] for usuario in usuarios]:
            window.close()
            usuario_seleccionado = next(usuario for usuario in usuarios if usuario["Alias"] == event)
            #mp.menu_principal(usuario_seleccionado)
            print(usuario_seleccionado)
            break

    # Cerramos la ventana y terminamos el programa
    window.close()
generar_pantalla_inicio()