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

if  opcionmenu1 == 1:
    system("cls")
    generosData = rq.get('http://127.0.0.1:5000/generos')
    generos = generosData.json()
    for genero in generos:
        print(f'Los generos disponibles son: {genero["generoNombre"]}')
elif opcionmenu1 == 2:
    system("cls")
    pelisData = rq.get("http://127.0.0.1:5000/pelis")
    peliculas = pelisData.json()
    print("Las peliculas disponibles son: ")
    for pelicula in peliculas:
        print(pelicula["nombre"])
elif opcionmenu1 == 3:
    system("cls")
    directoresData = rq.get("http://127.0.0.1:5000/directores")
    directores = directoresData.json()
    print("Los directores disponibles son: ")
    for director in directores:
        print(directores)       
        

            