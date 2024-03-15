import random as rand
from termcolor import colored
import copy

#Funciones
def imprimir_matriz(matriz, tamaño_bosque, t):
    """ Imprime la matriz del bosque con el formato y colores necesarios """
    print(f"Minute: {t}", end="\n")
    for i in range(tamaño_bosque): #Recorre toda la matriz e imprime "▓▓" verde cuando hay un -1 (arbol), un "▓▓" blanco cuando hay un o (arbol quemado), un "▓▓" rojo cuando hay un numero mayor 0 (arbol quemandose) o dos espacios vacios si hay un -2.
        for j in  range(tamaño_bosque):
            if matriz[i][j] == -2:
                print("  ", end = "")
            elif matriz[i][j] == -1:
                print(colored("▓▓", "green"), end = "")
            elif matriz[i][j] == 0:
                print(colored("▓▓", "white"), end = "")
            elif matriz[i][j] > 0:
                print(colored("▓▓", "red"), end = "")
        print("")
    #Se imprimen las cantidades de cada tipo de arbol
    print(colored(f"Burning trees: {cantidades_matriz(matriz, tamaño_bosque)['arboles_quemandose']}","red"))
    print(colored(f"Remaining trees: {cantidades_matriz(matriz, tamaño_bosque)['arboles_sanos']}","green"))
    print(colored(f"Burned trees: {cantidades_matriz(matriz, tamaño_bosque)['arboles_quemados']}","white"))

def setear_matriz(matriz,tamaño_bosque,d_inicial,t_quemado):
    """ Llena la matriz de arboles (dependiendo de la densidad) y llena las 9 casillas centrales con arboles quemandose """
    #Se recorre toda la matriz y por cada posicion, dependiendo de la densidad, se cambia por un -1 (arbol)
    for i in range(tamaño_bosque):
        for j in  range(tamaño_bosque):
            if rand.random() <= d_inicial:
                matriz[i][j] = -1
    #Se cambian las 9 casillas centrales de la matriz por arboles quemandose
    for i in range(-1,2):
        for j in range(-1,2):
            matriz[(tamaño_bosque//2)+i][(tamaño_bosque//2)+j] = t_quemado

def simulacion(matriz,tamaño_bosque,t_quemado,Px):
    """ Simula el incendio del bosque hasta que no queden mas arboles quemandose """
    t = 0
    arboles_quemandose = 9 #Siempre se empieza con 9 arboles quemados
    while arboles_quemandose > 0: #Recorre toda la matriz hasta que no hallan arboles quemados
        matriz_paralela = copy.deepcopy(matriz) #Se crea una matriz paralela en un diferente espacio en memoria para ir aplicando los cambios
        for i in range(tamaño_bosque):
            for j in range(tamaño_bosque):
                if matriz[i][j] > 0: #Si en la posicion hay un arbol quemado se le resta un minuto al tiempo que tarda en quemarse
                    matriz_paralela[i][j] -= 1
                    if matriz_paralela[i][j] == 0: #Si el arbol se termina de quemar (llega a 0) se le resta uno a la cantidad de arboles quemandose
                        arboles_quemandose -= 1
                if matriz[i][j] == -1:
                    #Si en la posicion hay un arbol, se elije la probabilidad que tiene de quemarse dependiendo de la cantidad de arboles quemandose vecinos que tenga
                    if rand.random() <= Px[cant_arboles_vecinos_quemados(matriz, tamaño_bosque, i, j)]:
                        matriz_paralela[i][j] = t_quemado
                        arboles_quemandose += 1
        matriz = matriz_paralela #Se cambia la matriz por la matriz paralela con los cambios aplicados
        t+=1
    return t, matriz

def cantidades_matriz(matriz, tamaño_bosque):
    """ Recorre la matriz y devuelve un diccionario con las cantidades de cada tipo de arbol (arboles_quemados , arboles_sanos y arboles_quemandose) """
    arboles_quemados = 0
    arboles_sanos = 0
    arboles_quemandose = 0
    #Se recorre la matriz y se aumentan las cantidades de cada variable dependiendo el numero que haya en la posicion   
    for i in range(tamaño_bosque):
        for j in range(tamaño_bosque):
            if matriz[i][j] > 0:
                arboles_quemandose += 1
            elif matriz[i][j] == 0:
                arboles_quemados += 1
            elif matriz[i][j] == -1:
                arboles_sanos += 1
    #Se devuelven las cantidades en un diccionario
    return {"arboles_quemados":arboles_quemados, "arboles_sanos":arboles_sanos, "arboles_quemandose":arboles_quemandose}

def cant_arboles_vecinos_quemados(matriz,tamaño_bosque,x,y):
    """ Toma una posicion de la matriz y devuelve la cantidad de arboles vecinos que se estan prendiendo fuego """
    cant = 0
    #Recorre las casillas de alrededor de la posicion a analizar
    for i in range(-1,2):
        for j in range(-1,2):
            #El if asegura que no se produzca un error si se intenta analizar una posicion de la primera o ultima fila o columna
            if ((x+i >= 0) and (x+i < tamaño_bosque) and (y+j >= 0) and (y+j < tamaño_bosque)):
                if matriz[x+i][y+j] > 0: #Si en la posicion hay un arbol quemandose (un numero mayor a 0), se aumenta en uno la cantidad
                    cant+=1
    return cant