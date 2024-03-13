from termcolor import colored
import random as rand
import time 

#Parametros de la simulacion
tamaño_bosque = 30 #N
d_inicial = 0.6 #Densidad inicial (Di)
t_quemado = 3 #Tiempo que tarda en quemarse un arbol por completo (Tq)
Px = [0,0.2,0.4,0.6,0.8,1,1,1,1] #Probabilidad de que un arbol se prenda fuego dependiendo la cantidad de vecinos que se estan quemando"
t = 0 #Tiempo de la simulacion

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


def cantidades_matriz(matriz, tamaño_bosque):
    arboles_quemados = 0
    arboles_sanos = 0
    arboles_quemandose = 0
    for i in range(tamaño_bosque):
        for j in range(tamaño_bosque):
            if matriz[i][j] > 0:
                arboles_quemandose += 1
            elif matriz[i][j] == 0:
                arboles_quemados += 1
            elif matriz[i][j] == -1:
                arboles_sanos += 1
    return {"arboles_quemados":arboles_quemados, "arboles_sanos":arboles_sanos, "arboles_quemandose":arboles_quemandose}

def cant_arboles_vecinos_quemados(matriz,tamaño_bosque,x,y):
    cant = 0
    for i in range(0,3):
        for j in range(0,3):
            try:
                if matriz[x-1+i][y-1+j] > 0:
                    cant+=1
            except IndexError:
                pass
    return cant

#Inicilizacion de la matriz
matriz = [[-2 for i in range(tamaño_bosque)] for j in range(tamaño_bosque)]
for i in range(tamaño_bosque):
    for j in  range(tamaño_bosque):
        if rand.random() <= d_inicial:
            matriz[i][j] = -1
for i in range(0,3):
    for j in range(0,3):
        matriz[(tamaño_bosque//2)-1+i][(tamaño_bosque//2)-1+j] = t_quemado

#Loop principal de la simulacion
while cantidades_matriz(matriz, tamaño_bosque)["arboles_quemandose"] > 0:
    imprimir_matriz(matriz, tamaño_bosque,t)
    for i in range(tamaño_bosque):
        for j in range(tamaño_bosque):
            if matriz[i][j] > 0:
                matriz[i][j] -= 1
            if matriz[i][j] == -1:
                if rand.random() <= Px[cant_arboles_vecinos_quemados(matriz, tamaño_bosque, i, j)]:
                    #print(colored(Px[cant_arboles_vecinos_quemados(matriz, tamaño_bosque, i, j)],"yellow"))
                    matriz[i][j] = t_quemado
    #time.sleep(60)
    print("- "*(tamaño_bosque))
    t+=1     
imprimir_matriz(matriz, tamaño_bosque,t)
print("Fin de la simulacion")  
