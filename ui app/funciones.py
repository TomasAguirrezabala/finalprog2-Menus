import requests as rq
from os import system
import json
import random



def menuInicial():
    opcion = 0
    while not(opcion>=1 and opcion<=3):
        system("cls")
        print('=====================')
        print('PELISPEDIA')
        print('=====================')
        print('1) Iniciar sesion')
        print('2) Ingresar como invitado')
        print('3) Para salir')
        print('=====================')
        opcion = int(input('Ingrese una opcion: '))
    return opcion              

# incio de sesion
def inicio_de_sesion():
    system('cls')
    try:
        #cargo los usuarios
        usuariosData = rq.get("http://127.0.0.1:5000/usuarios")
        usuarios = usuariosData.json()
    except:
        print("Ocurrió un error al intentar cargar los usuarios.")
        return False
    #pido los datos
    while True:
        system("cls")
        print('*Iniciar sesión*')
        input_id = input('ID: ')
        input_contrasena = input('Contraseña: ').lower()
        if input_id == '' or input_contrasena == '':
                print ('Por favor, no deje ningun campo vacio.')
                input('Enter para continuar...')
                system('cls')
                continue
        encontrado = False  
        for usuario in usuarios:
            if usuario['usuarioID'] == input_id and usuario['contrasena'] == input_contrasena:
                usuarioID = usuario["usuarioID"]
                admin = usuario["admin"]
                encontrado = True
        if encontrado == False:
            system("cls")
            print('*Iniciar sesión*')
            print("ID o contraseña incorrectos") 
            input("Enter para continuar.")
        else: 
            system("cls")
            print('*Iniciar sesión*')
            print("Inicio de sesion exitoso!") 
            print() 
            input("Enter para continuar.")
            break
    return usuarioID, admin
    
# menu usuario
def menuUsuarioResgistrado():
    system("cls")
    opcionmenu1 = 0
    while not(opcionmenu1>=1 and opcionmenu1<=19):
        print("---MENU---")
        print("1) Mostrar las peliculas disponibles.")
        print("2) Mostrar las ultimas diez peliculas agregadas.")
        print("3) Mostrar peliculas de un director.")
        print("4) Mostrar las peliculas con portada.")
        print("5) Agregar una pelicula.")
        print("6) Eliminar una pelicula.")
        print("7) Modificar una pelicula.")
        print("8) ABM Comentarios")
        print("9) Buscar pelicula o director.")
        print("10) Puntuar pelicula.")
        print("11) Agregar usuario.")   
        print("12) Eliminar usuario.") 
        print("13) Dar admin")
        print("14) Sacar admin")
        print("15) Pelicula aleatoria!")
        print("16) Mostrar visualizaciones por pelicula")
        print("17) ABM Directores")
        print("18) ABM Generos")
        print("19) Salir.")
        opcionmenu1=int(input("ingresar opcion: "))
    return opcionmenu1

# menu comentarios
def menuComentarios():
    opcion = 0
    while not(opcion>=1 and opcion<=5):
        system("cls")
        print('=====================')
        print("1) Agregar un comentario.")
        print("2) Eliminar un comentario.")
        print("3) Editar un comentario.")
        print("4) Salir")
        print('=====================')
        opcion = int(input('Ingrese opcion: '))
    return opcion

# muestra las peliculas
def mostrarPelis():
    pelisData = rq.get("http://127.0.0.1:5000/pelis")
    peliculas = pelisData.json()
    system("cls")
    print("Las peliculas disponibles son: ")
    print()

    for pelicula in peliculas:
        print(f"{pelicula['nombre']}")
        print()

    enteras = input('Si quieres conocer todos los detalles de las peliculas, ingresa "y", si quieres \
volver al menu, ingresa "n": ').lower()

    if enteras == "y":
        if len(peliculas) > 5:
            paginado()
        else:
            for pelicula in peliculas:
                print(f'{pelicula["nombre"]} con id: {pelicula["peliculaID"]}, genero: {pelicula["generoPeli"]}, del año: {pelicula["anio"]}\
        y su sinopsis es: {pelicula["sinopsis"]}')
                print()

            input("Enter para continuar.")
    elif enteras == "n":
        return
    else:
        print("Opcion no valida")
        input("Enter para continuar...")

