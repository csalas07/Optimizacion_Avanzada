import random
import math

#1 - Parametros iniciales
Poblacion_Tam = 40 #Numero de individuos
Generaciones = 40 #Iteraciones
Prob_Cruce = 0.8 #Probabilidad de cruzar dos padres
Prob_Muta = 0.2 #Probabilidad de mutar al hijo
Rango_Min = -3.0 #Limite inferior
Rango_Max = 3.0 #Limite Superior

#Función fitness
def calcular_fitness(x):
    return x**4 - 4 * (x**2) + 2

#Operadores geneticos
def crear_poblacion_incial(longitud):
    return [random.uniform(Rango_Min,Rango_Max) for _ in range(longitud)]

#Seleccion por torneo, donde elegiremos 3 al azar y nos quedamos con el mejor (menor f(x))
def seleccion_torneo(poblacion, k=3):
    aspirantes = random.sample(poblacion,k)
    #Buscamos al minimo
    mejor = min(aspirantes, key = calcular_fitness)
    return mejor

#Cruzamiento, mezcla de padres para generar 2 hijitos
def cruza(padre1, padre2):
    if random.random() < Prob_Cruce:
        alpha = random.random() #peso aleatorio entre 0 y 1
        hijo1 = alpha * padre1 + (1-alpha) * padre2
        hijo2 = (1-alpha) * padre1 + alpha * padre2
        return hijo1, hijo2
    return padre1, padre2

#Mutación Gausiana
def muta(individuo):
    if random.random()< Prob_Muta:
        ruido = random.gauss(0,0.2) #Media = 0 y Desv_Est = 0.2
        nuevo_x = individuo + ruido
        #Mantener dentro de los los limites del dominio [-3,3]
        return max(Rango_Min, min(Rango_Max, nuevo_x))
    return individuo

#===============================
#Bucle principal
#==============================

poblacion = crear_poblacion_incial(Poblacion_Tam)

for gen in range(Generaciones):
    nueva_poblacion = []

    #Conservamos al mejor de todos solo para no perder buenas soluciones
    mejor_actual = min(poblacion, key = calcular_fitness)
    nueva_poblacion.append(mejor_actual)

    #Generamos el resto de la nueva poblacion
    while len(nueva_poblacion) < Poblacion_Tam:
        #Seleccion de padres
        padre1 = seleccion_torneo(poblacion)
        padre2 = seleccion_torneo(poblacion)

        #cruzamos
        hijo1, hijo2 = cruza(padre1, padre2)

        #Mutamos
        hijo1 = muta(hijo1)
        hijo2 = muta(hijo2)

        #añadimos nueva generacion
        nueva_poblacion.append(hijo1)
        if len(nueva_poblacion) < Poblacion_Tam:
            nueva_poblacion.append(hijo2)
    poblacion = nueva_poblacion


#Resultados finales
mejor_x = min(poblacion, key = calcular_fitness)
mejor_f = calcular_fitness(mejor_x)

print(f"Mejor 'x' encontrado : {mejor_x:.4f}")
print(f"Valor 'f(x)' en x: {mejor_f:.4f}")
print(f"\nValor exacto teórico: x = +-{math.sqrt(2):.4f}, f(x) = -2.0000")
