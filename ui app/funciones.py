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
                system("cls")
                print("=====================================")
                print('Por favor, no deje ningun campo vacio.')
                print("=====================================")
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
    while not(opcionmenu1>=1 and opcionmenu1<=14):
        print("---MENU---")
        print("1) Mostrar las peliculas disponibles.")
        print("2) Mostrar las ultimas diez peliculas agregadas.")
        print("3) Mostrar peliculas de un director.")
        print("4) Mostrar las peliculas con portada.")
        print("5) ABM Peliculas.")
        print("6) ABM Comentarios.")
        print("7) Buscar pelicula o director.")
        print("8) Puntuar pelicula.")
        print("9) ABM usuario.")   
        print("10) Pelicula aleatoria!")
        print("11) Mostrar visualizaciones por pelicula.")
        print("12) ABM Directores.")
        print("13) ABM Generos.")
        print("14) Salir.")
        opcionmenu1=int(input("ingresar opcion: "))
    return opcionmenu1

# menu comentarios
def menuComentarios():
    opcion = 0
    while not(opcion>=1 and opcion<=4):
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
        
        
    enteras = input('Si quieres conocer todos los detalles de las peliculas, ingresa "y", si quieres \
volver al menu, ingresa "n": ').lower()

    if enteras == "y":
        if len(peliculas) > 5:
            paginado()
        else:
            system("cls")
            for pelicula in peliculas:
                print(f'{pelicula["nombre"]} con id: {pelicula["peliculaID"]}, genero: {pelicula["generoPeli"]}, del año: {pelicula["anio"]}\
        y su sinopsis es: {pelicula["sinopsis"]}')
                print()
            print()
            input("Enter para continuar...")
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
    input("Enter para continuar...")    

# muestra las peliculas por un director
def pelisDirector():
    system("cls")
    #mostrar los directores disponibles
    directorData = rq.get("http://127.0.0.1:5000/directores")
    directores = directorData.json()
    print("Los directores disponibles son: ")
    print()
    for director in directores:
        print(f'#{director["director"]} con id: {director["idDirector"]}')
        print()
    directorID = input("Ingrese la id del director: ")
    try:
        peliculasDirectorData = rq.get(f"http://127.0.0.1:5000/peliculas/director/{directorID}")
        peliculasDirector = peliculasDirectorData.json()
        system("cls")
        print()
        print("Las peliculas de este director son: ")
        print()
        for peliDirector in peliculasDirector:
            print(f'{peliDirector["nombre"]} con id: {peliDirector["peliculaID"]}, genero: {peliDirector["generoPeli"]}, del año: {peliDirector["anio"]}\
 y su sinopsis es: {peliDirector["sinopsis"]}')
            print()
        input('Enter para continuar...')
    except rq.exceptions.JSONDecodeError:
        system("cls")
        print("=========================================================")
        print("Este director no existe o no tiene peliculas para mostrar")   
        print("=========================================================")      
        input('Enter para continuar...')   

# muestra las peli con portada
def peliPortada():
    system("cls")
    peliPortadaData = rq.get("http://127.0.0.1:5000/peliculas/portada")
    peliPortada = peliPortadaData.json()
    print()
    print("Las peliculas con portada son: ")
    print()
    for peliConPortada in peliPortada:
        print(f'{peliConPortada["nombre"]} con id: {peliConPortada["peliculaID"]}, genero: {peliConPortada["generoPeli"]}, portada: {peliConPortada["portada"]}\
, id del director: {peliConPortada["directorID"]} y del año: {peliConPortada["anio"]}')
        print()
    input('Enter para continuar...')           