# muestra las ultimas 10 pelis
def ultimas10Pelis():
    system("cls")
    print("Las ultimas diez peliculas agregadas son:")
    ult_10_pelis_data = rq.get("http://127.0.0.1:5000/ultimas_diez_peliculas")
    ult_10_pelis = ult_10_pelis_data.json()
    for i, pelicula in enumerate(ult_10_pelis):
        print(f'{pelicula["nombre"]} con id: {pelicula["peliculaID"]}, genero: {pelicula["generoPeli"]}, del año: {pelicula["anio"]}\
 y su sinopsis es: {pelicula["sinopsis"]}')
        print()
        if i == 9:
            break
    input("Enter para continuar.")    

# muestra las peliculas por un director
def pelisDirector():
    system("cls")
    directorID = input("Ingrese la id del director: ")
    try:
        peliculasDirectorData = rq.get(f"http://127.0.0.1:5000/peliculas/director/{directorID}")
        peliculasDirector = peliculasDirectorData.json()
        print()
        print("Las peliculas de este director son: ")
        print()
        for peliDirector in peliculasDirector:
            print(f'{peliDirector["nombre"]} con id: {peliDirector["peliculaID"]}, genero: {peliDirector["generoPeli"]}, del año: {peliDirector["anio"]}\
 y su sinopsis es: {peliDirector["sinopsis"]}')
            print()
        input('Enter para continuar...')
    except rq.exceptions.JSONDecodeError:
        print()
        print("Este director no existe o no tiene peliculas para mostrar")         
        input('Enter para continuar...')   

# muestra las peli con portada
def peliPortada():
    system("cls")
    peliPortadaData = rq.get("http://127.0.0.1:5000/peliculas/portada")
    peliPortada = peliPortadaData.json()
    print()
    print("-----------------------------------")
    print("Las peliculas con portada son: ")
    print("-----------------------------------")
    print()
    for peliConPortada in peliPortada:
        print(f'{peliConPortada["nombre"]} con id: {peliConPortada["peliculaID"]}, genero: {peliConPortada["generoPeli"]}, portada: {peliConPortada["portada"]}\
, id del director: {peliConPortada["directorID"]} y del año: {peliConPortada["anio"]}')
        print()
    input('Enter para continuar...')           

# agregar una peli
def peliAgregar():
    peliculaNueva = []
    # nombre de la peli nueva
    nombrePeliAgregar = input("Ingrese el nombre de la pelicula a agregar: ")
    while nombrePeliAgregar == "" or (len(nombrePeliAgregar)) > 196:
        system ("cls")
        print('=====================')
        print("Esa pelicula no existe, o ingreso un nombre vacio")
        print('=====================')
        titulo = input("Ingrese el nombre de la pelicula a agregar: ")
    # año de la peli nueva
    anioPeliAgregar = input(f"Ingrese el año de estreno para {nombrePeliAgregar}: ")
    while (len(anioPeliAgregar) != 4):
        system("cls")
        print("=====================")
        print(f'{anioPeliAgregar} no es valido, debe tener 4 numeros. Ej: 2002')
        print("=====================")
        anioPeliAgregar = input(f"Ingrese el año de estreno para {nombrePeliAgregar}: ")
    # genero de la peli nueva
    generosData = rq.get('http://127.0.0.1:5000/generos')
    generos = generosData.json()
    for genero in generos:
        print(f'Los generos disponibles son: {genero["generoNombre"]}')    

    generoPeliAgregar = input("Que genero quiere?: ")
    # director de la peli nueva
    directoresData = rq.get("http://127.0.0.1:5000/directores")
    directores = directoresData.json()
    print("Los directores disponibles son: ")
    for director in directores:
        print(f'{director["director"]} con id: {director["idDirector"]}')
    
    directorPeliAgregar = input("Que director quiere? Escriba el id del director. Ej: 1. : ")
    # sinopsis de la peli nueva
    sinopsisPeliAgregar = input(f"Ingrese su sinopsis para {nombrePeliAgregar}: ")
    while (sinopsisPeliAgregar == ""):
        system ("cls")
        print('=====================')
        print("La sinopsis no puede estar vacía.")
        print('=====================')
        sinopsisPeliAgregar = input(f"Ingrese su sinopsis para {nombrePeliAgregar}: ")
        
    imagenPeliAgregar = input(f'Ingrese el URL de la imagen para {nombrePeliAgregar}: ')
    # peli nueva
    peliAgregar = {
        "anio": anioPeliAgregar,
        "comentariosID": [],
        "directorID": directorPeliAgregar,
        "generoPeli": generoPeliAgregar,
        "nombre":nombrePeliAgregar,
        "peliculaID": "",
        "portada": imagenPeliAgregar,
        "puntuacion": "",
        "puntuaciones": {},
        "sinopsis": sinopsisPeliAgregar,
        "visualizaciones": 0
    }
    # paso a json
    dataEnviar = json.dumps(peliAgregar)
    # si no aclaras el tipo de contenido no te deja
    encabezado = {'Content-type': 'application/json'}
    # post
    response = rq.post("http://127.0.0.1:5000/peliculas/agregar", data=dataEnviar, headers=encabezado)
    
    print(response.text)
    input('Enter para continuar...')

