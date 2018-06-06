import re

# Extraer solo palabras dada una cadena. Retornar una lista cuyos contenidos
# corresponden a tales palabras.
def extrWrds(phrase):
    # El patron coincide en cualquier caracter que no sea una letra, un numero,
    # o un guion bajo:
    sep = re.compile(r'\W+')
    
    # Separar la cadena, tomando el patron como un separador de palabras:
    allWrds = re.split(sep, phrase)
    
    # Pueden darse coincidencias al principio de la cadena, luego, se
    # retornarian cadenas vacias, eliminar primero esas cadenas:
    if allWrds[0] == '':
        allWrds.pop(0)
    if allWrds[-1] == '':
        allWrds.pop(-1)
    
    return allWrds

# ------------------------------- Pruebas: ------------------------------------
# match al principio y al final:
str1 = '¿Te has hartado alguna vez de todo? - le dije -'
print(extrWrds(str1))

# Mayusculas, ruptura de linea y caracteres no ASCII:
str2 = '''Muchas veces me imagino que hay un montón de 
niños jugando en un campo de centeno.'''
print(extrWrds(str2))

# Palabras sin sentido, que hacer con ellas?
str3 = 'tegno 22 anios'
print(extrWrds(str3))

# Una palabra sin sentido se convierte en dos palabras con sentido?:
str4 = 'hola carro%feria'
print(extrWrds(str4))


# Extraer palabras sin repeticion, indiferente a mayusculas y minusculas
# 'QUE' == 'que', retornar una lista con esas palabras:
def uniqueWrds(phrase):
    # Copiar toda la cadena con palabras solo en minuscula:
    lowPhrase = phrase.lower()
    
    # Lista con todas las palabras en minuscula:
    lsLowWrds = extrWrds(lowPhrase)
    
    # Extraer solo las palabras sin repeticion:
    uniqueWrds = set(lsLowWrds)
    
    # Construir la lista:
    lsUniqueWrds = [wrd for wrd in uniqueWrds]
    
    return lsUniqueWrds


# Contar palabras dada una cadena que las contiene, la comparacion se hace de
# manera indiferente respecto a mayusculas y minusculas 'QUE' == 'que'. Se re-
# torna un diccionario en donde cada clave es una palabra y cada valor la can-
# tidad de veces que aparece. 
def cntWrds(phrase):
    lowPhrase = phrase.lower()
    
    # Lista con todas las palabras en minuscula:
    lsWrds = extrWrds(lowPhrase)
    
    # Lista con palabras sin repeticion:
    lsUniqueWrds = uniqueWrds(phrase)
    
    # Diccionario tipo (palabra:# ocurrencias):
    wrdCount = {wrd: lsWrds.count(wrd) for wrd in lsUniqueWrds}
    
    return wrdCount

# ------------------------------- Pruebas: ------------------------------------
str5 = 'Ola la ola la cola,ola la Ola'
print(cntWrds(str5))


# Contar la totalidad de palabras en una cadena:
def totalWrds(phrase):
    # Extraer todas las palabras:
    wrds = extrWrds(phrase)
    
    return len(wrds)

# ------------------------------- Pruebas: ------------------------------------
print(totalWrds(str5))


# Contar numero de caracteres por palabra, retornar diccionario con las
# palabras como clave y la cantidad de caracteres como valor (palabra: #chars).
def cntChars(phrase):
    # Extraer palabras sin repeticion:
    lsUniqueWrds = uniqueWrds(phrase)
    
    # Diccionario tipo (palabra: #de caracteres):
    wrdNumchars = {wrd: len(wrd) for wrd in lsUniqueWrds}
    
    return wrdNumchars

# ------------------------------- Pruebas: ------------------------------------
print(str2)
print(cntChars(str2))

