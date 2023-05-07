import funciones as fun
from os import system


opcionMenu1 = 0
while opcionMenu1 != 3:
    opcionMenu1 = fun.menuInicial()
    if opcionMenu1 == 1:
        usuarioID, admin = fun.inicio_de_sesion()
        while True:
            opcion = fun.menuUsuarioResgistrado()
            if opcion == 1:
                fun.mostrarPelis()
            if opcion == 2:
                fun.ultimas10Pelis()
            if opcion == 3:
                fun.pelisDirector()
            if opcion == 4:
                fun.peliPortada()
            if opcion == 5:
                fun.peliAgregar()
            if opcion == 6:
                fun.peliEliminar(usuarioID)
            if opcion == 7:
                fun.modificar_pelicula()
            if opcion == 8:
                opcionComen = fun.menuComentarios()
                if opcionComen == 1:
                    fun.agregarComentario(usuarioID)
                elif opcionComen == 2:
                    fun.eliminarComentario(usuarioID)
                elif opcionComen == 3:
                    fun.modificarComentario(usuarioID)    
            if opcion == 9:
                fun.paginado()
            if opcion == 10:
                fun.puntuar_peli(usuarioID)
            if opcion == 11:
                fun.agregarUsuario()
            if opcion == 12:
                fun.eliminarUsuario(admin)
            if opcion == 13:
                break
    if opcionMenu1 == 2:
        fun.ultimas10Pelis()
        print('Cuando finalice de ver las peliculas, presione "enter" para continuar')
        input()
        break
    
system("cls")
print("Gracias por su visita!")           
