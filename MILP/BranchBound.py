import numpy as np
from scipy.optimize import linprog as lp


#Definición del problema base minimizamos Z = -3x -5y
c=[-3.0,-5.0]

#Restricciones
A_ub=[
    [1.0, 2.0], # x + 2y <= 3.5
    [1.0, -3.0] # x - 3y <= 0
]

b_ub = [3.5, 0.0]

#Limites por defecto a las variables x >= 0, 0 <= y <= 1
bounds_base = [(0, None), (0,1)]

#Creación del branch & bound recursivo
def branch_and_bound(bounds_actuales, nivel=0, nombre_nodo='Nodo Raíz'):
    prefix = " " * nivel
    print(f"\n{prefix} == {nombre_nodo} ==")

    #Paso 1 Relajación continua del nodo actual
    res = lp(c, A_ub = A_ub, b_ub = b_ub, bounds = bounds_actuales, method = 'highs')

    #Poda 1
    if not res.success:
        print(f"{prefix} ---> [Poda por INFACTIBILIDAD] no hay solución en la rama")
        return -np.inf, None

    x_val, y_val, = res.x[0], res.x[1]
    z_val = -res.fun #Inversión para maximizar
    print(f"{prefix} Solución Continua: x = {x_val:.2f}, y = {y_val:2f} | z = {z_val:2f}")

    #Paso 2 Verificar que la variable binaria ya es entera (Y)
    #Usaremos una toleraincia 0 y 1

    if np.isclose(y_val, np.round(y_val), atol=1e-5):
        print(f"{prefix} --> [Solución Entera Factible] y = {int(np.round(y_val))}")
        return z_val, (x_val, int(np.round(y_val)))

    #Paso 3 Ramificación sobre Y
    print(f"{prefix} --> 'y = {y_val:2f} es fraccionada ... Ramificando...")

    #Izquierda: forzar a y <=0 (Limite superior pasara a 0)
    bounds_izq = [bounds_actuales[0], (bounds_actuales[1][0], 0)]
    z_izq, sol_izq = branch_and_bound(bounds_izq, nivel + 1, "Rama y >=1")

    #Rama Derecha: forzar a y >=1 (pasamos el limite superior de Y a 1)
    bounds_der = [bounds_actuales[0], (1, bounds_actuales[1][1])]
    z_der, sol_der = branch_and_bound(bounds_der, nivel + 1, "Rama y >= 1")

    #Paso 4: Selección de mejor solución entre ambas ramas
    if z_izq >= z_der:
        return z_izq, sol_izq
    else:
        return z_der, sol_der

#Ejecución
z_opt, sol_opt = branch_and_bound(bounds_base)
print("Resultado Final del Solver")
print(f"Solución Óptima: x = {sol_opt[0]:.2f} (Continuo), y = {sol_opt[1]} (Binario)")
print(f"Beneficio Maximo: Z = {z_opt:.2f}")