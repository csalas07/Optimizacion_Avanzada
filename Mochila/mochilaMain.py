#Parametros del problema
pesos = [2,3,4] #w_i
valores = [3,4, 5] #v_i
W =5 # Capacidad Maxima
n = len(pesos)

#Construcción de la tabla
#creamos la matriz

dp = [[0 for _ in range(W+1)] for _ in range(n+1)]

#llenado fila por fila

for i in range(1,n+1):
    w_i = pesos[i-1]
    v_i = valores[i-1]

    for w in range(W+1):
        if w_i>w:
            #Si el objeto es mas pesado que la capacidad actual, no entra
            dp[i][w] = dp[i-1][w]
        else:
            #Revision si meterlo o no
            no_meter = dp[i-1][w]
            meter = v_i + dp[i-1][w-w_i]
            dp[i][w] = max(no_meter, meter)

#Backtraking
objetos_seleccionados = []
w_restante = W

for i in range(n, 0, -1):
    #Si el valor cambio respecto a la fila superior, el objeto fue incluido
    if dp[i][w_restante] != dp [i-1][w_restante]:
        objetos_seleccionados.append(i) #Guardamos el indice del objeto
        w_restante -= pesos[i-1]
objetos_seleccionados.reverse()

#Impresión de resultados
print("==== Matriz dinamica ====")

for fila in dp:
    print(fila)


print("\n Resultado de la optimización")
print(f"valor máximo obtenido: {dp[n][w]}")
print(f"Objetos seleccionados: {objetos_seleccionados}")
print(f"Peso total: {sum(pesos[i-1] for i in objetos_seleccionados)} kg / {W} kg")