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