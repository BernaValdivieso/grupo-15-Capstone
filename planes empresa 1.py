
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
                
        # 1 UNIDAD
        
        if combinacion.count(0) == 4:
            if (combinacion.count(1) > 0) or (combinacion.count(2) > 0):
                planes[combinacion] = 50
            if (combinacion.count(3) > 0) or (combinacion.count(4) > 0):
                planes[combinacion] = 50
            if (combinacion.count(5) > 0) or (combinacion.count(6) > 0):
                planes[combinacion] = 54
            if (combinacion.count(7) > 0) or (combinacion.count(8) > 0):
                planes[combinacion] = 58
            
        # 2 UNIDADES
        
        if combinacion.count(0) == 3:
            
            # SE ENTREGAN LAS 2 UNIDADES EN EL MISMO PUERTO
            
            if visitados == 1:
                if (combinacion.count(1) > 0) or (combinacion.count(2) > 0):
                    planes[combinacion] = 49 * 2
                if (combinacion.count(3) > 0) or (combinacion.count(4) > 0):
                    planes[combinacion] = 49 * 2
                if (combinacion.count(5) > 0) or (combinacion.count(6) > 0):
                    planes[combinacion] = 52.8 * 2
                if (combinacion.count(7) > 0) or (combinacion.count(8) > 0):
                    planes[combinacion] = 57.2 * 2
            
            # SE ENTREGA EN 2 PUERTOS DISTINTOS
                    
            if visitados == 2:
                # UNA UNIDAD EN REGIÓN 1 Y OTRA EN REGIÓN 1
                if (combinacion.count(1) + combinacion.count(2) == 2):
                    planes[combinacion] = 50 * 2
                # UNA UNIDAD EN REGIÓN 1 Y OTRA EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 1) and (combinacion.count(3) + combinacion.count(4) == 1):
                    planes[combinacion] = 49 * 2
                # UNA UNIDAD EN REGIÓN 1 Y OTRA EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 1) and (combinacion.count(5) + combinacion.count(6) == 1):
                    planes[combinacion] = 52 * 2
                # UNA UNIDAD EN REGIÓN 1 Y OTRA EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 1) and (combinacion.count(7) + combinacion.count(8) == 1):
                    planes[combinacion] = 58.5 * 2
                # UNA UNIDAD EN REGIÓN 2 Y OTRA EN REGIÓN 3
                if (combinacion.count(3) + combinacion.count(4) == 1) and (combinacion.count(5) + combinacion.count(6) == 1):
                    planes[combinacion] = 52 * 2
                # UNA UNIDAD EN REGIÓN 2 Y OTRA EN REGIÓN 4
                if (combinacion.count(3) + combinacion.count(4) == 1) and (combinacion.count(7) + combinacion.count(8) == 1):
                    planes[combinacion] = 58.5 * 2
                # UNA UNIDAD EN REGIÓN 3 Y OTRA EN REGIÓN 3
                if (combinacion.count(5) + combinacion.count(6) == 2):
                    planes[combinacion] = 53.6 * 2
                # UNA UNIDAD EN REGIÓN 3 Y OTRA EN REGIÓN 4
                if (combinacion.count(5) + combinacion.count(6) == 1) and (combinacion.count(7) + combinacion.count(8) == 1):
                    planes[combinacion] = 60.1 * 2
                # UNA UNIDAD EN REGIÓN 4 Y OTRA EN REGIÓN 4
                if (combinacion.count(7) + combinacion.count(8) == 2):
                    planes[combinacion] = 60.1 * 2
    
        # 3 UNIDADES
        
        if combinacion.count(0) == 2:
            
            # SE ENTREGAN LAS 3 UNIDADES EN EL MISMO PUERTO 
            
            if visitados == 1:
                if (combinacion.count(1) > 0) or (combinacion.count(2) > 0):
                    planes[combinacion] = 44 * 3
                if (combinacion.count(3) > 0) or (combinacion.count(4) > 0):
                    planes[combinacion] = 44 * 3
                if (combinacion.count(5) > 0) or (combinacion.count(6) > 0):
                    planes[combinacion] = 47.2 * 3
                if (combinacion.count(7) > 0) or (combinacion.count(8) > 0):
                    planes[combinacion] = 52.6 * 3
                    
            # SE ENTREGA EN DOS PUERTOS DISTINTOS
            
            if visitados == 2:
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1
                if (combinacion.count(1) + combinacion.count(2) == 2):
                    planes[combinacion] = 47.5 * 3
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 1) and (combinacion.count(3) + combinacion.count(4) == 1):
                    planes[combinacion] = 46.5 * 3
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 1) and (combinacion.count(5) + combinacion.count(6) == 1):
                    planes[combinacion] = 49.5 * 3
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 1) and (combinacion.count(7) + combinacion.count(8) == 1):
                    planes[combinacion] = 56 * 3
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3
                if (combinacion.count(3) + combinacion.count(4) == 1) and (combinacion.count(5) + combinacion.count(6) == 1):
                    planes[combinacion] = 49.5 * 3
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4
                if (combinacion.count(3) + combinacion.count(4) == 1) and (combinacion.count(7) + combinacion.count(8) == 1):
                    planes[combinacion] = 56 * 3
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3
                if (combinacion.count(5) + combinacion.count(6) == 2):
                    planes[combinacion] = 50.7 * 3
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4
                if (combinacion.count(5) + combinacion.count(6) == 1) and (combinacion.count(7) + combinacion.count(8) == 1):
                    planes[combinacion] = 57.2 * 3
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4
                if (combinacion.count(7) + combinacion.count(8) == 2):
                    planes[combinacion] = 57.6 * 3
                    
            # SE ENTREGA EN 3 PUERTOS DISTINTOS
            
        
        # 4 UNIDADES
        
        if combinacion.count(0) == 1:
            # SE ENTREGAN LAS 4 UNIDADES EN EL MISMO PUERTO 
            if visitados == 1:
                if (combinacion.count(1) > 0) or (combinacion.count(2) > 0):
                    planes[combinacion] = 43 * 4
                if (combinacion.count(3) > 0) or (combinacion.count(4) > 0):
                    planes[combinacion] = 43 * 4
                if (combinacion.count(5) > 0) or (combinacion.count(6) > 0):
                    planes[combinacion] = 45.8 * 4
                if (combinacion.count(7) > 0) or (combinacion.count(8) > 0):
                    planes[combinacion] = 51.6 * 4
                    
            # SE ENTREGA EN DOS PUERTOS DISTINTOS
            
            if visitados == 2:
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1
                if (combinacion.count(1) + combinacion.count(2) == 2):
                    planes[combinacion] = 46.5 * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 1) and (combinacion.count(3) + combinacion.count(4) == 1):
                    planes[combinacion] = 45.5 * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 1) and (combinacion.count(5) + combinacion.count(6) == 1):
                    planes[combinacion] = 48.5 * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 1) and (combinacion.count(7) + combinacion.count(8) == 1):
                    planes[combinacion] = 55 * 4
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3
                if (combinacion.count(3) + combinacion.count(4) == 1) and (combinacion.count(5) + combinacion.count(6) == 1):
                    planes[combinacion] = 48.5 * 4
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4
                if (combinacion.count(3) + combinacion.count(4) == 1) and (combinacion.count(7) + combinacion.count(8) == 1):
                    planes[combinacion] = 55 * 4
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3
                if (combinacion.count(5) + combinacion.count(6) == 2):
                    planes[combinacion] = 49.3 * 4
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4
                if (combinacion.count(5) + combinacion.count(6) == 1) and (combinacion.count(7) + combinacion.count(8) == 1):
                    planes[combinacion] = 55.8 * 4
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4
                if (combinacion.count(7) + combinacion.count(8) == 2):
                    planes[combinacion] = 56.6 * 4
                    
            # SE ENTREGA EN 3 PUERTOS DISTINTOS
            
            # SE ENTREGA EN 4 PUERTOS DISTINTOS 
            
            
        # 5 PUERTOS VISITADO        
        if combinacion.count(0) == 0:
            pass

    return planes



print(len(crear_plan(combinaciones_puertos)))