#ABM peliculas
def peliAgregar():
    while True:
        system("cls")
        print("-----------------------------------")
        print("Agregar una pelicula! ")
        print("-----------------------------------")
        print()
        nombrePeliAgregar = input("Ingrese el nombre de la pelicula a agregar(x para cancelar): ")
        if nombrePeliAgregar == "x":
            break
        else:
            while nombrePeliAgregar == "" or (len(nombrePeliAgregar)) > 196:
                system ("cls")
                print('=====================')
                print("Esa pelicula no existe, o ingreso un nombre vacio")
                print('=====================')
                nombrePeliAgregar = input("Ingrese el nombre de la pelicula a agregar(x para cancelar): ")
                
            # año de la peli nueva
            system("cls")
            print("-----------------------------------")
            print("Agregar una pelicula! ")
            print("-----------------------------------")
            print()
            anioPeliAgregar = input(f"Ingrese el año de estreno para {nombrePeliAgregar}: ")
            while (len(anioPeliAgregar) != 4):
                system("cls")
                print("=====================")
                print(f'{anioPeliAgregar} no es valido, debe tener 4 numeros. Ej: 2002')
                print("=====================")
                anioPeliAgregar = input(f"Ingrese el año de estreno para {nombrePeliAgregar}: ")
            while True:
                if anioPeliAgregar.isdigit():
                    break
                else:
                    print("===================================================")
                    print('Error, ingrese un número entero válido')
                    print("===================================================")
                    input('Ingrese enter para continuar...')
                    system("cls")
                    anioPeliAgregar = input(f"Ingrese el año de estreno para {nombrePeliAgregar}: ")
            
            
            # genero de la peli nueva
            system("cls")
            print("-----------------------------------")
            print("Agregar una pelicula! ")
            print("-----------------------------------")
            print()
            generosData = rq.get('http://127.0.0.1:5000/generos')
            generos = generosData.json()
            print('Los generos disponibles son:' )
            print()
            for genero in generos:
                print(f'{genero["generoNombre"]}')
            print()
            generoPeliAgregar = input("Que genero quiere?: ")
            # director de la peli nueva
            system("cls")
            print("-----------------------------------")
            print("Agregar una pelicula! ")
            print("-----------------------------------")
            print()
            directoresData = rq.get("http://127.0.0.1:5000/directores")
            directores = directoresData.json()
            print("Los directores disponibles son: ")
            for director in directores:
                print(f'{director["director"]} con id: {director["idDirector"]}')
            print()
            directorPeliAgregar = input("Que director quiere? Escriba el id del director: ")
            # sinopsis de la peli nueva
            system("cls")
            print("-----------------------------------")
            print("Agregar una pelicula! ")
            print("-----------------------------------")
            print()
            sinopsisPeliAgregar = input(f"Ingrese su sinopsis para {nombrePeliAgregar}: ")
            while (sinopsisPeliAgregar == ""):
                system("cls")
                print('=====================')
                print("La sinopsis no puede estar vacía.")
                print('=====================')
                sinopsisPeliAgregar = input(f"Ingrese su sinopsis para {nombrePeliAgregar}: ")
            system("cls")
            print("-----------------------------------")
            print("Agregar una pelicula! ")
            print("-----------------------------------")
            print()   
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
            system("cls")
            print("========================")
            print(response.text)
            print("========================")
            input('Enter para continuar...')
            break
    system("cls")
    print()
    print("Usted a cancelado la accion.")
    input("Enter para continuar...")

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
        print("nombre: "f'{pelicula["nombre"]} con id: {pelicula["peliculaID"]}')
        print()
    
    while True: 
        peliculaID = input('Ingrese el id de la pelicula que quiere borrar(x para salir): ')
        if peliculaID != 'x':
            datos = rq.delete(f'http://127.0.0.1:5000/peliculas/{peliculaID}/usuarioID/{usuarioID}/eliminar')
            mensaje = datos.text
            system("cls")
            print("=============================")
            print(mensaje)
            print("=============================")
            input('Enter para continuar...')
            break
        else:
            system("cls")
            print("============================")
            print('Usted cancelo la eliminacion')
            print("============================")
            input('Enter para continuar...')
            break

