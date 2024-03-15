import copy
from Tp1_Funciones_Cardelli import *
import math

#Parametros
tamaño_bosque = 30 #N
t_quemado = 3 #Tiempo que tarda en quemarse un arbol por completo (Tq)
Px = [0,0.2,0.4,0.6,0.8,1,1,1,1] #Probabilidad de que un arbol se prenda fuego dependiendo la cantidad de vecinos que se estan quemando"
t = 0 #Tiempo de una simulacion
cant_simulaciones = 100 #Cantidad de simulaciones a realizar
cant_arboles_quemados = 0
d_inicial = 0.1

#Inicilizacion de la matriz
matriz = [[-2 for _ in range(tamaño_bosque)] for _ in range(tamaño_bosque)] #Creo una matriz llena de -2 (celdas vacias)
setear_matriz(matriz,tamaño_bosque,d_inicial,t_quemado) #Se setea la matriz
matriz_inicial = copy.deepcopy(matriz) #Creo una copia de la matriz en un diferente espacio en memoria

#Loop principal de la simulacion

print("+----------+----------------+")
print("| Densidad | Bosque quemado |")
print("+----------+----------------+")

for _ in range (10):
    for _ in range(cant_simulaciones):
        _,matriz = simulacion(matriz,tamaño_bosque,t_quemado,Px) #Se ejecuta una simulacion
        cant_arboles_quemados += cantidades_matriz(matriz, tamaño_bosque)["arboles_quemados"] #Se suman las cantidades de arboles quemados de todas las simulaciones
        matriz = copy.deepcopy(matriz_inicial) #Se reinicia la matriz
    promedio_arboles_quemados = cant_arboles_quemados/cant_simulaciones
    porcentaje_bosque_quemado = (100 * promedio_arboles_quemados)/((tamaño_bosque**2)) #Calculo del porcentaje
    cant_arboles_quemados = 0 
    #Se imprimen todos los resultados con el mismo formato y que queden todos iguales 
    print(f"| {round(d_inicial,1)}{' '*(len('densidad')-len(str(round(d_inicial,1))))} | {round(porcentaje_bosque_quemado,2)} %{' '*(len('Bosque quemado')-len(str(round(porcentaje_bosque_quemado,2))+' %'))} |")
    print("+----------+----------------+")
    d_inicial += 0.1 #Se aumenta en 0.1 la densidad
    setear_matriz(matriz,tamaño_bosque,d_inicial,t_quemado) #Se vuelve a setear la matriz con la nueva densidad
    matriz_inicial = copy.deepcopy(matriz) #La matriz inicial se cambia por la nueva matriz