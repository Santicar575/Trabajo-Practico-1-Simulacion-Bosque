import random as rand
import copy

#Parametros de la simulacion
tamaño_bosque = 30 #N
d_inicial = 0.6 #Densidad inicial (Di)
t_quemado = 3 #Tiempo que tarda en quemarse un arbol por completo (Tq)
Px = [0,0.2,0.4,0.6,0.8,1,1,1,1] #Probabilidad de que un arbol se prenda fuego dependiendo la cantidad de vecinos que se estan quemando"
t = 0 #Tiempo de una simulacion
t_total = 0 #Tiempo total de todas las simulaciones
cant_simulaciones = 100 #Cantidad de simulaciones a realizar

#Funciones
def resetear_matriz(matriz,tamaño_bosque):
    for i in range(tamaño_bosque):
        for j in  range(tamaño_bosque):
            if rand.random() <= d_inicial:
                matriz[i][j] = -1
    for i in range(0,3):
        for j in range(0,3):
            matriz[(tamaño_bosque//2)-1+i][(tamaño_bosque//2)-1+j] = t_quemado

def simulacion(matriz_incial,t):
    matriz = copy.deepcopy(matriz_incial)
    arboles_quemados = 9 #cantidades_matriz(matriz, tamaño_bosque)["arboles_quemandose"]
    while arboles_quemados > 0:
        for i in range(tamaño_bosque):
            for j in range(tamaño_bosque):
                if matriz[i][j] > 0:
                    matriz[i][j] -= 1
                    if matriz[i][j] == 0:
                        arboles_quemados -= 1
                if matriz[i][j] == -1:
                    if rand.random() <= Px[cant_arboles_vecinos_quemados(matriz, tamaño_bosque, i, j)]:
                        matriz[i][j] = t_quemado
                        arboles_quemados += 1
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
resetear_matriz(matriz,tamaño_bosque)
matriz_inicial = copy.deepcopy(matriz)

#Loop principal de la simulacion
for i in range(cant_simulaciones):
    t = simulacion(matriz_inicial,t)
    t_total += t
    t = 0
    #resetear_matriz(matriz,tamaño_bosque)
promedio = t_total / cant_simulaciones

print(f"El tiempo promedio que dura un incendio en extinguirse naturalmente luego de {cant_simulaciones} simulaciones es de {promedio} minutos")  