def modificar_pelicula():
    opcion_modificar = 0
    system("cls")
    pelisData = rq.get("http://127.0.0.1:5000/pelis")
    peliculas = pelisData.json()
    system("cls")
    print("Las peliculas disponibles son: ")
    print()
    for pelicula in peliculas:
        print(f'#{pelicula["nombre"]} con id: {pelicula["peliculaID"]}')
        print()
    modificar = input('Ingrese la ID de la pelicula que desea modificar: ')
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
                system("cls")
                print('Modificar Pelicula')
                print('1) Titulo')
                print('2) Director')
                print('3) Genero')
                print('4) Año')
                print('5) Portada')
                print('6) Sinopsis')
                print('7) Salir')
                opcion_modificar = int(input('Ingresar opcion: '))
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
                    print("===============")
                    print(mensaje)
                    print("===============")
                    input('Enter para continuar...')
                    system("cls")

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
            opcion = input(' "-" para pagina anterior y "+" para siguiente pagina.("x" para salir): ')
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
            pelicula["puntuacion"] = sum(puntos) / len(pelicula['puntuaciones'])

def puntuar_peli(usuarioID):
    pelisData = rq.get("http://127.0.0.1:5000/pelis")
    peliculas = pelisData.json()
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
                rq.put(f"http://127.0.0.1:5000/peliculas/actualizar", json=peliculas)
                system("cls")
                print("Película puntuada con éxito.")
            else:
                system("cls")
                print("La puntuación ingresada debe ser de 0 a 5.")
            input("Enter para continuar.")
            return
    system("cls")
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
        system("cls")
        buscar = input("Ingrese el título que busca: ")
        for pelicula in pelisData:
            if buscar.lower() in pelicula['nombre'].lower():
                if buscar.lower() in pelicula['nombre'].lower():
                    pelicula["visualizaciones"] = pelicula["visualizaciones"] + 1
                    rq.put(f"http://127.0.0.1:5000/peliculas/actualizar", json=pelisData)
                peliculas_encontradas.append(pelicula)
        if peliculas_encontradas:
            system("cls")
            print(f'Se encontraron {len(peliculas_encontradas)} películas:')
            for peli in peliculas_encontradas:
                print(f'- {peli["nombre"]} (id: {peli["peliculaID"]}), género: {peli["generoPeli"]}, año: {peli["anio"]}, sinopsis: {peli["sinopsis"]}')
        else:
            system("cls")
            print("No se encontraron películas.")
        input("Presione Enter para volver...")
            
    elif opcion == "2":
        system("cls")
        buscar = input("Ingrese el director que busca: ")
        for director in directoresData:
            if buscar.lower() in director['director'].lower():
                directores_encontrados.append(director)
        if directores_encontrados:
            print(f'Se encontraron {len(directores_encontrados)} directores:')
            for director in directores_encontrados:
                print(f'- {director["director"]} (id: {director["idDirector"]})')
        else:
            system("cls")
            print("No se encontraron directores.")
        input("Presione Enter para volver...")
    else:
        system("cls")
        print("Opción no válida")
        input("Presione Enter para continuar...")

#ABM comentarios
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
            system("cls")
            print("=====================")
            print(respuestaFlask)
            print("=====================")
    
    if encontrado == False:
        system("cls")
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
        # Pedir al usuario que ingrese el ID del comentario que desea eliminar
        while True:
            print()
            system("cls")
            print('Sus comentarios son:')
            for comentario in comentariosUsuario:
                print(f"ID: {comentario['comentarioID']}, Comentario: {comentario['comentario']}")
            comenBorrarID = input("Ingrese el ID del comentario que desea eliminar (0 para salir): ")
            if comenBorrarID == '0':
                # Si el usuario ingresa 0, salir de la función
                system("cls")
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
                    system("cls")
                    print("==================================")
                    print(mensaje)
                    print("==================================")
                    input('Ingrese enter para continuar...')
                    system("cls")
                    break
                else:
                    system("cls")
                    print("===================================================")
                    print('Error, ingresó un número que no es suyo o no existe')
                    print("===================================================")
                    input('Ingrese enter para continuar...')
                    system("cls")
            else:
                system("cls")
                print("===================================================")
                print('Error, ingrese un número entero válido')
                print("===================================================")
                input('Ingrese enter para continuar...')
                system("cls")
    else:
        system("cls")
        print("=======================")
        print('No tiene comentarios.')
        print("=======================")
        input('Ingrese enter para continuar...')
        system("cls")

