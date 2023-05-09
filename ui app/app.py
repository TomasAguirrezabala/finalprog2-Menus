import funciones as fun
from os import system


opcionMenu1 = 0
while opcionMenu1 != 3:
    opcionMenu1 = fun.menuInicial()
    if opcionMenu1 == 1:
        usuarioID,admin = fun.inicio_de_sesion()
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
                opcionPelis = fun.menuABMpelis()
                if opcionPelis == 1:
                    fun.peliAgregar()
                elif opcionPelis == 2:
                    fun.peliEliminar(usuarioID)
                elif opcionPelis == 3:
                    fun.modificar_pelicula()
            if opcion == 6:
                opcionComen = fun.menuComentarios()
                if opcionComen == 1:
                    fun.agregarComentario(usuarioID)
                elif opcionComen == 2:
                    fun.eliminarComentario(usuarioID)
                elif opcionComen == 3:
                    fun.modificarComentario(usuarioID)   
            if opcion == 7:
                fun.buscar_pelicula_o_director()
            if opcion == 8:
                fun.puntuar_peli(usuarioID)
            if opcion == 9:
                opcionUsuario = fun.menuABMusuario()
                if opcionUsuario == 1:
                    fun.agregarUsuario()
                elif opcionUsuario == 2:
                    fun.eliminarUsuario(admin)
                elif opcionUsuario == 3:
                    fun.modificarUsuario(usuarioID)
                elif opcionUsuario == 4:
                    fun.darAdmin(admin)
                elif opcionUsuario == 5:
                    fun.sacarAdmin(admin)
            if opcion == 10:
                fun.peliculaAleatoria()
            if opcion == 11:
                fun.mostrarVisualizaciones()
            if opcion == 12:
                opcionDirector = fun.menuDirector()
                if opcionDirector == 1:
                    fun.agregarDirector()
                elif opcionDirector == 2:
                    fun.eliminarDirector()
                elif opcionDirector == 3:
                    fun.modificarDirector()
            if opcion == 13:
                opcionGenero = fun.menuGenero()
                if opcionGenero == 1:
                    fun.agregarGenero()
                elif opcionGenero == 2:
                    fun.eliminarGenero()
                elif opcionGenero == 3:
                    fun.modificarGenero()      
            if opcion == 14:
                break
    if opcionMenu1 == 2:
        fun.ultimas10Pelis()
        break
    
system("cls")
print("Gracias por su visita!")           
