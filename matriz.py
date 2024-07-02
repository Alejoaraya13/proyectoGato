ficha_jugador = "x"

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


def actualizar_matriz(matriz, i, j, ficha_jugador):
    # Ajustar coordenadas para indices de matriz (0 a 2)
    matriz[i-1][j-1] = ficha_jugador
'''
# Ejemplo para ver si sirve
matriz = [
    ["","",""],
    ["","",""],
    ["","",""]
]

# Obtener coordenadas del jugador
i, j = obtener_coordenadas()

# Actualizar la matriz
actualizar_matriz(matriz, i, j, ficha_jugador)

# Imprimir la matriz para verificar la actualizacion
for fila in matriz:
    print(fila)
'''

#En esta funcion se busca las posiciones de todos los simbolos que se quieran encontrar
def encontrarSimbolo(simbolo, matrix):
    posicionesSimbolo = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == simbolo:
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

#Esto es provicional, antes de implementar el sistema de inputs
matrix = [["x","x","x"],["0","0","x"],["x","0","0"]]
print(matrix[0], "\n", matrix[1], "\n", matrix[2])
print("Diga el simbolo que quiere encontrar:")
simbolo = input()

#Se define la variable que nos dice las posiciones del simbolo
posicionesSimbolo = encontrarSimbolo(simbolo, matrix)

#Este if revisa si hay mas de 3 simbolos
if len(posicionesSimbolo) >= 3:
    combinaciones = creacionCombinaciones(posicionesSimbolo)
juegoTerminado = checkJuegoTerminado(combinaciones)

#Basado en la funcion de arriba, si se cumple la condicion el juego termina
if juegoTerminado == True:
    print('El juego ha terminado')
    
