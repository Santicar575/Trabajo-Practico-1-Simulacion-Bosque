import random as rand
import copy

#Parametros
tamaño_bosque = 30 #N
d_inicial = 0.6 #Densidad inicial (Di)
t_quemado = 3 #Tiempo que tarda en quemarse un arbol por completo (Tq)
Px = [0,0.2,0.4,0.6,0.8,1,1,1,1] #Probabilidad de que un arbol se prenda fuego dependiendo la cantidad de vecinos que se estan quemando"
t = 0 #Tiempo de una simulacion
t_total = 0 #Tiempo total de todas las simulaciones
cant_simulaciones = 100 #Cantidad de simulaciones a realizar

def setear_matriz(matriz,tamaño_bosque):
    for i in range(tamaño_bosque):
        for j in  range(tamaño_bosque):
            if rand.random() <= d_inicial:
                matriz[i][j] = -1
    for i in range(0,3):
        for j in range(0,3):
            matriz[(tamaño_bosque//2)-1+i][(tamaño_bosque//2)-1+j] = t_quemado

def simulacion(matriz):
    #matriz = copy.deepcopy(matriz_inicial)
    t = 0
    arboles_quemados = 9 #cantidades_matriz(matriz, tamaño_bosque)["arboles_quemandose"]
    while arboles_quemados > 0:
        matriz_paralela = copy.deepcopy(matriz)
        for i in range(tamaño_bosque):
            for j in range(tamaño_bosque):
                if matriz[i][j] > 0: 
                    matriz_paralela[i][j] -= 1
                    if matriz_paralela[i][j] == 0:
                        arboles_quemados -= 1
                if matriz[i][j] == -1:
                    if rand.random() <= Px[cant_arboles_vecinos_quemados(matriz, tamaño_bosque, i, j)]:
                        matriz_paralela[i][j] = t_quemado
                        arboles_quemados += 1
        matriz = matriz_paralela
        t+=1
    return t

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
    for i in range(3):
        for j in range(3):
            if (x-1+i >= 0 and x-1+i < tamaño_bosque and y-1+j >= 0 and y-1+j < tamaño_bosque):
                if matriz[x-1+i][y-1+j] > 0:
                    cant+=1
    return cant