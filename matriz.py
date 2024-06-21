def solicitar_coordenada():
    while True:
        try:
            coord = input("Ingresa la coordenada en formato (i,j):")
            # quitar espacios en blanco y parentesis
            coord = coord.strip().strip("()")
            # Separar por coma, map es un comando que aplica la misma accion a cada elemento en este caso las coordenadas
            # solo convierte las coordenadas en enteros para que la matriz entienda 
            i, j = map(int, coord.split(","))
            return i, j
        except ValueError:
            print("Entrada inválida. Por favor, ingresa la coordenada en el formato correcto (i,j).")

def actualizar_matriz(matriz, i, j, valor):
    # Aqui compara las coordenadas con el largo y ancho de la matriz 
    if 1 <= i <= len(matriz) and 1 <= j <= len(matriz[0]):
        matriz[i-1][j-1] = valor
    #Si no cumple da error y quiero que vuelva a pedir el input, (nada mas que todavia no se como)
    else:
        print("Coordenadas fuera de los límites de la matriz. Por favor, intenta nuevamente.")
#Esto no se si puede servir para mostrar el resultado actualizado de la matriz
'''
def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j])
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
    