# modificar comentario
def modificarComentario(usuarioID):
    # Obtener los comentarios del usuario
    comentariosUsuarioData = rq.get(f"http://127.0.0.1:5000/comentarios/usuarioID/{usuarioID}")
    comentariosUsuario = comentariosUsuarioData.json()
    
    # Mostrar los comentarios del usuario
    if len(comentariosUsuario) != 0:
        # Pedir al usuario que ingrese el ID del comentario que desea modificar
        while True:
            system("cls")
            print("-------------")
            print("Modificar comentarios")
            print("-------------")
            print('Sus comentarios son:')
            print()
            for comentario in comentariosUsuario:
                print(f"ID: {comentario['comentarioID']}, Comentario: {comentario['comentario']}")
            print()
            comenEditarID = input("Ingrese el ID del comentario que desea modificar (0 para salir): ")
            if comenEditarID == '0':
                # Si el usuario ingresa 0, salir de la función
                print("Usted cancelo la edicion")
                break
            elif comenEditarID.isdigit():
                # Si el usuario ingresa un número entero válido, verificar si existe en la lista de comentarios del usuario
                comentarioEncontrado = False
                for comentario in comentariosUsuario:
                    if comentario['comentarioID'] == comenEditarID:
                        #pedimos el texto nuevo
                        while True:
                            system("cls")
                            comenModificado = input("Ingrese el comentario nuevo: ")
                            system("cls")
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
                    system("cls")
                    print("==================================")
                    print(mensaje)
                    print("==================================")
                    input('Ingrese enter para continuar...')
                    break
                else:
                    system("cls")
                    print("===================================================")
                    print('Error, ingresó un número que no es suyo o no existe')
                    print("===================================================")
                    input('Ingrese enter para continuar...')
                    system("cls")
            else:
                system("cls")
                print("===================================================")
                print('Error, ingrese un número entero válido')
                print("===================================================")
                input('Ingrese enter para continuar...')
                system("cls")
    else:
        system("cls")
        print("=======================")
        print('No tiene comentarios.')
        print("=======================")
        input('Ingrese enter para continuar...')
# termina ABM comentarios

#ABM usuarios
def agregarUsuario():
    system("cls")
    print("--------------------")
    print("Registrar un Usuario")
    print("--------------------")
    while True:
        nombreUsuarioNuevo = input("Ingresa el nombre del nuevo usuario: ")
        contraUsuarioNuevo = input("Ingresa la contraseña del nuevo usuario: ")
        if nombreUsuarioNuevo == "" or contraUsuarioNuevo == "":
            system("cls")
            print("=================================")
            print("No debes dejar ningun campo vacio")
            print("=================================")
            input("Enter para continuar.")
            system("cls")
        else: 
            nuevoUsuario = {f"usuario":nombreUsuarioNuevo,"contrasena":contraUsuarioNuevo,"usuarioID":"","admin":False}
            datos = rq.post('http://127.0.0.1:5000/usuarios/abm', json=nuevoUsuario)
            respuestaFlask = datos.text
            system("cls")
            print("=====================")
            print(respuestaFlask)
            print("=====================")
            input("Enter para continuar.")
            system("cls")
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
        system("cls")
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
                system("cls")
                print("==================================")
                print(mensaje)
                print("==================================")
                input('Ingrese enter para continuar...')
                system("cls")
                break
            else:
                system("cls")
                print("===================================================")
                print('Error, ingresó un número que no existe')
                print("===================================================")
                input('Ingrese enter para continuar...')
                system("cls")
        else:
            system("cls")
            print("===================================================")
            print('Error, ingrese un número entero válido')
            print("===================================================")
            input('Ingrese enter para continuar...')
            system("cls")

