import requests as rq
from os import system
import json

# incio de sesion
def inicio_de_sesion():
    system('cls')
    while True:
        usuariosData = rq.get("http://127.0.0.1:5000/usuarios")
        usuarios = usuariosData.json()
        print('*Iniciar sesión*')
        input_usuario = input('Ingrese su usuario: ')
        input_contrasena = input('Ingrese su contraseña: ')
        for usuario in usuarios:
            if usuario['usuario'] == input_usuario and usuario['contrasena'] == input_contrasena:
                print('.Sesion iniciada con exito.')
                return 0
            else:
                print('Usuario y/o contraseña incorrecta.')
                continue    


def modificar_pelicula():
    opcion_modificar = 0
    while not(opcion_modificar>=1 and opcion_modificar<=7): 
        print('*Modificar Pelicula')
        print('1) Titulo')
        print('2) Director')
        print('3) Genero')
        print('4) Año')
        print('5) Portada')
        print('6) Sinopsis')
        print('7) Terminar/Salir')
        opcion_modificar = int(input('Ingresar opcion: '))
    return opcion_modificar

#ACOMODAR el inicio de sesion en un mejor lugar
inicio_de_sesion()

# menu usuario
print("---MENU---")
print("1) Mostrar generos disponibles.")
print("2) Mostrar peliculas disponibles.")
print("3) Mostrar los directores cargados.")
print("4) Mostrar peliculas de un director.")
print("5) Mostrar las peliculas por portada.")
print("6) Agregar una pelicula.")
print("7) Eliminar una pelicula.")
print("8) Modificar una pelicula.")
print("9) Mostrar las ultimas diez peliculas agregadas.")
opcionmenu1=int(input("ingresar opcion: "))
# muestra los generos
if  opcionmenu1 == 1:
    system("cls")
    generosData = rq.get('http://127.0.0.1:5000/generos')
    generos = generosData.json()
    for genero in generos:
        print(f'Los generos disponibles son: {genero["generoNombre"]}')
    input('Enter para continuar...')
# muestra las peliculas
elif opcionmenu1 == 2:
    system("cls")
    pelisData = rq.get("http://127.0.0.1:5000/pelis")
    peliculas = pelisData.json()
    print("Las peliculas disponibles son: ")
    for pelicula in peliculas:
        print(pelicula["nombre"])
    input('Enter para continuar...')
# muestra los directores
elif opcionmenu1 == 3:
    system("cls")
    directoresData = rq.get("http://127.0.0.1:5000/directores")
    directores = directoresData.json()
    print("Los directores disponibles son: ")
    for director in directores:
        print(f'{director["director"]} con id: {director["idDirector"]}')
    input('Enter para continuar...')
# muestra las peliculas por un director
elif opcionmenu1 == 4:
    system("cls")
    directorID = input("Ingrese la id del director: ")
    peliculasDirectorData = rq.get(f"http://127.0.0.1:5000/peliculas/director/{directorID}")
    peliculasDirector = peliculasDirectorData.json()
    print("Las peliculas de este director son: ")
    for peliDirector in peliculasDirector:
        print(f'{peliDirector["nombre"]} con id: {peliDirector["id"]}, genero: {peliDirector["generoPeli"]} y del año: {peliDirector["anio"]}')
    input('Enter para continuar...')
# muestra las peli con portada
elif opcionmenu1 == 5:
    system("cls")
    peliPortadaData = rq.get("http://127.0.0.1:5000/peliculas/portada")
    peliPortada = peliPortadaData.json()
    print("Las peliculas con portada son: ")
    for peliConPortada in peliPortada:
        print(f'{peliConPortada["nombre"]} con id: {peliConPortada["id"]}, genero: {peliConPortada["generoPeli"]}, portada: {peliConPortada["portada"]}\
, id del director: {peliConPortada["directorID"]} y del año: {peliConPortada["anio"]}')
    input('Enter para continuar...')
# agregar una peli
elif opcionmenu1 == 6:
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
                "anio":anioPeliAgregar, "peliculaID":" ", "portada":imagenPeliAgregar, "sinopsis":sinopsisPeliAgregar,"comentariosID":"0"}
    # paso a json
    dataEnviar = json.dumps(peliAgregar)
    # si no aclaras el tipo de contenido no te deja
    encabezado = {'Content-type': 'application/json'}
    # post
    response = rq.post("http://127.0.0.1:5000/peliculas/agregar", data=dataEnviar, headers=encabezado)
    
    print(response.text)
    input('Enter para continuar...')
# eliminar una peli    
elif opcionmenu1 == 7:
    system("cls")
    print('=====================')
    print('Borrar una pelicula')
    print('=====================')
    usuarioID = input("ingrese el id de su usuario: ")
    while int(usuarioID) < 4:   
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
    else:
        print("Ese usuario no existe")
        input('Ingrese enter para continuar...')
#editar una pelicula a partir de su ID
    # Un usuario registrado puede editar la información de una película ya cargada, pero no puede borrar ni editar comentarios de otros usuarios.
elif opcionmenu1 == 8:
    opcion_modificar = 0
    encontrar = False

    modificar = int(input('Ingrese la ID de la pelicula que desea modificar:'))
    #peli vacia donde guarda cada cambio para poder hacer mas de 1 cambio antes de enviar los datos
    modificaciones_pelicula = {"nombre": "", "directorID": "", "generoPeli": "", "anio": "", "id": "", "portada": "", "sinopsis": ""}
    data = rq.get('http://127.0.0.1:5000/pelis')
    peliculas = data.json()
    for pelicula in peliculas:
        if pelicula["id"] == modificar:
            encontrar = True
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
                    modificaciones_pelicula["id"] = modificar
                    datos = rq.put(f'http://127.0.0.1:5000/peliculas/modif/', json=modificaciones_pelicula)
                    mensaje = datos.text
                    print("*")
                    print(mensaje)
                    print("*")
                    input('Enter para continuar...')
#muestra las ultimas 10 peliculas agregadas
elif opcionmenu1 == 9:
    #PRINTEAR ULTIMAS 10 PELIS
    system("cls")
    ult_10_pelis_data = rq.get("http://127.0.0.1:5000/ultimas_diez_peliculas")
    ult_10_pelis = ult_10_pelis_data.json()
    for pelicula in ult_10_pelis:
        for key, value in pelicula.items():
            print(f"{key}: {value}")
        print("\n")


#paginado, funcion para printear por ejemplo 5 o 10 peliculas por pagina.
#buscador de peliculas, directores.
#abm usuarios, agregar permiso de admin y usuario publico
#abm generos y directores
#sistema de puntuacion, por usuario logueado


