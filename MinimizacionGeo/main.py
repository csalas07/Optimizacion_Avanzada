from scipy.optimize import minimize as mn

#El problema busca maximizar la resistencia de S = b * h^^2
#como la función minimize esta diseñada para minimizar, se aplica la equivalencia matematica
#por ello retornamos el resultado en negstivo.
def objetivo_negativo(x):
    b, h = x[0], x[1]
    return -(b*(h**2)) #Minimiz el negativo de la resistencia

#restricciones, las restricciones del tipo ineq deben definirse de la forma g(x)>=0
#la inecuación se redondea a 1600 - b^2-h^2>=0
const = ({'type':'ineq', 'fun': lambda x: 1600 - (x[0]**2 + x[1]**2)})
bound = [(1e-3, None), (1e-3,None)] #busqueda de limites donde 1e-3 es el limite inferior en lugar de 0 para eviar dimensiones por 0 
x0 = [10,10]

res = mn(objetivo_negativo, x0, method='SLSQP', bounds=bound, constraints=const)
print("===Ejercicio 1===")
print(f"Ancho optimo (b*): {res.x[0]:.4f} cm")
print(f"Altura optima (h*): {res.x[1]:.4f} cm")
print(f"Relación h/b: {res.x[1]/res.x[0]:.4f} aprox a 1.4142")
print(f"Resistencia Maximxa S(xb*): {-res.fun:.2f}")

#Actua como un experto en optimización numerica y python que use el metodo SLSQP de la libreria scipy.optimize.minimize
#Para resulver el siguiente problema:
#-Función a maximizar: S= b*h^2 (se debe minimizar -S)
#Restriccion: el diametro cumple b^2 + h^2 <= 1600
#limites: b>0 y h>0
#punto inicial: [10,10]
#imprime b*, h*, la relación h/b y el valor optimo S(x*) con formato de 4 decimales