def modificarUsuario(usuarioID):
    system("cls")
    print("-------------------")
    print("Modificar un Usuario")
    print("-------------------")
    
    while True:
        #mostrar los directores disponibles
        usuariosData = rq.get("http://127.0.0.1:5000/usuarios")
        usuarios = usuariosData.json()
        print("Los usuarios disponibles son: ")
        print()
        for usuario in usuarios:
            print(f'{usuario["usuario"]} con id: {usuario["usuarioID"]}')
            print()
            
        #pedir id
        idUsuarioModificar = input("Ingresa el id del usuario que deseas modificar(0 para salir): ")
        if idUsuarioModificar == "":
            system("cls")
            print("=================================")
            print("No debes dejar ningun campo vacio")
            print("=================================")
            input("Enter para continuar.")
            system("cls")
        elif idUsuarioModificar == "0":
            system("cls")
            print("========================")
            print("Usted cancelo la accion.")
            print("========================")
            input("Enter para continuar...")
            system("cls")
            break
        elif usuarioID != idUsuarioModificar:
            print("No se puede modificar a otros usuarios, solo a vos mismo")
            input("Enter para continuar... ")
            system("cls")
        else:
            system("cls")
            usuarioNuevo = input("Ingresa el nuevo nombre para el director: ")
            contrasenaNueva = input("Ingresa la nueva contraseña: ")
            usuarioModificado = {"usuario": usuarioNuevo, "contrasena" : contrasenaNueva, "usuarioID":idUsuarioModificar, "admin":""}
            datos = rq.put('http://127.0.0.1:5000/usuarios/modificar', json=usuarioModificado)
            respuestaFlask = datos.text
            system("cls")
            print("=====================")
            print(respuestaFlask)
            print("=====================")
            input("Enter para continuar.")
            system("cls")
            break
    
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
        system("cls")
        print("===================================================")
        print("Solo los administradores pueden hacer admin a un usuario")
        print("===================================================")
        input("Enter para continuar.")
        system("cls")
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
                system("cls")
                print("==================================")
                print(mensaje)
                print("==================================")
                input('Ingrese enter para continuar...')
                system("cls")
                break
            else:
                system("cls")
                print("===================================================")
                print('Error, ingresó un número que no existe')
                print("===================================================")
                input('Ingrese enter para continuar...')
                system("cls")
        else:
            system("cls")
            print("===================================================")
            print('Error, ingrese un número entero válido')
            print("===================================================")
            input('Ingrese enter para continuar...')
            system("cls")

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
        system("cls")
        print("===================================================")
        print("Solo los administradores pueden quitar el admin a un usuario")
        print("===================================================")
        input("Enter para continuar.")
        system("cls")
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
                system("cls")
                print("==================================")
                print(mensaje)
                print("==================================")
                input('Ingrese enter para continuar...')
                system("cls")
                break
            else:
                system("cls")
                print("===================================================")
                print('Error, ingresó un número que no existe')
                print("===================================================")
                input('Ingrese enter para continuar...')
                system("cls")
        else:
            system("cls")
            print("===================================================")
            print('Error, ingrese un número entero válido')
            print("===================================================")
            input('Ingrese enter para continuar...')
            system("cls")
#termina ABM usuarios
def peliculaAleatoria():
    system("cls")
    pelisData = rq.get("http://127.0.0.1:5000/pelis")
    peliculas = pelisData.json()
    peliAleatoria = random.choice(peliculas)
    print("Pelicula Aleatoria: ")
    print(f'{peliAleatoria["nombre"]} con id: {peliAleatoria["peliculaID"]}, genero: {peliAleatoria["generoPeli"]}, del año: {peliAleatoria["anio"]}\
y su sinopsis es: {peliAleatoria["sinopsis"]}')
    input("Enter para continuar...")
    system("cls")

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
    system("cls")   
#ABM directores
def menuDirector():
    system("cls")
    opcionMenuDirector = 0
    while not(opcionMenuDirector>=1 and opcionMenuDirector<=4):
        print("--------------------")
        print("Menu ABM Directores")
        print("--------------------")
        print("1) Agregar un Director")
        print("2) Eliminar un Director")
        print("3) Modificar un director")
        print("4) Salir")
        opcionMenuDirector=int(input("ingresar opcion: "))
        return opcionMenuDirector
    system("cls")

