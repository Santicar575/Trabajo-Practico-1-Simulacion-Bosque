import copy
from Tp1_Funciones_Cardelli import *

#Parametros
tamaño_bosque = 30 #N
d_inicial = 0.6 #Densidad inicial (Di)
t_quemado = 3 #Tiempo que tarda en quemarse un arbol por completo (Tq)
Px = [0,0.2,0.4,0.6,0.8,1,1,1,1] #Probabilidad de que un arbol se prenda fuego dependiendo la cantidad de vecinos que se estan quemando"
t = 0 #Tiempo de una simulacion
t_total = 0 #Tiempo total de todas las simulaciones
cant_simulaciones = 100 #Cantidad de simulaciones a realizar

#Inicilizacion de la matriz
matriz = [[-2 for _ in range(tamaño_bosque)] for _ in range(tamaño_bosque)] #Creo una matriz llena de -2 (celdas vacias)
setear_matriz(matriz,tamaño_bosque,d_inicial,t_quemado) #Se setea la matriz
matriz_inicial = copy.deepcopy(matriz) #Creo una copia de la matriz en un diferente espacio en memoria

#Loop principal de la simulacion
for _ in range(cant_simulaciones):
    t,_ = simulacion(matriz,tamaño_bosque,t_quemado,Px) #Se ejecuta una simulacion
    t_total += t #Al tiempo total se le suma el tiempo que tardo la anterior simulacion
    t = 0 #Se resetea el tiempo de la simulacion
    matriz = copy.deepcopy(matriz_inicial) #Se reinicia la matriz
promedio = t_total / cant_simulaciones 

print(f"El tiempo promedio que tarda un incendio en extinguirse naturalmente luego de {cant_simulaciones} simulaciones es de {promedio} minutos")  