# eliminar una peli 
def peliEliminar(usuarioID):
    system("cls")
    print('=====================')
    print('Borrar una pelicula')
    print('=====================')
    pelisData = rq.get("http://127.0.0.1:5000/pelis")
    peliculas = pelisData.json()
    print("Las peliculas disponibles son: ")
    print()
    for pelicula in peliculas:
        print(f'#{pelicula["nombre"]} con id: {pelicula["peliculaID"]}')
        print()
    print()
    
    while True: 
        peliculaID = input('Ingrese el id de la peli que quiere borrar(x para salir): ')
        if peliculaID != 'x':
            datos = rq.delete(f'http://127.0.0.1:5000/peliculas/{peliculaID}/usuarioID/{usuarioID}/eliminar')
            mensaje = datos.text
            print("=====================")
            print(mensaje)
            print("=====================")
        else:
            system("cls")
            print("===================================================")
            print('Usted cancelo la eliminacion')
            print("===================================================")
            break


def modificar_pelicula():
    opcion_modificar = 0
    system("cls")
    while not(opcion_modificar>=1 and opcion_modificar<=7): 
        print('Modificar Pelicula')
        print('1) Titulo')
        print('2) Director')
        print('3) Genero')
        print('4) Año')
        print('5) Portada')
        print('6) Sinopsis')
        print('7) Terminar/Salir')
        opcion_modificar = int(input('Ingresar opcion: '))

    pelisData = rq.get("http://127.0.0.1:5000/pelis")
    peliculas = pelisData.json()
    print("Las peliculas disponibles son: ")
    print()
    for pelicula in peliculas:
        print(f'#{pelicula["nombre"]} con id: {pelicula["peliculaID"]}')
        print()
    modificar = int(input('Ingrese la ID de la pelicula que desea modificar: '))
    #peli vacia donde guarda cada cambio para poder hacer mas de 1 cambio antes de enviar los datos
    modificaciones_pelicula = {
        "anio": "",
        "comentariosID": [],
        "directorID": "",
        "generoPeli": "",
        "nombre": "",
        "peliculaID": "",
        "portada": "",
        "puntuacion": "",
        "puntuaciones": {},
        "sinopsis": "",
        "visualizaciones": 0
    }
    data = rq.get('http://127.0.0.1:5000/pelis')
    peliculas = data.json()
    for pelicula in peliculas:
        if pelicula["peliculaID"] == modificar:
            system('cls')
            while opcion_modificar != 7:
                opcion_modificar = modificar_pelicula()
                if opcion_modificar == 1:
                    while True:
                        modif = input(f"El titulo a modificar es '{pelicula['nombre']}', Ingrese su nuevo valor: ")
                        if modif != "":
                            modificaciones_pelicula["nombre"] = modif
                            system('cls')
                            print('Titulo modificado con exito.')
                            break
                        else:
                            system('cls')
                            print("Es necesario ingresar un valor.")
                elif opcion_modificar == 2:
                    contador = 0
                    while True:
                        directoresData = rq.get("http://127.0.0.1:5000/directores")
                        directores = directoresData.json()
                        print("Los directores disponibles son: ")
                        for director in directores:
                            contador = contador + 1
                            print(f'{director["director"]} con id: {director["idDirector"]}')
                        modif = int(input(f"El ID del director actual es '{pelicula['directorID']}', Ingrese su nuevo valor: "))
                        if modif > 0 and modif <= contador:
                            str(modif)
                            modificaciones_pelicula["idDirector"] = modif
                            system('cls')
                            print('Director modificado con exito.')
                            break
                        else:
                            system('cls')
                            print("error, ingrese un id de director valido.")
                elif opcion_modificar == 3:
                    generos_disponibles = []
                    while True:
                        generosData = rq.get('http://127.0.0.1:5000/generos')
                        generos = generosData.json()
                        print("los generos disponibles son:")
                        for genero in generos:
                            generos_disponibles.append(genero["generoNombre"])
                            print(f'-{genero["generoNombre"]}')
                        modif = str(input(f"El genero a modificar es '{pelicula['generoPeli']}', Ingrese su nuevo valor: "))
                        if modif.lower() in generos_disponibles:
                            modificaciones_pelicula["generoPeli"] = modif.lower()
                            system('cls')
                            print('Genero modificado con exito.')
                            break
                        else:
                            system('cls')
                            print("error, ingrese un genero valido.")
                elif opcion_modificar == 4:
                    while True:
                        modif = input(f"El año a modificar es '{pelicula['anio']}', Ingrese su nuevo valor: ")
                        if len(modif) == 4:
                            modificaciones_pelicula["anio"] = modif
                            system('cls')
                            print('Año modificado con exito.')
                            break
                        else:
                            system('cls')
                            print("El valor d esta casilla debe ser de 4 cifras")
                elif opcion_modificar == 5:
                    while True:
                        modif = input(f"El URL de la portada actual es '{pelicula['portada']}', Ingrese su nuevo valor: ")
                        if "http" in modif:
                            modificaciones_pelicula["portada"] = modif
                            system('cls')
                            print('Portada modificada con exito.')
                            break
                        else:
                            system('cls')
                            print("para editar la portada se debe ingresar una URL.")
                elif opcion_modificar == 6:
                    while True:
                        modif = input(f"La sinopsis actual es '{pelicula['sinopsis']}', Ingrese su nuevo valor: ")
                        if len(modif) > 0:
                            modificaciones_pelicula["sinopsis"] = modif
                            system('cls')
                            print('Sinopsis modificada con exito.')
                            break
                        else:
                            system('cls')
                            print("La sinopsis no puede estar vacia.")
                elif opcion_modificar == 7:
                    print("saliendo de *modificar pelicula*")
                    break

                if opcion_modificar >= 1 and opcion_modificar <=6:
                    modificaciones_pelicula["peliculaID"] = modificar
                    datos = rq.put(f'http://127.0.0.1:5000/peliculas/modif/', json=modificaciones_pelicula)
                    mensaje = datos.text
                    print("*")
                    print(mensaje)
                    print("*")
                    input('Enter para continuar...')


