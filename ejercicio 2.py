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
