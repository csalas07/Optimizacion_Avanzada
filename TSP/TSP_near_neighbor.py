#Generamos nuestra matriz de distancias (A=0, B=1, C=2, D=3)

distancias = [
    [0,10,25,49], #A
    [10, 0, 30, 15], #B
    [25, 30, 0, 20], #C
    [40, 15, 20, 0] #D
]

nombres = ['Deposito A', 'Casa B', 'Casa C', 'Casa D']

#Aplicamos el algoritmo de vecino más cercano
def tsp_vecino_cercano(matriz_distancia, inicio = 0):
    total_ciudades = len(matriz_distancia)
    visitados = [inicio]
    distancia_total = 0
    cactual = inicio

    #Repetir hasta recorrer todas las ciudades
    while len(visitados) < total_ciudades:
        mas_cerca = None #vacio
        menor_distancia = float('inf')#numero muy grande

        #Buscamos entre las ciudades no visistadas
        for csiguiente in range(total_ciudades):
            if csiguiente not in visitados:
                distancia = matriz_distancia[cactual][csiguiente]

                if distancia < menor_distancia:
                    menor_distancia = distancia
                    mas_cerca = csiguiente

        #Avanzamos a la ciudad encontrada
        visitados.append(mas_cerca)
        distancia_total += menor_distancia
        cactual = mas_cerca

    #Pasos finales, regresamos al punto inicial
    distancia_regreso = matriz_distancia[cactual][inicio]
    distancia_total += distancia_regreso
    visitados.append(inicio)

    #Le damos nombre a las rutas
    ruta_nombrada = [nombres[i] for i in visitados]
    
    return ruta_nombrada, distancia_total

#Ejecutamos
ruta, kilomeros = tsp_vecino_cercano(distancias, 0)

print("===Solución===")

print("Ruta elegida: ", " -> ".join(ruta))

print("Distancia: ", kilomeros, "km")