def paginado():
    pelisData = rq.get("http://127.0.0.1:5000/pelis")
    peliculas = pelisData.json()
    num_peliculas = len(peliculas)
    peliculas_por_pagina = 4
    num_paginas = (num_peliculas + peliculas_por_pagina - 1) // peliculas_por_pagina # División entera redondeando hacia arriba
    pagina_actual = 0
    while True:
        inicio = pagina_actual * peliculas_por_pagina
        fin = min(num_peliculas, inicio + peliculas_por_pagina)
        system("cls")
        print(f"*pagina {pagina_actual+1}/{num_paginas}*")
        for pelicula in peliculas[inicio:fin]:
            print(f'{pelicula["nombre"]} con id: {pelicula["peliculaID"]}, genero: {pelicula["generoPeli"]}, del año: {pelicula["anio"]}, y su sinopsis es: {pelicula["sinopsis"]}\n')
        opcion = ""
        while opcion not in ["x", "-", "+"]:
            opcion = input(' "-" para pagina anterior y "+" para siguiente pagina.("x" para salir)')
        if opcion == "+":
            if pagina_actual < num_paginas - 1:
                pagina_actual += 1
        elif opcion == "-":
            if pagina_actual > 0:
                pagina_actual -= 1
        else:
            return


def promedio_puntuacion(id_Peli, peliculas):
    puntos = []
    for pelicula in peliculas:
        if pelicula["peliculaID"] == id_Peli:
            for key, value in pelicula.items():
                if key == "puntuaciones":
                    for i, p in value.items():
                        puntos.append(p)
            pelicula["puntuacion"] = sum(puntos)


def puntuar_peli(usuarioID):
    pelisData = rq.get("http://127.0.0.1:5000/pelis")
    peliculas = pelisData.json()
    system("cls")
    system("cls")
    print("Las peliculas disponibles son: ")
    print()
    for pelicula in peliculas:
        print(f"{pelicula['nombre']}" + " ID: "+ f"{pelicula['peliculaID']}")
        print("-------------")

    id_peli = input("Ingrese el ID de la película que desea puntuar: ")
    for pelicula in peliculas:
        if pelicula["peliculaID"] == id_peli:
            if usuarioID in pelicula["puntuaciones"]:
                print("Usted ya puntuó esta película.")
                input("Enter para continuar.")
                return

            puntuacion = int(input("Ingrese la puntuación de 0 a 5: "))
            if 0 <= puntuacion <= 5:
                pelicula["puntuaciones"][usuarioID] = puntuacion
                promedio_puntuacion(id_peli, peliculas)
                datos = rq.put(f"http://127.0.0.1:5000/peliculas/actualizar", json=peliculas)
                print("Película puntuada con éxito.")
            else:
                print("La puntuación ingresada debe ser de 0 a 5.")
            input("Enter para continuar.")
            return

    print("Error al encontrar la película.")
    input("Enter para volver...")