def agregarDirector():
    system("cls")
    print("--------------------")
    print("Registrar un Director")
    print("--------------------")
    while True:
        directorNuevo = input("Ingresa el nombre del nuevo director(0 para salir): ")
        if directorNuevo == "":
            system("cls")
            print("=================================")
            print("No debes dejar ningun campo vacio")
            print("=================================")
            input("Enter para continuar.")
            system("cls")
        elif directorNuevo == 0:
            system("cls")
            print("========================")
            print("Usted cancelo la accion.")
            print("========================")
            input("Enter para continuar...")
            system("cls")
            break
        else: 
            nuevoDirector = {f"director":directorNuevo,"idDirector": "idvacio"}
            datos = rq.post('http://127.0.0.1:5000/director/crear', json=nuevoDirector)
            respuestaFlask = datos.text
            system("cls")
            print("=====================")
            print(respuestaFlask)
            print("=====================")
            input("Enter para continuar.")
            system("cls")
            break

def eliminarDirector():
    system("cls")
    print('=====================')
    print('Eliminar un Director')
    print('=====================')
    directorData = rq.get("http://127.0.0.1:5000/directores")
    directores = directorData.json()
    print("Los directores disponibles son: ")
    print()
    for director in directores:
        print(f'#{director["director"]} con id: {director["idDirector"]}')
        print()
    print()

    while True: 
        exDirectorID = input('Ingrese el id del director que quiere eliminar(x para salir): ')
        if exDirectorID != 'x':
            datos = rq.delete(f'http://127.0.0.1:5000/director/eliminar/{exDirectorID}')
            mensaje = datos.text
            system("cls")
            print("=====================")
            print(mensaje)
            print("=====================")
            input("Enter para continuar.")
        else:
            system("cls")
            print("=============================")
            print('saliendo de eliminar director')
            print("=============================")
            input("Enter para continuar.")
            system("cls")
            break

def modificarDirector():
    system("cls")
    print("-------------------")
    print("Modificar un Director")
    print("-------------------")
    while True:
        #mostrar los directores disponibles
        directorData = rq.get("http://127.0.0.1:5000/directores")
        directores = directorData.json()
        print("Los directores disponibles son: ")
        print()
        for director in directores:
            print(f'#{director["director"]} con id: {director["idDirector"]}')
            print()
            
        #pedir id
        idDirectorModificar = input("Ingresa el id del director que deseas modificar(0 para salir): ")
        if idDirectorModificar == "":
            system("cls")
            print("=================================")
            print("No debes dejar ningun campo vacio")
            print("=================================")
            input("Enter para continuar.")
            system("cls")
        elif idDirectorModificar == "0":
            system("cls")
            print("=========================")
            print("Usted cancelo la accion.")
            print("=========================")
            input("Enter para continuar...")
            system("cls")
            break
        else:
            system("cls")
            directorNuevo = input("Ingresa el nuevo nombre para el director: ")
            directorModificado = {"director": directorNuevo, "idDirector" : idDirectorModificar}
            datos = rq.put('http://127.0.0.1:5000/director/modificar', json=directorModificado)
            respuestaFlask = datos.text
            system("cls")
            print("=====================")
            print(respuestaFlask)
            print("=====================")
            input("Enter para continuar.")
            system("cls")
            break
#ABM generos
def menuGenero():
    system("cls")
    opcionMenuGenero = 0
    while not(opcionMenuGenero>=1 and opcionMenuGenero<=4):
        print("----------------")
        print("Menu ABM Generos")
        print("----------------")
        print("1) Agregar un Genero")
        print("2) Eliminar un Genero")
        print("3) Modificar un Genero")
        print("4) Salir")
        opcionMenuGenero=int(input("ingresar opcion: "))
        return opcionMenuGenero

def agregarGenero():
    system("cls")
    print("-------------------")
    print("Registrar un Genero")
    print("-------------------")
    while True:
        generoNuevo = input("Ingresa el nombre del nuevo genero(0 para salir): ")
        if generoNuevo == "":
            system("cls")
            print("=================================")
            print("No debes dejar ningun campo vacio")
            print("=================================")
            input("Enter para continuar.")
            system("cls")
        elif generoNuevo == 0:
            system("cls")
            print("============================")
            print("saliendo de eliminar genero.")
            print("===========================")
            input("Enter para continuar...")
            system("cls")
            break
        else: 
            nuevoGenero = {"generoNombre":generoNuevo,"idgenero": ""}
            datos = rq.post('http://127.0.0.1:5000/genero/crear', json=nuevoGenero)
            respuestaFlask = datos.text
            system("cls")
            print("=====================")
            print(respuestaFlask)
            print("=====================")
            input("Enter para continuar.")
            system("cls")
            break

