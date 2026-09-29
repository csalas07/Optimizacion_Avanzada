import numpy as np
import sympy as sp
from scipy.optimize import minimize as mn

#Verificación de convexidad
x1, x2 = sp.symbols('x1 x2')
f = x1**2 + 2*x2**2 - 2*x1*x2 -4*x1

H = sp.hessian(f, (x1, x2))
eigenvals = [float(ev) for ev in H.eigenvals().keys()]

print("=====Verificamos la Convexalidad=========")
print("Matriz Hessiana:\n")
sp.pprint(H)

print(F"Eigenvals de H: {eigenvals}")
is_convex = all(ev > 0 for ev in eigenvals)
print(f"¿Nuestra función es estrictamente convexa?: {is_convex}\n")

#Resolución
def funcion_objetivo(x):
    return x[0]**2 + 2*x[1]**2 - 2*x[0]*x[1]-4*x[0]

#Restricción x1 + x2 <= 3 ----> 3 - x1- x2 >= 0
restriccion = {'type': 'ineq', 'fun': lambda x: 3 -(x[0] + x[1])}
limites = [(0, None), (0, None)]
x0 = [0,0]

solucion = mn(funcion_objetivo, x0, method='SLSQP', bounds=limites, constraints=restriccion)

#Resultado
print("========Resultados de la Optimización=================")
print(f"Estado de convergencia: {solucion.message}")
print(f"x1 Optimo global: {solucion.x[0]:.2f}")
print(f"x2 Optimo global: {solucion.x[1]:.2f}")
print(f"Valor minimo f(x*): {solucion.fun:.2f}")

#Prompt 
#Escribe un scrip en Python usando Sympy y SciPY para resolver esl siguiente problema de optimización convexa:
# -Funcion objetico f(x1,x2) = x1^2 + 2x2^2 - 2x1*x2 - 4x1
# - Restricciones x1+x2 <= 3 y x, x2 >=0

#El codigo debe:
#1 - Calcular la matriz hessiana y sus eigenvalores con SymPy para comprobar que sea convexo
#2 - Resolver el problema con la función de minimize de scipy desde x0 = [0,0]
#3 - Imprimir la Hessiana, eigenvalores, la confirmación de convexidad, las variables óptimas (x1, x2) y f(x*)