def buscar_pelicula_o_director():
    pelisData = rq.get("http://127.0.0.1:5000/pelis").json()
    directoresData = rq.get("http://127.0.0.1:5000/directores").json()

    peliculas_encontradas = []
    directores_encontrados = []
    system("cls")
    
    print("Desea buscar por título o por director?")
    print("1) Por título.")
    print("2) Por director.")
    opcion = input("Ingrese opción: ")
    
    if opcion == "1":
        buscar = input("Ingrese el título que busca: ")
        for pelicula in pelisData:
            if buscar.lower() in pelicula['nombre'].lower():
                if buscar.lower() in pelicula['nombre'].lower():
                    pelicula["visualizaciones"] = pelicula["visualizaciones"] + 1
                    datos = rq.put(f"http://127.0.0.1:5000/peliculas/actualizar", json=pelisData)
                peliculas_encontradas.append(pelicula)
        if peliculas_encontradas:
            print(f'Se encontraron {len(peliculas_encontradas)} películas:')
            for peli in peliculas_encontradas:
                print(f'- {peli["nombre"]} (id: {peli["peliculaID"]}), género: {peli["generoPeli"]}, año: {peli["anio"]}, sinopsis: {peli["sinopsis"]}')
        else:
            print("No se encontraron películas.")
        input("Presione Enter para volver...")
            
    elif opcion == "2":
        buscar = input("Ingrese el director que busca: ")
        for director in directoresData:
            if buscar.lower() in director['director'].lower():
                directores_encontrados.append(director)
        if directores_encontrados:
            print(f'Se encontraron {len(directores_encontrados)} directores:')
            for director in directores_encontrados:
                print(f'- {director["director"]} (id: {director["idDirector"]})')
        else:
            print("No se encontraron directores.")
        input("Presione Enter para volver...")
    else:
        print("Opción no válida")
        input("Presione Enter para continuar...")


# empieza ABM comentarios
# empieza ABM comentarios
# empieza ABM comentarios

# agregar comentario
def agregarComentario(usuarioID):
    system("cls")
    print("--------------------")
    print("Agregar un comentario")
    print("--------------------")
    pelisData = rq.get("http://127.0.0.1:5000/pelis")
    peliculas = pelisData.json()
    print("Las peliculas disponibles son: ")
    print()
    for pelicula in peliculas:
        print(f'#{pelicula["nombre"]} con id: {pelicula["peliculaID"]}')
        print()
    print()
    idPeliAgregar = input("¿A que pelicula le quiere agregar un comentario? Ingrese el ID: ")
    print()
    encontrado = False
    
    for pelicula in peliculas:
        if pelicula["peliculaID"] == idPeliAgregar:
            encontrado = True
            comentario = input("Ingrese su comentario: ")
            nuevoComentario={"comentarioID":"","usuarioID":usuarioID,"comentario":comentario}
            datos = rq.post(f'http://127.0.0.1:5000/pelicula/{idPeliAgregar}/comentarios/agregar', json=nuevoComentario)
            respuestaFlask = datos.text
            print("=====================")
            print(respuestaFlask)
            print("=====================")
    
    if encontrado == False:
        print("=====================")
        print('Error al crear el comentario')
        print("=====================")
            
    input('Ingrese enter para continuar...')

