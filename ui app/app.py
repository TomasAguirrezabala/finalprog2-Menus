import requests as rq
from os import system
import json
# incio de sesion


# menu usuario
print("---MENU---")
print("opcion 1: que generos hay")
opcionmenu1=int(input("decime 1 o 2: "))
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
    peliAgregar = {"nombre":nombrePeliAgregar, "directorID":directorPeliAgregar, "generoPeli":generoPeliAgregar, "anio":anioPeliAgregar, "peliculaID":" ", "portada":imagenPeliAgregar, "sinopsis":sinopsisPeliAgregar,"comentariosID":""}
    # paso a json
    dataEnviar = json.dumps(peliAgregar)
    # si no aclaras el tipo de contenido no te deja
    encabezado = {'Content-type': 'application/json'}
    # post
    response = rq.post("http://127.0.0.1:5000/peliculas/agregar", data=dataEnviar, headers=encabezado)
    
    print(response.text)
    input('Enter para continuar...')
    
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
    # eliminar una peli
    # Un usuario registado puede eliminar una película sólo si ésta no tiene comentarios de otros usuarios.
    # Un usuario registrado puede editar la información de una película ya cargada, pero no puede borrar ni editar comentarios de otros usuarios.
    # Un usuario no registrado no puede editar ni eliminar películas.
# modificar una peli
       
# menu invitado   
            
elif opcionmenu1 == 10:
    #PRINTEAR ULTIMAS 10 PELIS
    system("cls")
    ult_10_pelis_data = rq.get("http://127.0.0.1:5000//ultimas_diez_peliculas")
    ult_10_pelis = ult_10_pelis_data.json()
    for pelicula in ult_10_pelis:
        for key, value in pelicula.items():
            print(f"{key}: {value}")
        print("\n")