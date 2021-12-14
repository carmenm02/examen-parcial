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