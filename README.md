Este es el enlace de mi repositorio: https://github.com/carmenm02/examen-parcial.git

# examen-parcial
#ejercicio 1
def minion_game(string):
    stuart = 0
    kevin = 0
    vocales = "AEIOU"
    palabra = string.upper()

    for i in range(len(palabra)):
        if palabra[i] not in vocales:
            stuart = stuart + (len(palabra)-i)
        else:
            kevin = kevin + (len(palabra)-i)
    
    if stuart > kevin:
        print("¡Stuart es el ganador con una puntuación de: ", stuart)
    elif kevin > stuart:
        print("Kevin es el ganador con una puntuación de: ", kevin)
    else:
        print("Kevin y Stuart tienen la misma puntuación")

if __name__ == '__main__':
    string = input("La palabra elegida es: ")
    minion_game(string)
    
#ejercicio 2
from random import randint

player1 = 0
player2 = 0
tablero = 0

def funcion(filas, columnas):
    if filas == 0 and tablero[filas + 1][columnas] != " ":
        print("FALLO")
    elif filas == 1 and tablero[filas + 1][columnas] != " ":
        print("FALLO")
    else:
        print("No hay fallos")

def movimientos(filas, columnas):
    if filas == 0:
        tablero[filas+1][columnas] = tablero[filas][columnas]
        tablero[filas][columnas] = ' '
    elif filas == 1:
        if tablero[filas+1][columnas] != ' ':
            tablero[filas-1][columnas] = tablero[filas][columnas]
            tablero[filas][columnas] = ' '
        else:
            tablero[filas+1][columnas] = tablero[filas][columnas]
            tablero[filas][columnas] = ' '
    elif filas == 2:
        tablero[filas-1][columnas] = tablero[filas][columnas]
        tablero[filas][columnas] = ' '

#Voy a crear un while para completar el tablero
while True:
    tablero = [
        [' ', ' ', ' '], 
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]
#Nose como continuar y no me queda tiempo :(
