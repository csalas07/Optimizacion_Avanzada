import math as mt
import random as rd

# Parametros del NSGA
T_POP = 20
GENERATIONS = 15
PROB_MUTA = 0.2

# Limites
MIN_VAL, MAX_VAL = -2.0, 4.0


# Evaluación de objetivos
def evaluar_objetivos(ind):
  x1, x2 = ind['x']
  f1 = x1**2 + x2**2
  f2 = (x1 - 2) + (x2 - 2) ** 2
  return [f1, f2]


def domina(ind1, ind2):
  f1, f2 = ind1['f'], ind2['f']
  es_igual_o_mejor = (f1[0] <= f2[0]) and (f1[1] <= f2[1])
  es_estrictamente_mejor = (f1[0] < f2[0]) or (f1[1] < f2[1])
  return es_igual_o_mejor and es_estrictamente_mejor


# Mecanismos del NSGAII
def clasificar_no_dominancia(poblacion):
  frentes = [[]]

  for p in poblacion:
    p['S'] = []  # Individuos a los que p domina
    p['n'] = 0  # Contador de individuos que dominan a p

    for q in poblacion:
      if domina(p, q):
        p['S'].append(q)
      elif domina(q, p):
        p['n'] += 1
    if p['n'] == 0:
      p['rank'] = 1
      frentes[0].append(p)

  i = 0
  while len(frentes[i]) > 0:
    siguiente_frente = []
    for p in frentes[i]:
      for q in p['S']:
        q['n'] -= 1
        if q['n'] == 0:
          q['rank'] = i + 2
          siguiente_frente.append(q)

    i += 1
    if len(siguiente_frente) > 0:
      frentes.append(siguiente_frente)
    else:
      break

  return [f for f in frentes if len(f) > 0]


def calcular_distancias(frente):
  l = len(frente)
  if l == 0:
    return
  for ind in frente:
    ind['distance'] = 0.0

  n_objetivos = len(frente[0]['f'])

  for m in range(n_objetivos):
    frente.sort(key=lambda x: x['f'][m])

    frente[0]['distance'] = float('inf')
    frente[-1]['distance'] = float('inf')

    f_min = frente[0]['f'][m]
    f_max = frente[-1]['f'][m]

    if f_max == f_min:
      continue

    for i in range(1, l - 1):
      frente[i]['distance'] += (frente[i + 1]['f'][m] - frente[i - 1]['f'][m]) / (
          f_max - f_min
      )


def crear():
  ind = {
      'x': [rd.uniform(MIN_VAL, MAX_VAL), rd.uniform(MIN_VAL, MAX_VAL)],
      'rank': 1,
      'distance': 0.0,
  }
  ind['f'] = evaluar_objetivos(ind)
  return ind


def seleccion(popu):
  p1, p2 = rd.choice(popu), rd.choice(popu)
  if p1['rank'] < p2['rank']:
    return p1
  elif p2['rank'] < p1['rank']:
    return p2
  else:
    return p1 if p1['distance'] > p2['distance'] else p2


def cruza_muta(padre1, padre2):
  alpha = rd.random()
  hijo_x = [
      alpha * p1 + (1 - alpha) * p2 for p1, p2 in zip(padre1['x'], padre2['x'])
  ]

  # Mutación
  for i in range(len(hijo_x)):
    if rd.random() < PROB_MUTA:
      hijo_x[i] += rd.gauss(0, 0.5)
      hijo_x[i] = max(MIN_VAL, min(MAX_VAL, hijo_x[i]))

  hijo = {'x': hijo_x}
  hijo['f'] = evaluar_objetivos(hijo)
  return hijo


# Ejecutamos NSGA
poblacion = [crear() for _ in range(T_POP)]

for gen in range(1, GENERATIONS + 1):
  hijos = []
  while len(hijos) < T_POP:
    p1 = seleccion(poblacion)
    p2 = seleccion(poblacion)
    hijos.append(cruza_muta(p1, p2))

  r_t = poblacion + hijos
  frentes = clasificar_no_dominancia(r_t)

  nueva_pop = []
  for frente in frentes:
    calcular_distancias(frente)
    if len(nueva_pop) + len(frente) <= T_POP:
      nueva_pop.extend(frente)
    else:
      frente.sort(key=lambda x: x['distance'], reverse=True)
      espacio_restante = T_POP - len(nueva_pop)
      nueva_pop.extend(frente[:espacio_restante])
      break
  poblacion = nueva_pop
  print(
      f"Generación {gen:02d} completada. Tamaño del frente 1:"
      f" {len([i for i in poblacion if i['rank']==1])}"
  )

# Mostramos el frente
frente_1 = [ind for ind in poblacion if ind['rank'] == 1]
frente_1.sort(key=lambda ind: ind['f'][0])

print("\nSoluciones")
print(
    f"{'Solución':<10} | {'Variables (x1, x2)':<25} | {'Obj 1 (f1)':<12} |"
    f" {'Obj 2 (f2)':<12}"
)

for idx, ind in enumerate(frente_1, 1):
  x_str = f"[{ind['x'][0]:.3f}, {ind['x'][1]:.3f}]"
  print(
      f"Dron {idx:<5} | {x_str:<25} | {ind['f'][0]:<12.4f} |"
      f" {ind['f'][1]:<12.4f}"
  )