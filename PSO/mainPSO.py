import random as rd

def pso_1():
    #posicion del agua en el mapa
    def medir_altura(x,y):
        return x**2 + y**2

    #Creamos nuestras particulas (3... A,B,C)

    particulas = {
        'A':{'x':8, 'y':6, "vx":0, 'vy':0},
        'B':{'x':-5, 'y':5, "vx":0, 'vy':0},
        'C':{'x':2, 'y':-3, "vx":0, 'vy':0},
    }

    #Evaluamos la altura inicial de cada una
    gbest_nombre = None
    gbest_altura = float('inf')
    gbest_x, gbest_y = 0.0,0.0

    print("Demostración conceptual")

    for nombre, p in particulas.items():
        p['pbest_x'], p['pbest_y'] = p['x'], p['y']
        p['pbest_altura'] = medir_altura(p['x'], p['y'])

        print(f"Particula {nombre} inicio en {p['x']}, {p['y']} | Altura: {p['pbest_altura']}m")

        if p['pbest_altura'] < gbest_altura:
            gbest_altura = p['pbest_altura']
            gbest_x, gbest_y = p['x'], p['y']
            gbest_nombre = nombre

    print(f"\n --> Radio del enjambre: El lider inicial es particula {gbest_nombre} ({gbest_altura}m)\n")

    #hacemos simulación de un paso de movimiento hacia el lider
    for nombre, p in particulas.items():
        #Tiron social hacia la mejor particula
        tiron_x = 0.5 * (gbest_x - p['x'])
        tiron_y = 0.5 * (gbest_y - p['y'])

        #Nos movemos hacia el lider
        p['x'] += tiron_x
        p['y'] += tiron_y
        nueva_altura = medir_altura(p['x'], p['y'])

        print(f"Particula {nombre} avanzo hacia el lider -> Nueva posición: ({p['x']:.1f}, {p['y']:.1f})m")

def pso_2():
      #posicion del agua en el mapa
        def medir_altura(x,y):
            return x**2 + y**2
    
        #Creamos nuestras particulas (3... A,B,C)
    
        particulas = {
            'A':{'x':8, 'y':6, "vx":0, 'vy':0},
            'B':{'x':-5, 'y':5, "vx":0, 'vy':0},
            'C':{'x':2, 'y':-3, "vx":0, 'vy':0},
        }
    
        #Configuración de parametros
        w = 0.5 #inercia
        c1 = 1.0 #f. cognitivo
        c2 = 1.5 #f.social


        gbest_nombre = None
        gbest_altura = float('inf')
        gbest_x, gbest_y = 0.0,0.0
    
        print("Iniciamos particulas")
    
        for nombre, p in particulas.items():
            p['pbest_x'], p['pbest_y'] = p['x'], p['y']
            p['pbest_altura'] = medir_altura(p['x'], p['y'])
    
            print(f"Particula {nombre} inicio en {p['x']}, {p['y']} | Altura: {p['pbest_altura']}m")
    
            if p['pbest_altura'] < gbest_altura:
                gbest_altura = p['pbest_altura']
                gbest_x, gbest_y = p['x'], p['y']
                gbest_nombre = nombre
    
        print(f"\n --> Radio del enjambre: El lider inicial es particula {gbest_nombre} ({gbest_altura}m)\n")
    
        #hacemos simulación de un paso de movimiento hacia el lider
        for nombre, p in particulas.items():
            r1, r2 = rd.random(), rd.random()

            #Actualizar Velocidades
            p['vx'] = w * p['vx'] + c1 * r1 * (p['pbest_y'] - p['x']) + c2 * r2 * (gbest_x - p['x'])
            p['vy'] = w * p['vy'] + c1 * r1 * (p['pbest_y'] - p['y']) + c2 * r2 * (gbest_y - p['y'])

            #Actualizamos las posiciones
            p['x'] += p['vx']
            p['y'] += p['vy']

            nueva_altura = medir_altura(p['x'], p['y'])
            print(f"Particula {nombre} se movio a: ({p['x']:.2f}, {p['y']:.2f})m | Nueva Altura: {nueva_altura:.2f}m")

            #Actualizamos pbest si mejoro
            if nueva_altura < p['pbest_altura']:
                p['pbest_altura'] = nueva_altura
                p['pbest_x'], p['pbest_y'] = p['x'], p['y']

                #actualizamos gbesti si supero el lider global
                if nueva_altura < gbest_altura:
                    gbest_altura = nueva_altura
                    gbest_x, gbest_y = p['x'], p['y']
                    gbest_nombre = nombre
        print(f"\n --> nuevo lider tras paso 1: Particula {gbest_nombre} con {gbest_altura:.2f}m")

pso_2()