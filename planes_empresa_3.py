
#Combinaciones de puertos
combinaciones_1 = [(a,0,0,0,0) for a in range(1,9)]
combinaciones_2 = [(a,b,0,0,0) for a in range(1,9) for b in range(1,9)]
combinaciones_3 = [(a,b,c,0,0) for a in range(1,9) for b in range(1,9) for c in range(1,9)]
combinaciones_4 = [(a,b,c,d,0) for a in range(1,9) for b in range(1,9) for c in range(1,9) for d in range(1,9)]  
combinaciones_5 = [(a,b,c,d,e) for a in range(1,9) for b in range(1,9) for c in range(1,9) for d in range(1,9) for e in range(1,9)]  

combinaciones_puertos = combinaciones_1 + combinaciones_2 + combinaciones_3 + combinaciones_4 + combinaciones_5

#FUNCION QUE EVITA REPITENCIAS DE COMBINACIONES
def sin_repetir(combinaciones_puertos):
    lista= list()
    lista2 = list()
    for combinacion in combinaciones_puertos:
        combinacion = sorted(combinacion)
        if not combinacion in lista:
            lista.append(combinacion)
    for item in lista:
        tupla = (item[0],item[1],item[2],item[3],item[4])
        lista2.append(tupla)
    return lista2

combinaciones_puertos = sin_repetir(combinaciones_puertos)

# FUNCION QUE CUENTA LA CANTIDAD DE PUERTOS VISITADOS
def puertos_visitados(combinacion):
    lista = []
    for puerto in combinacion:
        if not puerto in lista and puerto != 0:
            lista.append(puerto)
    return len(lista)


def crear_plan(combinaciones_puertos):
    
    planes = dict()
    
    for combinacion in combinaciones_puertos:
        
        # SE DEFINE LA CANTIDAD DE PUERTOS VISITADOS Y EL ADICIONAL 
        visitados = puertos_visitados(combinacion)
                
        # 1 PUERTO VISITADO
        if combinacion.count(0) == 4:
            planes[combinacion] = 54.6
            
        # 2 PUERTOS VISITADO
        if combinacion.count(0) == 3:
            if visitados == 1:
                planes[combinacion] = (48.6)*2
            if visitados == 2:
                planes[combinacion] = (51.6)*2
    
        # 3 PUERTOS VISITADO
        if combinacion.count(0) == 2:
            if visitados == 1:
                planes[combinacion] = (48.1)*3
            if visitados == 2:
                planes[combinacion] = (50.6)*3
            if visitados == 3:
                planes[combinacion] = (53.1)*3
        
        # 4 PUERTOS VISITADO        
        if combinacion.count(0) == 1:
            if visitados == 1:
                planes[combinacion] = (47.4)*4
            if visitados == 2:
                planes[combinacion] = (49.6)*4
            if visitados == 3:
                planes[combinacion] = (51.6)*4
            if visitados == 4:
                planes[combinacion] = (53.6)*4

        # 5 PUERTOS VISITADO        
        if combinacion.count(0) == 0:
            if visitados == 1:
                planes[combinacion] = (45.6)*5
            if visitados == 2:
                planes[combinacion] = (47.6)*5
            if visitados == 3:
                planes[combinacion] = (49.6)*5
            if visitados == 4:
                planes[combinacion] = (51.6)*5

    return planes



print(len(crear_plan(combinaciones_puertos)))

planes_empresa3 = crear_plan(combinaciones_puertos)
