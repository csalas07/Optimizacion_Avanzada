import numpy as np
from scipy.optimize import minimize as mn

#Función objetivo
def objetivo(x):
    return (x[0] - 4) **2 +(x[1]-4)**2

def rest_g1(x):
    return 4-(x[0]+x[1]) #g(x) >=0 -> 4 - x1 -x2 >=0

cons = {'type':'ineq', 'fun':rest_g1}
bounds = [(0, None), (0, None)]
x0 = [0,0]

#Solución Numerica
res = mn(objetivo, x0, method='SLSQP', bounds=bounds, constraints=cons)

#Resultados
print("========== Condiciones KKT ============")
print(f"Estatus: {res.message}")
print(f"Optimo x1*: {res.x[0]:.4f}")
print(f"Optimo x2*: {res.x[1]:.4f}")
print(f"Valor Minimo f(x*): {res.fun:.4}")

#Extraccion del multiplicado de Lagrange
if 'ineq' in res.get('maxcv', {}):
    print("Multiplicador mu_i ajustado numericamente")

#Escribe un script en python que resuelva el siguiente problema de optimización no lineal
#sujeto a restricciones de desigualdad

#-Función objetivo: f(x1, x2) = (x1-4)^2 + (x2-4)^2
#-Restricciones: x1 + x2 >=4 y no negatividad (x1,x2 >=0)

#Requisitos de codigo:
#1 - Modela la función objetivo y la restirccion de desigualdad (g(X) >=0)
#2- Resuelve el problema numerericamente utilizando la función minimize con el metodo SLSQP a partir de x0[0,0]
#3 - imprime los resultados como: estado de convergencia, punto optimo (x1*, x2*), formateado a 4 decimales
#  y el valor minimo f(x*).
#4 - Incluye la logica para extraer o hacer referencia a los multiplicadores Lagrange (Condiciones KKT)