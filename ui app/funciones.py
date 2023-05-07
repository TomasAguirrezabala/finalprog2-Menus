import requests as rq
from os import system
import json



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
    while not(opcionmenu1>=1 and opcionmenu1<=13):
        print("---MENU---")
        print("1) Mostrar las peliculas disponibles.")
        print("2) Mostrar las ultimas diez peliculas agregadas.")
        print("3) Mostrar peliculas de un director.")
        print("4) Mostrar las peliculas con portada.")
        print("5) Agregar una pelicula.")
        print("6) Eliminar una pelicula.")
        print("7) Modificar una pelicula.")
        print("8) ABM Comentarios")
        print("9) Paginado de peliculas")
        print("10) Puntuar pelicula.")
        print("11) Agregar usuario.")   
        print("12) Eliminar usuario.") 
        print("13) Salir.")
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
    system("cls")
    pelisData = rq.get("http://127.0.0.1:5000/pelis")
    peliculas = pelisData.json()
    print("Las peliculas disponibles son: ")
    print()
    for pelicula in peliculas:
        print(f'#{pelicula["nombre"]}')
        print()
    enteras = input('Si quieres conocer todos los detalles de las peliculas, ingresa "y", si quieres \
volver al menu, ingresa "n": ').lower()
    print()
    if enteras == "y":
        for pelicula in peliculas:
            print(f'{pelicula["nombre"]} con id: {pelicula["peliculaID"]}, genero: {pelicula["generoPeli"]}, del año: {pelicula["anio"]}\
 y su sinopsis es: {pelicula["sinopsis"]}')
            print()
        input("Enter para continuar.")
    else:
        input('Enter para continuar...')
    
    
# muestra las ultimas 10 pelis
def ultimas10Pelis():
    system("cls")
    ult_10_pelis_data = rq.get("http://127.0.0.1:5000/ultimas_diez_peliculas")
    ult_10_pelis = ult_10_pelis_data.json()
    for pelicula in ult_10_pelis:
        print(f'{pelicula["nombre"]} con id: {pelicula["peliculaID"]}, genero: {pelicula["generoPeli"]}, del año: {pelicula["anio"]}\
 y su sinopsis es: {pelicula["sinopsis"]}')
        print()
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
    peliAgregar = {"nombre":nombrePeliAgregar, "directorID":directorPeliAgregar, "generoPeli":generoPeliAgregar,\
                "anio":anioPeliAgregar, "peliculaID":" ", "portada":imagenPeliAgregar, "sinopsis":sinopsisPeliAgregar,"comentariosID":[], "puntuacion":"", "puntuaciones":{}}
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
    modificaciones_pelicula = {"nombre": "", "directorID": "", "generoPeli": "", "anio": "", "peliculaID": "", "portada": "", "sinopsis": ""}
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
    listPeliculas = list(peliculas)
    i = 0
    j = 4
    pagina = 1
    opc = ""
    while j < len(peliculas):
        print(f"*pagina {pagina}*")
        for pelicula  in listPeliculas[i:j]:
            print(f'{pelicula["nombre"]} con id: {pelicula["peliculaID"]}, genero: {pelicula["generoPeli"]}, del año: {pelicula["anio"]}\
 y su sinopsis es: {pelicula["sinopsis"]}')
            print("\n")
        opc = input (' "-" para pagina anterior y "+" para siguiente pagina.("x" para salir)')
        if opc == "+":
            pagina = pagina + 1
            i = i + 5
            j = j + 5
        elif opc == "-" and i >= 0:
            pagina = pagina - 1
            i = i - 5
            j = j - 5
        elif opc == "x":
            return 0
        elif opc != "x" and opc != "-" and opc != "+" and opc != "":
            print('solo ingrese "+" o "-".("x" para salir.)')
    while j >= len(peliculas):
        print(f"*pagina {pagina}*")
        for pelicula  in listPeliculas[i:j]:
            print(f'{pelicula["nombre"]} con id: {pelicula["peliculaID"]}, genero: {pelicula["generoPeli"]}, del año: {pelicula["anio"]}\
 y su sinopsis es: {pelicula["sinopsis"]}')
            print("\n")
        opc = input (' "-" para pagina anterior y "+" para siguiente pagina.("x" para salir)')
        if opc == "+":
            pagina = pagina + 1
            i = i + 5
            j = j + 5
        elif opc == "-" and i >= 0:
            pagina = pagina - 1
            i = i - 5
            j = j - 5
        elif opc == "x":
            return 0
        elif opc != "x" and opc != "-" and opc != "+" and opc != "":
            print('solo ingrese "+" o "-".("x" para salir.)')