# eliminar comentario
def eliminarComentario(usuarioID):
    # Obtener los comentarios del usuario
    comentariosUsuarioData = rq.get(f"http://127.0.0.1:5000/comentarios/usuarioID/{usuarioID}")
    comentariosUsuario = comentariosUsuarioData.json()
    
    # Mostrar los comentarios del usuario
    if len(comentariosUsuario) != 0:
        print('Sus comentarios son:')
        for comentario in comentariosUsuario:
            print(f"ID: {comentario['comentarioID']}, Comentario: {comentario['comentario']}")
        
        # Pedir al usuario que ingrese el ID del comentario que desea eliminar
        while True:
            print()
            comenBorrarID = input("Ingrese el ID del comentario que desea eliminar (0 para salir): ")
            if comenBorrarID == '0':
                # Si el usuario ingresa 0, salir de la función
                return "Usted cancelo la eliminacion"
            elif comenBorrarID.isdigit():
                # Si el usuario ingresa un número entero válido, verificar si existe en la lista de comentarios del usuario
                comentarioEncontrado = False
                for comentario in comentariosUsuario:
                    if comentario['comentarioID'] == comenBorrarID:
                        comentarioEncontrado = True
                        break
                
                if comentarioEncontrado == True:
                    # Si el comentario existe, enviar una solicitud para eliminarlo
                    datos = rq.delete(f"http://127.0.0.1:5000/comentarios/{comenBorrarID}/usuarioID/{usuarioID}/borrar")
                    mensaje = datos.text
                    print("==================================")
                    print(mensaje)
                    print("==================================")
                    input('Ingrese enter para continuar...')
                    break
                else:
                    print("===================================================")
                    print('Error, ingresó un número que no es suyo o no existe')
                    print("===================================================")
                    input('Ingrese enter para continuar...')
            else:
                print("===================================================")
                print('Error, ingrese un número entero válido')
                print("===================================================")
                input('Ingrese enter para continuar...')
    else:
        print("=======================")
        print('No tiene comentarios.')
        print("=======================")
        input('Ingrese enter para continuar...')

# modificar comentario
def modificarComentario(usuarioID):
    # Obtener los comentarios del usuario
    comentariosUsuarioData = rq.get(f"http://127.0.0.1:5000/comentarios/usuarioID/{usuarioID}")
    comentariosUsuario = comentariosUsuarioData.json()
    
    # Mostrar los comentarios del usuario
    if len(comentariosUsuario) != 0:
        print('Sus comentarios son:')
        for comentario in comentariosUsuario:
            print(f"ID: {comentario['comentarioID']}, Comentario: {comentario['comentario']}")

        # Pedir al usuario que ingrese el ID del comentario que desea modificar
        while True:
            print()
            comenEditarID = input("Ingrese el ID del comentario que desea modificar (0 para salir): ")
            if comenEditarID == '0':
                # Si el usuario ingresa 0, salir de la función
                print("Usted cancelo la edicion")
                
            elif comenEditarID.isdigit():
                # Si el usuario ingresa un número entero válido, verificar si existe en la lista de comentarios del usuario
                comentarioEncontrado = False
                for comentario in comentariosUsuario:
                    if comentario['comentarioID'] == comenEditarID:
                        #pedimos el texto nuevo
                        while True:
                            comenModificado = input("Ingrese el comentario nuevo: ")
                            if comenModificado == "":
                                print("No puede dejar el comentario vacio.")
                                continue
                            else:
                                comentarioEncontrado = True
                                break
                
                if comentarioEncontrado == True:
                    # Si el comentario existe, enviar una solicitud para modificarlo
                    comenEditado = {"comentarioID":comenEditarID,"usuarioID":usuarioID,"comentario":comenModificado}
                    datos = rq.put(f"http://127.0.0.1:5000/comentarios/modificar", json=comenEditado)
                    mensaje = datos.text
                    print("==================================")
                    print(mensaje)
                    print("==================================")
                    input('Ingrese enter para continuar...')
                    break
                else:
                    print("===================================================")
                    print('Error, ingresó un número que no es suyo o no existe')
                    print("===================================================")
                    input('Ingrese enter para continuar...')
            else:
                print("===================================================")
                print('Error, ingrese un número entero válido')
                print("===================================================")
                input('Ingrese enter para continuar...')
    else:
        print("=======================")
        print('No tiene comentarios.')
        print("=======================")
        input('Ingrese enter para continuar...')
# termina ABM comentarios
# termina ABM comentarios
# termina ABM comentarios

# empieza abm usuario
# empieza abm usuario
# empieza abm usuario

def agregarUsuario():
    system("cls")
    print("--------------------")
    print("Registrar un Usuario")
    print("--------------------")
    while True:
        nombreUsuarioNuevo = input("Ingresa el nombre del nuevo usuario: ")
        contraUsuarioNuevo = input("Ingresa la contraseña del nuevo usuario: ")
        if nombreUsuarioNuevo == "" or contraUsuarioNuevo == "":
            print("No debes dejar ningun campo vacio")
            input("Enter para continuar.")
        else: 
            nuevoUsuario = {f"usuario":nombreUsuarioNuevo,"contrasena":contraUsuarioNuevo,"usuarioID":"","admin":False}
            datos = rq.post('http://127.0.0.1:5000/usuarios/abm', json=nuevoUsuario)
            respuestaFlask = datos.text
            print("=====================")
            print(respuestaFlask)
            print("=====================")
            input("Enter para continuar.")
            break

