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
# muestra las peliculas
elif opcionmenu1 == 2:
    system("cls")
    pelisData = rq.get("http://127.0.0.1:5000/pelis")
    peliculas = pelisData.json()
    print("Las peliculas disponibles son: ")
    for pelicula in peliculas:
        print(pelicula["nombre"])
# muestra los directores
elif opcionmenu1 == 3:
    system("cls")
    directoresData = rq.get("http://127.0.0.1:5000/directores")
    directores = directoresData.json()
    print("Los directores disponibles son: ")
    for director in directores:
        print(f'{director["director"]} con id: {director["idDirector"]}')
# muestra las peliculas por un director
elif opcionmenu1 == 4:
    system("cls")
    directorID = input("Ingrese la id del director: ")
    peliculasDirectorData = rq.get(f"http://127.0.0.1:5000/peliculas/director/{directorID}")
    peliculasDirector = peliculasDirectorData.json()
    print("Las peliculas de este director son: ")
    for peliDirector in peliculasDirector:
        print(f'{peliDirector["nombre"]} con id: {peliDirector["id"]}, genero: {peliDirector["generoPeli"]} y del año: {peliDirector["anio"]}')
# muestra las peli con portada
elif opcionmenu1 == 5:
    system("cls")
    peliPortadaData = rq.get("http://127.0.0.1:5000/peliculas/portada")
    peliPortada = peliPortadaData.json()
    print("Las peliculas con portada son: ")
    for peliConPortada in peliPortada:
        print(f'{peliConPortada["nombre"]} con id: {peliConPortada["id"]}, genero: {peliConPortada["generoPeli"]}, portada: {peliConPortada["portada"]}\
, id del director: {peliConPortada["directorID"]} y del año: {peliConPortada["anio"]}')
# agregar una peli
elif opcionmenu1 == 6:
    peliculaNueva = []
    nombrePeliAgregar = input("Ingrese el nombre de la pelicula a agregar: ")
    while nombrePeliAgregar == "" or (len(nombrePeliAgregar)) > 196:
        system ("cls")
        print('=====================')
        print("Esa pelicula no existe, o ingreso un nombre vacio")
        print('=====================')
        titulo = input("Ingrese el nombre de la pelicula a agregar: ")
        
    anioPeliAgregar = input(f"Ingrese el año de estreno para {nombrePeliAgregar}: ")
    while (len(anioPeliAgregar) != 4):
        system("cls")
        print("=====================")
        print(f'{anioPeliAgregar} no es valido, debe tener 4 numeros. Ej: 2002')
        print("=====================")
        anioPeliAgregar = input(f"Ingrese el año de estreno para {nombrePeliAgregar}: ")
        
    generosData = rq.get('http://127.0.0.1:5000/generos')
    generos = generosData.json()
    for genero in generos:
        print(f'Los generos disponibles son: {genero["generoNombre"]}')    

    generoPeliAgregar = input("Que genero quiere?: ")
    
    directoresData = rq.get("http://127.0.0.1:5000/directores")
    directores = directoresData.json()
    print("Los directores disponibles son: ")
    for director in directores:
        print(f'{director["director"]} con id: {director["idDirector"]}')
    
    directorPeliAgregar = input("Que director quiere? Escriba el id del director. Ej: 1. : ")
    
    sinopsisPeliAgregar = input(f"Ingrese su sinopsis para {nombrePeliAgregar} ")
    while (sinopsisPeliAgregar == ""):
        system ("cls")
        print('=====================')
        print("La sinopsis no puede estar vacía.")
        print('=====================')
        sinopsisPeliAgregar = input(f"Ingrese su sinopsis para {nombrePeliAgregar}: ")
        
    imagenPeliAgregar = input(f'Ingrese el URL de la imagen para {nombrePeliAgregar}: ')
    peliAgregar = {"nombre":nombrePeliAgregar, "directorID":directorPeliAgregar, "generoPeli":generoPeliAgregar, "anio":anioPeliAgregar, "id":" ", "portada":imagenPeliAgregar, "sinopsis":sinopsisPeliAgregar}
    
    peliAgregar = rq.post('http://127.0.0.1:5000/peliculas/agregar', json=peliAgregar)
    mostrarPeliNueva = peliAgregar.text
    print("=====================")
    print(mostrarPeliNueva)
    print("=====================")
    input('Enter para continuar...')
# eliminar una peli
    # Un usuario registado puede eliminar una película sólo si ésta no tiene comentarios de otros usuarios.
    # Un usuario registrado puede editar la información de una película ya cargada, pero no puede borrar ni editar comentarios de otros usuarios.
    # Un usuario no registrado no puede editar ni eliminar películas.
# modificar una peli
       
# menu invitado   
            
# elif opcionmenu1 == 10:
#     #PRINTEAR ULTIMAS 10 PELIS
#     system("cls")
#     ult_10_Pelis_Data = rq.get("http://127.0.0.1:5000/pelis")
#     ult_10_Pelis = ult_10_Pelis_Data.json()
#     if len(ult_10_Pelis) >= 10:
#         for i in range(-10, 0):
#             pelicula_10 = ult_10_Pelis[i]
#             for key, value in pelicula_10.items():
#                 print(f"{key}: {value}")
#             print("\n")
#     else:
#         print("Hay menos de 10 peliculas agregadas.")
#         print("las ultimas agregadas son:")
#         for pelicula_10 in ult_10_Pelis:
#             for key,value in pelicula_10.items():
#                 print(f"{key}: {value}")
#             print("\n")