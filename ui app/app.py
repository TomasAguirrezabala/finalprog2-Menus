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
                fun.buscar_pelicula_o_director()
            if opcion == 10:
                fun.puntuar_peli(usuarioID)
            if opcion == 11:
                fun.agregarUsuario()
            if opcion == 12:
                fun.eliminarUsuario(admin)
            if opcion == 13:
                fun.darAdmin(admin)
            if opcion == 14:
                fun.sacarAdmin(admin)
            if opcion == 15:
                fun.peliculaAleatoria()
            if opcion == 16:
                fun.mostrarVisualizaciones()
            if opcion == 17:
                opcionDirector = fun.menuDirector()
                if opcionDirector == 1:
                    print("Aca se agrega un director")
                elif opcionDirector == 2:
                    print("Aca se elimina un director")
                elif opcionDirector == 3:
                    print("Aca se modifica un director")
            if opcion == 18:
                opcionGenero = fun.menuGenero()
                if opcionGenero == 1:
                    print("Aca se agrega un genero")
                elif opcionGenero == 2:
                    print("Aca se elimina un genero")
                elif opcionGenero == 3:
                    print("Aca se modifica un genero")        
            if opcion == 19:
                break
    if opcionMenu1 == 2:
        fun.ultimas10Pelis()
        print('Cuando finalice de ver las peliculas, presione "enter" para continuar')
        input()
        break
    
system("cls")
print("Gracias por su visita!")           