def eliminarUsuario(admin):
    system("cls")
    print("--------------------")
    print("Eliminar un Usuario")
    print("--------------------")
    esAdmin = False 
    if admin == True:
        esAdmin = True
    else:
        esAdmin=False
        
    if esAdmin == False:
        print("Solo los administradores pueden eliminar un usuario")
        input("Enter para continuar.")
        return
    else:
        usuariosData = rq.get('http://127.0.0.1:5000/usuarios')
        usuarios = usuariosData.json()
        print('Los usuarios disponibles son: ')
        for usuario in usuarios:
            print(f'Usuario: {usuario["usuario"]}')
            print(f'ID: {usuario["usuarioID"]}')
    # Pedir al usuario que ingrese el ID del usuario que desea eliminar
    while True:
        print()
        usuarioBorrarID = input("Ingrese el ID del usuario que desea eliminar (0 para salir): ")
        if usuarioBorrarID == '0':
            # Si el usuario ingresa 0, salir de la función
            print("Usted cancelo la eliminacion")
            input("Enter para continuar.")
            return
        elif usuarioBorrarID.isdigit():
            # Si el usuario ingresa un número entero válido, verificar si existe en la lista de usuarios
            usuarioEncontrado = False
            for usuario in usuarios:
                if usuario['usuarioID'] == usuarioBorrarID:
                    usuarioEncontrado = True
                    break
            
            if usuarioEncontrado == True:
                # Si el usuario existe, enviar una solicitud para eliminarlo
                encabezado = {"Content-Type":"application/json"}
                datos = rq.delete(f"http://127.0.0.1:5000/usuarios/{usuarioBorrarID}/eliminar", headers=encabezado)
                mensaje = datos.text
                print("==================================")
                print(mensaje)
                print("==================================")
                input('Ingrese enter para continuar...')
                break
            else:
                print("===================================================")
                print('Error, ingresó un número que no existe')
                print("===================================================")
                input('Ingrese enter para continuar...')
        else:
            print("===================================================")
            print('Error, ingrese un número entero válido')
            print("===================================================")
            input('Ingrese enter para continuar...')

def darAdmin(admin):
    system("cls")
    print("--------------------")
    print("Hacer Admin a un Usuario")
    print("--------------------")
    
    esAdmin = False 
    
    if admin == True:
        esAdmin = True
    else:
        esAdmin=False
        
    if esAdmin == False:
        print("Solo los administradores pueden hacer admin a un usuario")
        input("Enter para continuar.")
        return
    else:
        print("Lista de usuarios: ")
        usuariosData = rq.get('http://127.0.0.1:5000/usuarios')
        usuarios = usuariosData.json()
        for usuario in usuarios:
            print(f'Usuario: {usuario["usuario"]}')
            print(f'ID: {usuario["usuarioID"]}')
            
        # Pedir al usuario que ingrese el ID del usuario que desea hacer admin
    while True:
        print()
        nuevoAdminID = input("Ingrese el ID del usuario que desea dar admin (0 para salir): ")
        if nuevoAdminID == '0':
            # Si el usuario ingresa 0, salir de la función
            print("Usted cancelo la accion")
            input("Enter para continuar.")
            return
        elif nuevoAdminID.isdigit():
            # Si el usuario ingresa un número entero válido, verificar si existe en la lista de usuarios
            usuarioEncontrado = False
            for usuario in usuarios:
                if usuario['usuarioID'] == nuevoAdminID:
                    usuarioEncontrado = True
                    break
            
            if usuarioEncontrado == True:
                # Si el usuario existe, enviar una solicitud para hacerlo admin
                encabezado = {"Content-Type":"application/json"}
                datos = rq.put(f"http://127.0.0.1:5000/usuarios/admin/{nuevoAdminID}", headers=encabezado)
                mensaje = datos.text
                print("==================================")
                print(mensaje)
                print("==================================")
                input('Ingrese enter para continuar...')
                break
            else:
                print("===================================================")
                print('Error, ingresó un número que no existe')
                print("===================================================")
                input('Ingrese enter para continuar...')
        else:
            print("===================================================")
            print('Error, ingrese un número entero válido')
            print("===================================================")
            input('Ingrese enter para continuar...')