def promedio_puntuacion(id_Peli, peliculas):
    puntos = []
    for pelicula in peliculas:
        if pelicula["peliculaID"] == id_Peli:
            for key, value in pelicula.items():
                if key == "puntuaciones":
                    for i, p in value.items():
                        puntos.append(p)
            pelicula["puntuacion"] = sum(puntos)

#falta hacer el post
def puntuar_peli(usuarioID):
    pelisData = rq.get("http://127.0.0.1:5000/pelis")
    peliculas = pelisData.json()


    id_Peli = input("ingrese el ID de la pelicula que desea puntuar: ")
    for pelicula in peliculas:
        if pelicula["peliculaID"] == id_Peli:
            puntuacion = int(input("ingrese la puntuacion: "))
            puntuacion_usuario = {usuarioID : puntuacion}
            if usuarioID not in pelicula["puntuaciones"]:
                pelicula["puntuaciones"].update(puntuacion_usuario)
                promedio_puntuacion(id_Peli, peliculas)
                #guardar peliculas en peliculas.json
                # paso a json
                datos = rq.put(f"http://127.0.0.1:5000/peliculas/puntuar", json=peliculas)
                print("Pelicula puntuada con exito.")
                input("Enter para continuar.")
                break
            else:
                print("Usted ya puntuó esta pelicula.")
                input("Enter para continuar.")
                break
        if id_Peli not in peliculas:
            print("error al encontrar la pelicula.")
            input("Enter para volver...")

def buscar_por_Director_Genero(peliculas, buscar):
    pelisData = rq.get("http://127.0.0.1:5000/pelis")
    peliculas = pelisData.json()

    peliculas_encontradas = []
    print("Desea buscar por titulo o por director?")
    print("1) Por titulo.")
    print("2) Por director.")
    opc = input ("Inrese opcion: ")
    if opc == "1":
        buscar = input("Ingrese el titulo que busca: ")
        for pelicula in peliculas:
            if buscar.lower() in pelicula['titulo'].lower():
                peliculas_encontradas.append(pelicula)
        for peli in peliculas_encontradas:
            print(f'{peli["nombre"]} con id: {peli["peliculaID"]}, genero: {peli["generoPeli"]}, del año: {peli["anio"]}\
y su sinopsis es: {peli["sinopsis"]}')
        input("Enter para volver...")

        #hay que importar el json de directores y buscar por ID
#     elif opc == "2":
#         buscar = input("Ingrese el director que busca: ")
#         for pelicula in peliculas:
#             if buscar.lower() in pelicula['directorID'].lower():
#                 peliculas_encontradas.append(pelicula)
#         for peli in peliculas_encontradas:
#             print(f'{peli["nombre"]} con id: {peli["peliculaID"]}, genero: {peli["generoPeli"]}, del año: {peli["anio"]}\
# y su sinopsis es: {peli["sinopsis"]}')
#         input("Enter para volver...")
    else:
        print("Opcion no valida")
        input("Enter para continuar...")



#paginado, funcion para printear por ejemplo 5 o 10 peliculas por pagina. x
#buscador de peliculas o directores. x
#abm usuarios, agregar permiso de admin y usuario publico
#abm generos y directores
#sistema de puntuacion, por usuario logueado. x
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
        for usuario in usuarios:
            print('Los usuarios disponibles son: ')
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
    

            
    
        
    
# empieza abm usuario
# empieza abm usuario
# empieza abm usuario
    

# buscador de películas, actores o directores.
# Implementar ABM de usuarios y capacidad de asignar permisos de administrador o usuario público.
# Implementar ABM de directores y Géneros.


