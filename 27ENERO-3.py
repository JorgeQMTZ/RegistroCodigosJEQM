while True:
    print("Sleccione una de las 3 opciones de a continuacion:")
    print("Opción 1 - comenzar")
    print("Opción 2 - imprimir listado")
    print("Opción 3 - finalizar")
    
    opcion=int(input("Ingrese el numero de la opcion elegida: "))
    
    if opcion==1:
        print("Inicio del programa")
    elif opcion==2:
        print("Listado de equipos de futbol mas destacados:")
        print("Tigres")
        print("Rayados")
        print("America")
        print("Cruz Azul")
        print("Atlas")
    elif opcion==3:
        print("Fin del programa")
        break
    else:
        print("A ocurrido un error")