def eliminarGenero():
    system("cls")
    print("-------------------")
    print("Eliminar un Genero")
    print("-------------------")
    while True:
        #mostrar generos
        generosData = rq.get('http://127.0.0.1:5000/generos')
        generos = generosData.json()
        print('Los generos disponibles son:' )
        for genero in generos:
            print(f'nombre: {genero["generoNombre"]}'f'e ID: {genero["idgenero"]}')
        generoEliminar = input("Ingresa el id del genero que deseas eliminar(0 para salir): ")
        if generoEliminar == "":
            system("cls")
            print("=================================")
            print("No debes dejar ningun campo vacio")
            print("=================================")
            input("Enter para continuar.")
            system("cls")
        elif generoEliminar == "0":
            system("cls")
            print("========================")
            print("Usted cancelo la accion.")
            print("========================")
            input("Enter para continuar...")
            system("cls")
            break
        else:
            datos = rq.delete(f'http://127.0.0.1:5000/genero/eliminar/{generoEliminar}')
            respuestaFlask = datos.text
            system("cls")
            print("=====================")
            print(respuestaFlask)
            print("=====================")
            input("Enter para continuar.")
            system("cls")
            break

def modificarGenero():
    system("cls")
    print("-------------------")
    print("Modificar un Genero")
    print("-------------------")
    while True:
        #mostrar generos
        generosData = rq.get('http://127.0.0.1:5000/generos')
        generos = generosData.json()
        print('Los generos disponibles son:' )
        for genero in generos:
            print("Nombre: " f'{genero["generoNombre"]} ' "ID: " f'{genero["idgenero"]}')
        print()
        generoModificar = input("Ingresa el id del genero que deseas modificar(0 para salir): ")
        if generoModificar == "":
            system("cls")
            print("=================================")
            print("No debes dejar ningun campo vacio")
            print("=================================")
            input("Enter para continuar.")
            system("cls")
        elif generoModificar == "0":
            system("cls")
            print("=======================")
            print("Usted cancelo la accion.")
            print("=======================")
            input("Enter para continuar...")
            system("cls")
            break
        else:
            print()
            generoNuevo = input("Ingresa el nuevo nombre para el genero: ")
            generoModificado = {"generoNombre": generoNuevo, "idgenero" :generoModificar}
            datos = rq.put(f'http://127.0.0.1:5000/genero/modificar', json=generoModificado)
            respuestaFlask = datos.text
            system("cls")
            print("=====================")
            print(respuestaFlask)
            print("=====================")
            input("Enter para continuar.")
            system("cls")
            break

#menus extras
def menuABMpelis():
    system("cls")
    opcionMenuPelis = 0
    while not(opcionMenuPelis>=1 and opcionMenuPelis<=4):
        print("----------------")
        print("Menu ABM Pelis")
        print("----------------")
        print("1) Agregar una pelicula")
        print("2) Eliminar una pelicula")
        print("3) Modificar una pelicula")
        print("4) Salir")
        opcionMenuPelis=int(input("ingresar opcion: "))
        return opcionMenuPelis

def menuABMusuario():
    system("cls")
    opcionMenuUsuario = 0
    while not(opcionMenuUsuario>=1 and opcionMenuUsuario<=6):
        print("----------------")
        print("Menu ABM Usuario")
        print("----------------")
        print("1) Agregar un usuario")
        print("2) Eliminar un usuario")
        print("3) Modificar un usuario")
        print("4) Dar admin a un usuario")
        print("5) Quitar admin a un usuario")
        print("6) Salir")
        opcionMenuUsuario=int(input("ingresar opcion: "))
        return opcionMenuUsuario