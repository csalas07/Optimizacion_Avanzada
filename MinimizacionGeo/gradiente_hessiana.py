import numpy as np
import sympy as sp
from scipy.optimize import minimize as mn

#Paso 1 proyeccion de paso matematicos
x,y = sp.symbols('x,y')
f_sym = 2*x**2 + y**2 - 2*x*y - 4*x -2*y+10

grad_sym = sp.Matrix([sp.diff(f_sym,x),sp.diff(f_sym,y)])
hess_sym = sp.hessian(f_sym,(x,y))

print("Analisis simbolico")
print("Gradiente f(xy): ", grad_sym.T)
print("Matriz Hessiana:")
sp.pprint(hess_sym)

#Punto critico
sol = sp.solve(grad_sym, (x,y))
px,py = float(sol[x]), float(sol[y])

H_num = np.array(hess_sym, dtype=np.float64)
eigenvals = np.linalg.eigvals(H_num)

#Impresion de resultados

print(f"Punto critico P*: ({px:.1f}, {py:.1f})")
print(f"Eigenvals de H: {eigenvals}")
print("Definicion de H:", "Positiva " if np.all(eigenvals>0) else "Otra")

#verificamos de manera numeric

def f_num(v):
    return 2*v[0]**2 + v[1]**2 - 2*v[0]*v[1] - 4*v[0] - 2*v[1] + 10


res = mn(f_num, [0,0], method='BFGS')

print("Verificación")
print(f"Solución NImerica: x = {res.x[0]:.4f}, y= {res.x[1]:.4f}")
print(f"valor minimo f(x*): {res.fun:.4f}")