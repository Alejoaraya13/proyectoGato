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
        elif combinaciones[x][0][1] != combinaciones[x][1][1] != combinaciones[x][2][1] and combinaciones[x][0][0] != combinaciones[x][1][0] != combinaciones[x][2][0]:
            juegoTerminado = True
            break
    return juegoTerminado

juegoTerminado = False

matriz = [
    ["","",""],
    ["","",""],
    ["","",""]
]

print('Bienvenido al juego: ¡Super Gato! Ingrese la ficha que el jugador 1 va a usar. (x/o)')
simbolo = input().lower()

while simbolo != 'x' and simbolo != 'o':
    print('El símbolo que ingresó está incorrecto, inténtelo de nuevo.')
    simbolo = input().lower()

print('Cuál jugador va a jugar primero? (1/2)')
primerJugador = int(input())

while primerJugador != 1 and primerJugador != 2:
    print('El número que ingresó no está correcto, inténtelo de nuevo.')
    primerJugador = int(input())

if primerJugador == 2:
    if simbolo == 'x':
        simbolo = 'o'
    else:
        simbolo = 'x'

#Enseñar matriz al jugador
for fila in matriz:
    print(fila)

while juegoTerminado == False:
    print('Es el turno del jugador:', primerJugador, 'con el símbolo:', simbolo)
    
    # Obtener coordenadas del jugador
    i, j = obtener_coordenadas()

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
    if len(posicionesSimbolo) == 5:
        juegoTerminado == True
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
    if primerJugador == 1:
        primerJugador = 2
    else:
        primerJugador = 1

