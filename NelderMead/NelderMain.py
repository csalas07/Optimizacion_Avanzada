import numpy as np
from scipy.optimize import minimize as mn

#Definicion de la caja negra
def black_box(x):
    return np.abs(x[0]-3) +(x[1]-2)**2

#Generamos los puntos iniciales del Simplex
x0 = np.array([0.0,0.0])
initial_simplex = np.array([
    [0.0,0.0],
    [2.0, 0.0],
    [0.0, 2.0]
])

#Optimización por Nelder-Mead
#Usamos nuestra matriz inicial con el resumen de la convergencia
resultado = mn(
    black_box, x0, method='Nelder-Mead',
    options={
        'initial_simplex': initial_simplex, 'disp': True
    }
)

print("\n===Resultado Final ===")
print(f"Optimo encontrado (x*): {resultado.x}")
print(f"Valor Minimo: {resultado.fun}")
print(f"Evaluaciones de f(x): {resultado.nfev}")
print(f"Iteraciones totales: {resultado.nit}")