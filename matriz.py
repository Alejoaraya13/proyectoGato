import random

#Una lista primero que tenga todas las posibles convinaciones de la matriz y luego las discrimina con base a cuales no tienen simbolo
def coordenada_aleatoria(matriz):
    coordenadas_validas = [(i, j) for i in range(1, 4) for j in range(1, 4) if matriz[i-1][j-1] == ""]
    return random.choice(coordenadas_validas)

def obtener_coordenadas():
    while True:
        try:
            coord = input("Ingresa las coordenadas en formato (i, j): ")
            # Eliminar espacios y parentesis
            coord = coord.strip().strip("()")
            # Convertir a enteros
            i, j = map(int, coord.split(","))
            if 1 <= i <= 3 and 1 <= j <= 3:  # Ver que las coordenadas esten en el rango correcto
                return i, j
            else:
                print("Las coordenadas deben estar en el rango de 1 a 3. Inténtelo de nuevo.")
        except ValueError:
            print("La entrada es invalida. Debe ingresar las coordenadas en el formato correcto (i, j). Inténtelo de nuevo.")

# Función para verificar si una coordenada está libre y obtener coordenadas válidas
def obtener_coordenadas_validas(matriz):
    while True:
        i, j = obtener_coordenadas()
        if matriz[i-1][j-1] == "":  # Verifica si la coordenada está libre
            return i, j
        else:
            print("Esa coordenada está ocupada. Inténtalo de nuevo.")
            
def actualizar_matriz(matriz, i, j, simbolo):
    # Ajustar coordenadas para indices de matriz (0 a 2)
    matriz[i-1][j-1] = simbolo

#En esta funcion se busca las posiciones de todos los simbolos que se quieran encontrar
def encontrarSimbolo(simbolo, matriz):
    posicionesSimbolo = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == simbolo:
                posicionesSimbolo.append((i,j))
    return posicionesSimbolo

#En esta se combinan en grupos de 3 todas las posiciones previamente encontradas
def creacionCombinaciones(posicionesSimbolo):
    combinaciones = []
    for x in range(len(posicionesSimbolo)):
        for y in range(x + 1, len(posicionesSimbolo)):
            for z in range(y + 1, len(posicionesSimbolo)):
                combinacionesTres = (posicionesSimbolo[x], posicionesSimbolo[y], posicionesSimbolo[z])
                combinaciones.append(combinacionesTres)
    return combinaciones

#En esta se checkea si dentro de las combinaciones de tres hay simbolos en la misma fila, columna o en diagonal
def checkJuegoTerminado(combinaciones):
    juegoTerminado = False
    for x in range(len(combinaciones)):
        if combinaciones[x][0][0] == combinaciones[x][1][0] == combinaciones[x][2][0]:
            juegoTerminado = True
            break
        elif combinaciones[x][0][1] == combinaciones[x][1][1] == combinaciones[x][2][1]:
            juegoTerminado = True
            break
        elif combinaciones[x][0][1] != combinaciones[x][1][1] and combinaciones[x][0][1] != combinaciones[x][2][1] and combinaciones[x][2][1] != combinaciones[x][1][1] and combinaciones[x][0][0] != combinaciones[x][1][0] and combinaciones[x][0][0] != combinaciones[x][2][0] and combinaciones[x][1][0] != combinaciones[x][2][0]:
            for y in range(3):
                if combinaciones[x][y] == (1,0) or combinaciones[x][y] == (1,2):
                    juegoTerminado = False
                    break
                else:
                    juegoTerminado = True
            break
    return juegoTerminado

#Variables importantes para el el juego
juegoTerminado = False

matriz = [
    ["","",""],
    ["","",""],
    ["","",""]
]

#Pregunta inicial, selección de modos de juego
print('Bienvenid@ al juego: ¡Súper Gato! ¿Cuántos jugadores van a jugar? (1/2)')
modoDeJuego = input()

#Checkea que el input del modo de juego sea correcto
while modoDeJuego != '1' and modoDeJuego != '2':
    print('El modo de juego que ingresó es incorrecto, inténtelo de nuevo.')
    modoDeJuego = input()

