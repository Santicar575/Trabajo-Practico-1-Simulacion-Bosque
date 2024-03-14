import random as rand
import copy
from Funciones import *

#Inicilizacion de la matriz
matriz = [[-2 for i in range(tamaño_bosque)] for j in range(tamaño_bosque)]
setear_matriz(matriz,tamaño_bosque)
matriz_inicial = copy.deepcopy(matriz)

#Loop principal de la simulacion
for i in range(cant_simulaciones):
    t = simulacion(matriz)
    t_total += t
    t = 0
    matriz = copy.deepcopy(matriz_inicial)
    #resetear_matriz(matriz,tamaño_bosque)
promedio = t_total / cant_simulaciones

print(f"El tiempo promedio que tarda un incendio en extinguirse naturalmente luego de {cant_simulaciones} simulaciones es de {promedio} minutos")  