def sacarAdmin(admin):
    system("cls")
    print("--------------------")
    print("Quitar Admin a un Usuario")
    print("--------------------")
    
    esAdmin = False 
    
    if admin == True:
        esAdmin = True
    else:
        esAdmin=False
        
    if esAdmin == False:
        print("Solo los administradores pueden quitar el admin a un usuario")
        input("Enter para continuar.")
        return
    else:
        print("Lista de usuarios: ")
        usuariosData = rq.get('http://127.0.0.1:5000/usuarios')
        usuarios = usuariosData.json()
        for usuario in usuarios:
            print(f'Usuario: {usuario["usuario"]}')
            print(f'ID: {usuario["usuarioID"]}')
            
        # Pedir al usuario que ingrese el ID del usuario al que le desea quitar el admin
    while True:
        print()
        exAdminID = input("Ingrese el ID del usuario al que desea quitar el admin (0 para salir): ")
        if exAdminID == '0':
            # Si el usuario ingresa 0, salir de la función
            print("Usted cancelo la accion")
            input("Enter para continuar.")
            return
        elif exAdminID.isdigit():
            # Si el usuario ingresa un número entero válido, verificar si existe en la lista de usuarios
            usuarioEncontrado = False
            for usuario in usuarios:
                if usuario['usuarioID'] == exAdminID:
                    usuarioEncontrado = True
                    break
            
            if usuarioEncontrado == True:
                # Si el usuario existe, enviar una solicitud para sacarle admin
                encabezado = {"Content-Type":"application/json"}
                datos = rq.put(f"http://127.0.0.1:5000/usuarios/admin/eliminar/{exAdminID}", headers=encabezado)
                mensaje = datos.text
                print("==================================")
                print(mensaje)
                print("==================================")
                input('Ingrese enter para continuar...')
                break
            else:
                print("===================================================")
                print('Error, ingresó un número que no existe')
                print("===================================================")
                input('Ingrese enter para continuar...')
        else:
            print("===================================================")
            print('Error, ingrese un número entero válido')
            print("===================================================")
            input('Ingrese enter para continuar...')
             
# termina abm usuario
# termina abm usuario
# termina abm usuario

def peliculaAleatoria():
    system("cls")
    pelisData = rq.get("http://127.0.0.1:5000/pelis")
    peliculas = pelisData.json()
    peliAleatoria = random.choice(peliculas)
    print("Pelicula Aleatoria: ")
    print(f'{peliAleatoria["nombre"]} con id: {peliAleatoria["peliculaID"]}, genero: {peliAleatoria["generoPeli"]}, del año: {peliAleatoria["anio"]}\
y su sinopsis es: {peliAleatoria["sinopsis"]}')
    input("Enter para continuar...")
 
 
def mostrarVisualizaciones():
    system("cls")
    print("--------------------")
    print("Visualizaciones por pelicula")
    print("--------------------")
    pelisData = rq.get("http://127.0.0.1:5000/pelis")
    peliculas = pelisData.json()
    for pelicula in peliculas:
        print("nombre: "f"{pelicula['nombre']}")
        print("ID: "f"{pelicula['peliculaID']}")
        print("Visualizaciones: "f"{pelicula['visualizaciones']}")
        print()
    input("Enter para continuar...")    
    
#abm generos y directores
#abm generos y directores
#abm generos y directores
def menuDirector():
    system("cls")
    opcionMenuDirector = 0
    while not(opcionMenuDirector>=1 and opcionMenuDirector<=3):
        print("--------------------")
        print("Menu ABM Directores")
        print("--------------------")
        print("1) Agregar un Director")
        print("2) Eliminar un Director")
        print("3) Modificar un director")
        opcionMenuDirector=int(input("ingresar opcion: "))
        return opcionMenuDirector


def agregarDirector():
    system("cls")
    print("--------------------")
    print("Registrar un Director")
    print("--------------------")
    while True:
        directorNuevo = input("Ingresa el nombre del nuevo director(0 para salir): ")
        if directorNuevo == "":
            print("No debes dejar ningun campo vacio")
            input("Enter para continuar.")
        elif directorNuevo == 0:
            print("Usted cancelo la accion.")
            input("Enter para continuar...")
            break
        else: 
            nuevoDirector = {f"director":directorNuevo,"idDirector": "idvacio"}
            datos = rq.post('http://127.0.0.1:5000/director/crear', json=nuevoDirector)
            respuestaFlask = datos.text
            print("=====================")
            print(respuestaFlask)
            print("=====================")
            input("Enter para continuar.")
            break
    
def eliminarDirector():
    return
def modificarDirector():
    return
def menuGenero():
    opcionMenuGenero = 1
    return opcionMenuGenero
def agregarGenero():
    return
def eliminarGenero():
    return
def modificarGenero():
    return
#abm generos y directores   
#abm generos y directores
#abm generos y directores
    




# Implementar ABM de directores y Géneros.