#Modo de 2 jugadores
if modoDeJuego == '2':
    #Selección del simbolo del jugador 1
    print('Ingrese el símbolo que el jugador 1 va a usar. (x/o)')
    simbolo = input().lower()

    #Checkea que el simbolo escrito sea correcto
    while simbolo != 'x' and simbolo != 'o':
        print('El símbolo que ingresó es incorrecto, inténtelo de nuevo.')
        simbolo = input().lower()

    #Selección del jugador que va a ir primero
    print('¿Cuál jugador va a jugar primero? (1/2)')
    primerJugador = input()

    #Checkea si el input sea válido
    while primerJugador != '1' and primerJugador != '2':
        print('El número que ingresó es icorrecto, inténtelo de nuevo.')
        primerJugador = int(input())

    #Cambia la ficha que se está jugando
    if primerJugador == '2':
        if simbolo == 'x':
            simbolo = 'o'
        else:
            simbolo = 'x'

    #Enseñar matriz al jugador
    for fila in matriz:
        print(fila)

    #Main loop del modo 2 jugadores
    while juegoTerminado == False:
        print('Es el turno del jugador:', primerJugador, 'con el símbolo:', simbolo)
        
        # Obtener coordenadas del jugador
        i, j = obtener_coordenadas_validas(matriz)

        # Actualizar la matriz
        actualizar_matriz(matriz, i, j, simbolo)

        #Se define la variable que nos dice las posiciones del simbolo
        posicionesSimbolo = encontrarSimbolo(simbolo, matriz)


        #Este if revisa si hay mas de 3 simbolos
        #Si se cumple la condicion el juego termina
        if len(posicionesSimbolo) >= 3:
            combinaciones = creacionCombinaciones(posicionesSimbolo)
            juegoTerminado = checkJuegoTerminado(combinaciones)
            if juegoTerminado == True:
                print('El juego ha terminado, el ganador es:', simbolo)

        #Checkea si ya no hay mas posiciones disponibles en el tablero
        if len(posicionesSimbolo) == 5 and juegoTerminado == False:
            juegoTerminado = True
            print('No hay más movimientos disponibles')
        
        #Printea la fila resultante
        print('El resultado de su movimiento es:')
        for fila in matriz:
            print(fila)
        
        #Cambia el simbolo que se va a poner
        if simbolo == 'x':
            simbolo = 'o'
        else:
            simbolo = 'x'
        
        #Cambia el jugador
        if primerJugador == '1':
            primerJugador = '2'
        else:
            primerJugador = '1'

#Modo de juego contra computadora
else:
    #Selección del simbolo del jugador
    print('Ingrese el símbolo que el jugador va a usar. (x/o)')
    simbolo = input().lower()

    #Checkea que el símbolo escrito sea correcto
    while simbolo != 'x' and simbolo != 'o':
        print('El símbolo que ingresó es incorrecto, inténtelo de nuevo.')
        simbolo = input().lower()
        
    #Enseñar matriz al jugador
    for fila in matriz:
        print(fila)
        
    #El primer jugador es el Jugador xd
    jugadorActual = 'Jugador'

    #Main loop del modo de juego contra la computadora
    while juegoTerminado == False:
        print('Es el turno de', jugadorActual, 'con el símbolo:', simbolo)
      
        #Turno del Jugador
        if jugadorActual == 'Jugador':
            # Obtener coordenadas del jugador
            i, j = obtener_coordenadas_validas(matriz)

            # Actualizar la matriz
            actualizar_matriz(matriz, i, j, simbolo)

            #Se define la variable que nos dice las posiciones del simbolo
            posicionesSimbolo = encontrarSimbolo(simbolo, matriz)

            #Este if revisa si hay mas de 3 simbolos
            #Si se cumple la condicion el juego termina
            if len(posicionesSimbolo) >= 3:
                combinaciones = creacionCombinaciones(posicionesSimbolo)
                juegoTerminado = checkJuegoTerminado(combinaciones)
                if juegoTerminado == True:
                    print('El juego ha terminado. ¡Has ganado!')

            #Checkea si ya no hay mas posiciones disponibles en el tablero
            if len(posicionesSimbolo) == 5 and juegoTerminado == False:
                juegoTerminado = True
                print('No hay más movimientos disponibles')
            
            #Printea la fila resultante
            print('El resultado de su movimiento es:')
            for fila in matriz:
                print(fila)
 
        #Turno de la computadora  
        else:
            #Este es para que vean el resultado de su movimiento!
            print('¿Desea continuar? (sí)')
            esperaComputador = input().lower()
            
            #Verificar si su respuesta es correcta
            while esperaComputador != 'si' and esperaComputador != 'sí':
                print('Su respuesta es incorrecta, ingrese de nuevo su respuesta.')
                esperaComputador = input()
            
            #Seleccion de cordenadas para la computadora
            i, j = coordenada_aleatoria(matriz)      

            # Actualizar la matriz
            actualizar_matriz(matriz, i, j, simbolo)
            
            #Este if revisa si hay mas de 3 simbolos
            #Si se cumple la condicion el juego termina
            if len(posicionesSimbolo) >= 3:
                combinaciones = creacionCombinaciones(posicionesSimbolo)
                juegoTerminado = checkJuegoTerminado(combinaciones)
                if juegoTerminado == True:
                    print('El juego ha terminado. ¡Ha ganado la computadora¡')

            #Checkea si ya no hay mas posiciones disponibles en el tablero
            if len(posicionesSimbolo) == 5 and juegoTerminado == False:
                juegoTerminado = True
                print('No hay más movimientos disponibles')
            
            #Printea la fila resultante
            print('El resultado del movimiento de la computadora es:')
            for fila in matriz:
                print(fila)
                
        
        #Cambia el simbolo que se va a poner
        if simbolo == 'x':
            simbolo = 'o'
        else:
            simbolo = 'x'
        
        #Cambia el jugador
        if jugadorActual == 'Jugador':
            jugadorActual = 'Computadora'
        else:
            jugadorActual = 'Jugador'
        
        


