import random as rand
import copy
from Tp1_Funciones_Cardelli import *

#Parametros
tamaño_bosque = 30 #N
d_inicial = 0.6 #Densidad inicial (Di)
t_quemado = 3 #Tiempo que tarda en quemarse un arbol por completo (Tq)
Px = [0,0.2,0.4,0.6,0.8,1,1,1,1] #Probabilidad de que un arbol se prenda fuego dependiendo la cantidad de vecinos que se estan quemando"
t = 0 #Tiempo de una simulacion

#Inicilizacion de la matriz
matriz = [[-2 for _ in range(tamaño_bosque)] for _ in range(tamaño_bosque)] #Creo una matriz llena de -2 (celdas vacias)
setear_matriz(matriz,tamaño_bosque,d_inicial,t_quemado) #Se setea la matriz

#Loop principal de la simulacion
while cantidades_matriz(matriz, tamaño_bosque)["arboles_quemandose"] > 0: #Recorre toda la matriz hasta que no hallan arboles quemados
    imprimir_matriz(matriz, tamaño_bosque,t)
    matriz_paralela = copy.deepcopy(matriz) #Se crea una matriz paralela en un diferente espacio en memoria para ir aplicando los cambios
    for i in range(tamaño_bosque):
        for j in range(tamaño_bosque):
            if matriz[i][j] > 0: #Si en la posicion hay un arbol quemado se le resta un minuto al tiempo que tarda en quemarse
                matriz_paralela[i][j] -= 1
            if matriz[i][j] == -1:
                #Si en la posicion hay un arbol, se elije la probabilidad que tiene de quemarse dependiendo de la cantidad de arboles quemandose vecinos que tenga
                if rand.random() <= Px[cant_arboles_vecinos_quemados(matriz, tamaño_bosque, i, j)]:
                    matriz_paralela[i][j] = t_quemado
    print("- "*(tamaño_bosque))
    matriz = matriz_paralela #Se cambia la matriz por la matriz paralela con los cambios aplicados
    t+=1     
imprimir_matriz(matriz, tamaño_bosque,t)
print("Fin de la simulacion")  
