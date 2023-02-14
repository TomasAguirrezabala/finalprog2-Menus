import requests as rq
from os import system

# peliculas = rq.get('http://127.0.0.1:5000/pelis')
# printear = peliculas.json
# print(printear)

# generosData = rq.get('http://127.0.0.1:5000/generos')
# generos = generosData.json()
# for genero in generos:
#     print(genero["generoNombre"])

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
# # # elif opcionmenu1 == 4:
# # #     system("cls")
# # #     peliculasDirectorData = rq.get("http://127.0.0.1:5000/peliculas/director/{directorID}")
# # #     peliculasDirector = peliculasDirectorData.json()
# # #     print("Las peliculas de este director son: ")
# # #     print(peliculasDirector)
            
        

            