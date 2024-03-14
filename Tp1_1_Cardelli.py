from termcolor import colored
import random as rand
import copy
from Funciones import *

#Funciones
def imprimir_matriz(matriz, tamaño_bosque, t):
    print(f"Minute: {t}", end="\n")
    for i in range(tamaño_bosque):
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
    print(colored(f"Burning trees: {cantidades_matriz(matriz, tamaño_bosque)['arboles_quemandose']}","red"))
    print(colored(f"Remaining trees: {cantidades_matriz(matriz, tamaño_bosque)['arboles_sanos']}","green"))
    print(colored(f"Burned trees: {cantidades_matriz(matriz, tamaño_bosque)['arboles_quemados']}","white"))

#Inicilizacion de la matriz
matriz = [[-2 for i in range(tamaño_bosque)] for j in range(tamaño_bosque)]
setear_matriz(matriz,tamaño_bosque)

#Loop principal de la simulacion
while cantidades_matriz(matriz, tamaño_bosque)["arboles_quemandose"] > 0:
    imprimir_matriz(matriz, tamaño_bosque,t)
    matriz_paralela = copy.deepcopy(matriz)
    for i in range(tamaño_bosque):
        for j in range(tamaño_bosque):
            if matriz[i][j] > 0:
                matriz_paralela[i][j] -= 1
            if matriz[i][j] == -1:
                if rand.random() <= Px[cant_arboles_vecinos_quemados(matriz, tamaño_bosque, i, j)]:
                    matriz_paralela[i][j] = t_quemado
    print("- "*(tamaño_bosque))
    matriz = matriz_paralela
    t+=1     
imprimir_matriz(matriz, tamaño_bosque,t)
print("Fin de la simulacion")  
