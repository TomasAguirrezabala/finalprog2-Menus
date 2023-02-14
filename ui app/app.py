import requests as rq
from os import system

# peliculas = rq.get('http://127.0.0.1:5000/pelis')
# printear = peliculas.json
# print(printear)

generosData = rq.get('http://127.0.0.1:5000/generos')
generos = generosData.json()
for genero in generos:
    print(genero["generoNombre"])

print("---MENU---")
print("opcion 1: que generos hay")
opcionmenu1=int(input("decime 1: "))

if  opcionmenu1 == 1:
    system("cls")
    generosData = rq.get('http://127.0.0.1:5000/generos')
    generos = generosData.json()
    for genero in generos:
        print(f'Los generos disponibles son: {genero["generoNombre"]}')
            