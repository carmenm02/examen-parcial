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
