region_de_puerto = {1: 1,
                    2: 1,
                    3: 2,
                    4: 2,
                    5: 3,
                    6: 3,
                    7: 4,
                    8: 4
                    }

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

# FUNCION QUE VE SI SE LE SUMA X O Y
def subclasificacion(combinacion):
    # SE CREA UN SET DONDE VAN A IR TODOS LOS PUERTOS
    puertos = set()
    # SE AGREGAN LOS ELEMENTOS DE LA TUPLA AL SET
    puertos.update(combinacion)
    # SE SACA EL 0 SI ES QUE SE ENCUENTRA EN EL SET
    puertos.discard(0)
    # LA IDEA ES TENER EN EL SET TODOS LOS PUERTOS EN LOS QUE SE VA A DESCARGAR
    # SI SE TIENE (0,0,1,1,1), EL SET ES {1} PORQUE SOLO SE VA AL PUERTO 1
    # SI SE TIENE (0,0,1,2,3), EL SET ES {1,2,3} Y ASÍ CON TODAS LAS COMBINACIONES
    
    # SI EL SET TIENE UN ELEMENTO, SIGNIFICA QUE TODOS LOS PUERTOS ESTÁN EN LA MISMA
    # CLASIFICACIÓN (ES EL MISMO PUERTO), POR LO QUE INDEPENDIENTE DE LA CLASIFICACIÓN 
    # EN LA QUE ESTÉN, SABEMOS QUE SE LE VA A SUMAR X
    if len(puertos) == 1:
        return "X"

    # SI EL SET TIENE MÁS DE UN ELEMENTO, SE DESCARGA EN DISTINTOS PUERTOS Y HAY QUE
    # REVISAR SI ESTOS ESTÁN EN LA MISMA SUBCLASIFICACIÓN O NO 
    sub_1 = 0
    sub_2 = 0
    sub_3 = 0
    for p in puertos:
        if region_de_puerto[p] == 1:
            sub_1 += 1
        elif region_de_puerto[p] == 2:
            sub_1 += 1
        elif region_de_puerto[p] == 3:
            sub_2 += 1
        elif region_de_puerto[p] == 4:
            sub_3 += 1
    # CASO EN QUE TODOS LOS PUERTOS ESTÁN EN SUBCLASIFICACIÓN 1 
    if (sub_1 != 0) and (sub_2 == 0) and (sub_3 == 0):
        return "X"
    # CASO EN QUE TODOS LOS PUERTOS ESTÁN EN SUBCLASIFICACIÓN 2 
    if (sub_1 == 0) and (sub_2 != 0) and (sub_3 == 0):
        return "X"
    # CASO EN QUE TODOS LOS PUERTOS ESTÁN EN SUBCLASIFICACIÓN 3 
    if (sub_1 == 0) and (sub_2 == 0) and (sub_3 != 0):
        return "X"
    # CUALQUIER OTRO CASO SE ADICIONA Y
    return "Y"



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
                if (combinacion.count(1) + combinacion.count(2) == 3):
                    planes[combinacion] = 47.5 * 3
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2
                if (combinacion.count(5) + combinacion.count(6) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    planes[combinacion] = 46.5 * 3
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    planes[combinacion] = 49.5 * 3
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    planes[combinacion] = 56 * 3
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    planes[combinacion] = 49.5 * 3
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    planes[combinacion] = 56 * 3
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3
                if (combinacion.count(5) + combinacion.count(6) == 3):
                    planes[combinacion] = 50.7 * 3
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    planes[combinacion] = 57.2 * 3
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4
                if (combinacion.count(7) + combinacion.count(8) == 3):
                    planes[combinacion] = 57.6 * 3
                    
            # SE ENTREGA EN 3 PUERTOS DISTINTOS
            if visitados == 3:
                letra = subclasificacion(combinacion)
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 1 
                if (combinacion.count(1) + combinacion.count(2) == 3):
                    if letra == "X":
                        planes[combinacion] = (47.5 + 1.1) * 3
                    elif letra == "Y":
                        planes[combinacion] = (47.5 + 3.8) * 3
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 2 
                if (combinacion.count(1) + combinacion.count(2) == 2) and (combinacion.count(3) + combinacion.count(4) == 1):
                    if letra == "X":
                        planes[combinacion] = (47.5 + 0.6) * 3
                    elif letra == "Y":
                        planes[combinacion] = (47.5 + 3.8) * 3
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 3 
                if (combinacion.count(1) + combinacion.count(2) == 2) and (combinacion.count(5) + combinacion.count(6) == 1):
                    if letra == "X":
                        planes[combinacion] = (47.5 + 0.9) * 3
                    elif letra == "Y":
                        planes[combinacion] = (47.5 + 4.95) * 3
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 4 
                if (combinacion.count(1) + combinacion.count(2) == 2) and (combinacion.count(7) + combinacion.count(8) == 1):
                    if letra == "X":
                        planes[combinacion] = (47.5 + 0.9) * 3
                    elif letra == "Y":
                        planes[combinacion] = (47.5 + 7) * 3
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 1
                if (combinacion.count(1) + combinacion.count(2) == 2) and (combinacion.count(3) + combinacion.count(4) == 1):
                    if letra == "X":
                        planes[combinacion] = (46.5 + 1.1) * 3
                    elif letra == "Y":
                        planes[combinacion] = (46.5 + 3.8) * 3
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 1) and (combinacion.count(3) + combinacion.count(4) == 2):
                    if letra == "X":
                        planes[combinacion] = (46.5 + 0.6) * 3
                    elif letra == "Y":
                        planes[combinacion] = (46.5 + 3.8) * 3
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 1) and (combinacion.count(3) + combinacion.count(4) == 1) and (combinacion.count(5) + combinacion.count(6) == 1):
                    if letra == "X":
                        planes[combinacion] = (46.5 + 0.9) * 3
                    elif letra == "Y":
                        planes[combinacion] = (46.5 + 4.95) * 3
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 1) and (combinacion.count(3) + combinacion.count(4) == 1) and (combinacion.count(7) + combinacion.count(8) == 1):
                    if letra == "X":
                        planes[combinacion] = (46.5 + 0.9) * 3
                    elif letra == "Y":
                        planes[combinacion] = (46.5 + 7) * 3
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 1
                if (combinacion.count(1) + combinacion.count(2) == 2) and (combinacion.count(5) + combinacion.count(6) == 1):
                    if letra == "X":
                        planes[combinacion] = (49.5 + 1.1) * 3
                    elif letra == "Y":
                        planes[combinacion] = (49.5 + 3.8) * 3
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 1) and (combinacion.count(5) + combinacion.count(6) == 1) and (combinacion.count(3) + combinacion.count(4) == 1):
                    if letra == "X":
                        planes[combinacion] = (49.5 + 0.6) * 3
                    elif letra == "Y":
                        planes[combinacion] = (49.5 + 3.8) * 3
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 1) and (combinacion.count(5) + combinacion.count(6) == 2):
                    if letra == "X":
                        planes[combinacion] = (49.5 + 0.9) * 3
                    elif letra == "Y":
                        planes[combinacion] = (49.5 + 4.95) * 3
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 1) and (combinacion.count(5) + combinacion.count(6) == 1) and (combinacion.count(7) + combinacion.count(8) == 1):
                    if letra == "X":
                        planes[combinacion] = (49.5 + 0.9) * 3
                    elif letra == "Y":
                        planes[combinacion] = (49.5 + 7) * 3
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(1) + combinacion.count(2) == 2) and (combinacion.count(7) + combinacion.count(8) == 1):
                    if letra == "X":
                        planes[combinacion] = (56 + 1.1) * 3
                    elif letra == "Y":
                        planes[combinacion] = (56 + 3.8) * 3
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 1) and (combinacion.count(7) + combinacion.count(8) == 1) and (combinacion.count(3) + combinacion.count(4) == 1):
                    if letra == "X":
                        planes[combinacion] = (56 + 0.6) * 3
                    elif letra == "Y":
                        planes[combinacion] = (56 + 3.8) * 3
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 1) and (combinacion.count(7) + combinacion.count(8) == 1) and (combinacion.count(5) + combinacion.count(6) == 1):
                    if letra == "X":
                        planes[combinacion] = (56 + 0.9) * 3
                    elif letra == "Y":
                        planes[combinacion] = (56 + 4.95) * 3
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 1) and (combinacion.count(7) + combinacion.count(8) == 2):
                    if letra == "X":
                        planes[combinacion] = (56 + 0.9) * 3
                    elif letra == "Y":
                        planes[combinacion] = (56 + 7) * 3
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 1) and (combinacion.count(5) + combinacion.count(6) == 1) and (combinacion.count(1) + combinacion.count(2) == 1):
                    if letra == "X":
                        planes[combinacion] = (49.5 + 1.1) * 3
                    elif letra == "Y":
                        planes[combinacion] = (49.5 + 3.8) * 3
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 2
                if (combinacion.count(3) + combinacion.count(4) == 2) and (combinacion.count(5) + combinacion.count(6) == 1):
                    if letra == "X":
                        planes[combinacion] = (49.5 + 0.6) * 3
                    elif letra == "Y":
                        planes[combinacion] = (49.5 + 3.8) * 3
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 3
                if (combinacion.count(3) + combinacion.count(4) == 1) and (combinacion.count(5) + combinacion.count(6) == 2):
                    if letra == "X":
                        planes[combinacion] = (49.5 + 0.9) * 3
                    elif letra == "Y":
                        planes[combinacion] = (49.5 + 4.95) * 3
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 4
                if (combinacion.count(3) + combinacion.count(4) == 1) and (combinacion.count(5) + combinacion.count(6) == 1) and (combinacion.count(7) + combinacion.count(8) == 1):
                    if letra == "X":
                        planes[combinacion] = (49.5 + 0.9) * 3
                    elif letra == "Y":
                        planes[combinacion] = (49.5 + 7) * 3
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 1) and (combinacion.count(7) + combinacion.count(8) == 1) and (combinacion.count(1) + combinacion.count(2) == 1):
                    if letra == "X":
                        planes[combinacion] = (56 + 1.1) * 3
                    elif letra == "Y":
                        planes[combinacion] = (56 + 3.8) * 3
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(3) + combinacion.count(4) == 2) and (combinacion.count(7) + combinacion.count(8) == 1):
                    if letra == "X":
                        planes[combinacion] = (56 + 0.6) * 3
                    elif letra == "Y":
                        planes[combinacion] = (56 + 3.8) * 3
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(3) + combinacion.count(4) == 1) and (combinacion.count(7) + combinacion.count(8) == 1) and (combinacion.count(5) + combinacion.count(6) == 1):
                    if letra == "X":
                        planes[combinacion] = (56 + 0.9) * 3
                    elif letra == "Y":
                        planes[combinacion] = (56 + 4.95) * 3
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(3) + combinacion.count(4) == 1) and (combinacion.count(7) + combinacion.count(8) == 2):
                    if letra == "X":
                        planes[combinacion] = (56 + 0.9) * 3
                    elif letra == "Y":
                        planes[combinacion] = (56 + 7) * 3
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 1
                if (combinacion.count(5) + combinacion.count(6) == 2) and (combinacion.count(1) + combinacion.count(2) == 1):
                    if letra == "X":
                        planes[combinacion] = (50.7 + 1.1) * 3
                    elif letra == "Y":
                        planes[combinacion] = (50.7 + 3.8) * 3
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 2
                if (combinacion.count(5) + combinacion.count(6) == 2) and (combinacion.count(3) + combinacion.count(4) == 1):
                    if letra == "X":
                        planes[combinacion] = (50.7 + 0.6) * 3
                    elif letra == "Y":
                        planes[combinacion] = (50.7 + 3.8) * 3
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 3
                if (combinacion.count(5) + combinacion.count(6) == 3):
                    if letra == "X":
                        planes[combinacion] = (50.7 + 0.9) * 3
                    elif letra == "Y":
                        planes[combinacion] = (50.7 + 4.95) * 3
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 4
                if (combinacion.count(5) + combinacion.count(6) == 2) and (combinacion.count(7) + combinacion.count(8) == 1):
                    if letra == "X":
                        planes[combinacion] = (50.7 + 0.9) * 3
                    elif letra == "Y":
                        planes[combinacion] = (50.7 + 7) * 3
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(5) + combinacion.count(6) == 1) and (combinacion.count(7) + combinacion.count(8) == 1) and (combinacion.count(1) + combinacion.count(2) == 1):
                    if letra == "X":
                        planes[combinacion] = (57.2 + 1.1) * 3
                    elif letra == "Y":
                        planes[combinacion] = (57.2 + 3.8) * 3
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(5) + combinacion.count(6) == 1) and (combinacion.count(7) + combinacion.count(8) == 1) and (combinacion.count(3) + combinacion.count(4) == 1):
                    if letra == "X":
                        planes[combinacion] = (57.2 + 0.6) * 3
                    elif letra == "Y":
                        planes[combinacion] = (57.2 + 3.8) * 3
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(5) + combinacion.count(6) == 2) and (combinacion.count(7) + combinacion.count(8) == 1):
                    if letra == "X":
                        planes[combinacion] = (57.2 + 0.9) * 3
                    elif letra == "Y":
                        planes[combinacion] = (57.2 + 4.95) * 3
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(5) + combinacion.count(6) == 1) and (combinacion.count(7) + combinacion.count(8) == 2):
                    if letra == "X":
                        planes[combinacion] = (57.2 + 0.9) * 3
                    elif letra == "Y":
                        planes[combinacion] = (57.2 + 7) * 3
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(7) + combinacion.count(8) == 2) and (combinacion.count(1) + combinacion.count(2) == 1):
                    if letra == "X":
                        planes[combinacion] = (57.6 + 1.1) * 3
                    elif letra == "Y":
                        planes[combinacion] = (57.6 + 3.8) * 3
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(7) + combinacion.count(8) == 2) and (combinacion.count(3) + combinacion.count(4) == 1):
                    if letra == "X":
                        planes[combinacion] = (57.6 + 0.6) * 3
                    elif letra == "Y":
                        planes[combinacion] = (57.6 + 3.8) * 3
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(7) + combinacion.count(8) == 2) and (combinacion.count(5) + combinacion.count(6) == 1):
                    if letra == "X":
                        planes[combinacion] = (57.6 + 0.9) * 3
                    elif letra == "Y":
                        planes[combinacion] = (57.6 + 4.95) * 3
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(7) + combinacion.count(8) == 3):
                    if letra == "X":
                        planes[combinacion] = (57.6 + 0.9) * 3
                    elif letra == "Y":
                        planes[combinacion] = (57.6 + 7) * 3
        
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
                if (combinacion.count(1) + combinacion.count(2) == 4):
                    planes[combinacion] = 46.5 * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2
                if (combinacion.count(5) + combinacion.count(6) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    planes[combinacion] = 45.5 * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    planes[combinacion] = 48.5 * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    planes[combinacion] = 55 * 4
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    planes[combinacion] = 48.5 * 4
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    planes[combinacion] = 55 * 4
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3
                if (combinacion.count(5) + combinacion.count(6) == 4):
                    planes[combinacion] = 49.3 * 4
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    planes[combinacion] = 55.8 * 4
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4
                if (combinacion.count(7) + combinacion.count(8) == 4):
                    planes[combinacion] = 56.6 * 4
                    
            # SE ENTREGA EN 3 PUERTOS DISTINTOS
            
            if visitados == 3:
                letra = subclasificacion(combinacion)
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 1 
                if (combinacion.count(1) + combinacion.count(2) == 4):
                    if letra == "X":
                        planes[combinacion] = (46.5 + 0.8) * 4
                    elif letra == "Y":
                        planes[combinacion] = (46.5 + 2.55) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 2 
                if (combinacion.count(5) + combinacion.count(6) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (46.5 + 0.5) * 4
                    elif letra == "Y":
                        planes[combinacion] = (46.5 + 2.55) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 3 
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (46.5 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (46.5 + 3.6) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 4 
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (46.5 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (46.5 + 5.3) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 1
                if (combinacion.count(5) + combinacion.count(6) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (45.5 + 0.8) * 4
                    elif letra == "Y":
                        planes[combinacion] = (45.5 + 3.8) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 2
                if (combinacion.count(5) + combinacion.count(6) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (45.5 + 0.5) * 4
                    elif letra == "Y":
                        planes[combinacion] = (45.5 + 2.55) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 3
                if (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (45.5 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (45.5 + 3.6) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 4
                if (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (45.5 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (45.5 + 5.3) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.5 + 0.8) * 4
                    elif letra == "Y":
                        planes[combinacion] = (48.5 + 2.55) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 2
                if (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.5 + 0.5) * 4
                    elif letra == "Y":
                        planes[combinacion] = (48.5 + 2.55) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 3
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.5 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (48.5 + 3.6) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 4
                if (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.5 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (48.5 + 5.3) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (55 + 0.8) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55 + 2.55) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (55 + 0.5) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55 + 2.55) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (55 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55 + 3.6) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (55 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55 + 5.3) * 4
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 1
                if (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.5 + 0.8) * 4
                    elif letra == "Y":
                        planes[combinacion] = (48.5 + 2.55) * 4
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.5 + 0.5) * 4
                    elif letra == "Y":
                        planes[combinacion] = (48.5 + 2.55) * 4
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.5 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (48.5 + 3.6) * 4
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.5 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (48.5 + 5.3) * 4
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (55 + 0.8) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55 + 2.55) * 4
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (55 + 0.5) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55 + 2.55) * 4
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0):
                    if letra == "X":
                        planes[combinacion] = (55 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55 + 3.6) * 4
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (55 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55 + 5.3) * 4
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (49.3 + 0.8) * 4
                    elif letra == "Y":
                        planes[combinacion] = (49.3 + 2.55) * 4
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (49.3 + 0.5) * 4
                    elif letra == "Y":
                        planes[combinacion] = (49.3 + 2.55) * 4
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 3
                if (combinacion.count(5) + combinacion.count(6) == 4):
                    if letra == "X":
                        planes[combinacion] = (49.3 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (49.3 + 3.6) * 4
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (49.3 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (49.3 + 5.3) * 4
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (55.8 + 0.8) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55.8 + 2.55) * 4
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0):
                    if letra == "X":
                        planes[combinacion] = (55.8 + 0.5) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55.8 + 2.55) * 4
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (55.8 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55.8 + 3.6) * 4
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (55.8 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55.8 + 5.3) * 4
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (56.6 + 0.8) * 4
                    elif letra == "Y":
                        planes[combinacion] = (56.6 + 2.55) * 4
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (56.6 + 0.5) * 4
                    elif letra == "Y":
                        planes[combinacion] = (56.6 + 2.55) * 4
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (56.6 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (56.6 + 3.6) * 4
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(7) + combinacion.count(8) == 4):
                    if letra == "X":
                        planes[combinacion] = (56.6 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (56.6 + 5.3) * 4
            
            # SE ENTREGA EN 4 PUERTOS DISTINTOS 

            if visitados == 4:
                letra = subclasificacion(combinacion)
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 1 
                if (combinacion.count(1) + combinacion.count(2) == 4):
                    if letra == "X":
                        planes[combinacion] = (46.5 + 0.8) * 4
                    elif letra == "Y":
                        planes[combinacion] = (46.5 + 2.55) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 2 
                if (combinacion.count(5) + combinacion.count(6) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (46.5 + 0.5) * 4
                    elif letra == "Y":
                        planes[combinacion] = (46.5 + 2.55) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 3 
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (46.5 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (46.5 + 3.6) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 4 
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (46.5 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (46.5 + 5.3) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 1
                if (combinacion.count(5) + combinacion.count(6) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (45.5 + 0.8) * 4
                    elif letra == "Y":
                        planes[combinacion] = (45.5 + 3.8) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 2
                if (combinacion.count(5) + combinacion.count(6) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (45.5 + 0.5) * 4
                    elif letra == "Y":
                        planes[combinacion] = (45.5 + 2.55) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 3
                if (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (45.5 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (45.5 + 3.6) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 4
                if (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (45.5 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (45.5 + 5.3) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.5 + 0.8) * 4
                    elif letra == "Y":
                        planes[combinacion] = (48.5 + 2.55) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 2
                if (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.5 + 0.5) * 4
                    elif letra == "Y":
                        planes[combinacion] = (48.5 + 2.55) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 3
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.5 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (48.5 + 3.6) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 4
                if (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.5 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (48.5 + 5.3) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (55 + 0.8) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55 + 2.55) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (55 + 0.5) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55 + 2.55) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (55 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55 + 3.6) * 4
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (55 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55 + 5.3) * 4
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 1
                if (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.5 + 0.8) * 4
                    elif letra == "Y":
                        planes[combinacion] = (48.5 + 2.55) * 4
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.5 + 0.5) * 4
                    elif letra == "Y":
                        planes[combinacion] = (48.5 + 2.55) * 4
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.5 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (48.5 + 3.6) * 4
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.5 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (48.5 + 5.3) * 4
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (55 + 0.8) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55 + 2.55) * 4
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (55 + 0.5) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55 + 2.55) * 4
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0):
                    if letra == "X":
                        planes[combinacion] = (55 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55 + 3.6) * 4
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (55 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55 + 5.3) * 4
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (49.3 + 0.8) * 4
                    elif letra == "Y":
                        planes[combinacion] = (49.3 + 2.55) * 4
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (49.3 + 0.5) * 4
                    elif letra == "Y":
                        planes[combinacion] = (49.3 + 2.55) * 4
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 3
                if (combinacion.count(5) + combinacion.count(6) == 4):
                    if letra == "X":
                        planes[combinacion] = (49.3 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (49.3 + 3.6) * 4
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (49.3 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (49.3 + 5.3) * 4
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (55.8 + 0.8) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55.8 + 2.55) * 4
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0):
                    if letra == "X":
                        planes[combinacion] = (55.8 + 0.5) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55.8 + 2.55) * 4
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (55.8 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55.8 + 3.6) * 4
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (55.8 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (55.8 + 5.3) * 4
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (56.6 + 0.8) * 4
                    elif letra == "Y":
                        planes[combinacion] = (56.6 + 2.55) * 4
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (56.6 + 0.5) * 4
                    elif letra == "Y":
                        planes[combinacion] = (56.6 + 2.55) * 4
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (56.6 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (56.6 + 3.6) * 4
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(7) + combinacion.count(8) == 4):
                    if letra == "X":
                        planes[combinacion] = (56.6 + 0.7) * 4
                    elif letra == "Y":
                        planes[combinacion] = (56.6 + 5.3) * 4
            
            
        # 5 PUERTOS VISITADO        
        if combinacion.count(0) == 0:
            # SE ENTREGAN LAS 4 UNIDADES EN EL MISMO PUERTO 
            if visitados == 1:
                if (combinacion.count(1) > 0) or (combinacion.count(2) > 0):
                    planes[combinacion] = 36 * 5
                if (combinacion.count(3) > 0) or (combinacion.count(4) > 0):
                    planes[combinacion] = 36 * 5
                if (combinacion.count(5) > 0) or (combinacion.count(6) > 0):
                    planes[combinacion] = 38.6 * 5
                if (combinacion.count(7) > 0) or (combinacion.count(8) > 0):
                    planes[combinacion] = 44.6 * 5


            # SE ENTREGA EN DOS PUERTOS DISTINTOS
            
            if visitados == 2:
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1
                if (combinacion.count(1) + combinacion.count(2) == 5):
                    planes[combinacion] = 39.5 * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2
                if (combinacion.count(5) + combinacion.count(6) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    planes[combinacion] = 38.5 * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    planes[combinacion] = 41.5 * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    planes[combinacion] = 48 * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    planes[combinacion] = 41.5 * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    planes[combinacion] = 48 * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3
                if (combinacion.count(5) + combinacion.count(6) == 5):
                    planes[combinacion] = 42.1 * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    planes[combinacion] = 48.6 * 5
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4
                if (combinacion.count(7) + combinacion.count(8) == 5):
                    planes[combinacion] = 49.6 * 5


            # SE ENTREGA EN TRES PUERTOS DISTINTOS

            if visitados == 3:
                letra = subclasificacion(combinacion)
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 1 
                if (combinacion.count(1) + combinacion.count(2) == 5):
                    if letra == "X":
                        planes[combinacion] = (39.5 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (39.5 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 2 
                if (combinacion.count(5) + combinacion.count(6) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (39.5 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (39.5 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 3 
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (39.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (39.5 + 3.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 4 
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (39.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (39.5 + 4.75) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 1
                if (combinacion.count(5) + combinacion.count(6) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (38.5 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (38.5 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 2
                if (combinacion.count(5) + combinacion.count(6) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (38.5 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (38.5 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 3
                if (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (38.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (38.5 + 3.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 4
                if (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (38.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (38.5 + 4.75) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 2
                if (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 3
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 3.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 4
                if (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 4.75) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 3.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 4.75) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 1
                if (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 2.25) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 2.25) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 3.25) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 4.75) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 2.25) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 2.25) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 3.25) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 4.75) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (42.1 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (42.1 + 2.25) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (42.1 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (42.1 + 2.25) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 3
                if (combinacion.count(5) + combinacion.count(6) == 5):
                    if letra == "X":
                        planes[combinacion] = (42.1 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (42.1 + 3.25) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (42.1 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (42.1 + 4.75) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.6 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48.6 + 2.25) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.6 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48.6 + 2.25) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.6 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48.6 + 3.25) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.6 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48.6 + 4.75) * 5
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (49.6 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (49.6 + 2.25) * 5
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (49.6 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (49.6 + 2.25) * 5
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (49.6 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (49.6 + 3.25) * 5
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(7) + combinacion.count(8) == 5):
                    if letra == "X":
                        planes[combinacion] = (49.6 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (49.6 + 4.75) * 5


                # SE ENTREGA EN CUATRO PUERTOS DISTINTOS

            if visitados == 4:
                letra = subclasificacion(combinacion)
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 1 
                if (combinacion.count(1) + combinacion.count(2) == 5):
                    if letra == "X":
                        planes[combinacion] = (39.5 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (39.5 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 2 
                if (combinacion.count(5) + combinacion.count(6) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (39.5 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (39.5 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 3 
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (39.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (39.5 + 3.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 4 
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (39.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (39.5 + 4.75) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 1
                if (combinacion.count(5) + combinacion.count(6) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (38.5 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (38.5 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 2
                if (combinacion.count(5) + combinacion.count(6) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (38.5 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (38.5 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 3
                if (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (38.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (38.5 + 3.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 4
                if (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (38.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (38.5 + 4.75) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 2
                if (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 3
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 3.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 4
                if (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 4.75) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 3.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 4.75) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 1
                if (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 2.25) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 2.25) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 3.25) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 4.75) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 2.25) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 2.25) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 3.25) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 4.75) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (42.1 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (42.1 + 2.25) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (42.1 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (42.1 + 2.25) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 3
                if (combinacion.count(5) + combinacion.count(6) == 5):
                    if letra == "X":
                        planes[combinacion] = (42.1 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (42.1 + 3.25) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (42.1 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (42.1 + 4.75) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.6 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48.6 + 2.25) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.6 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48.6 + 2.25) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.6 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48.6 + 3.25) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.6 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48.6 + 4.75) * 5
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (49.6 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (49.6 + 2.25) * 5
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (49.6 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (49.6 + 2.25) * 5
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (49.6 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (49.6 + 3.25) * 5
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(7) + combinacion.count(8) == 5):
                    if letra == "X":
                        planes[combinacion] = (49.6 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (49.6 + 4.75) * 5


            # SE ENTREGA EN CINCO PUERTOS DISTINTOS

            if visitados == 5:
                letra = subclasificacion(combinacion)
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 1 
                if (combinacion.count(1) + combinacion.count(2) == 5):
                    if letra == "X":
                        planes[combinacion] = (39.5 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (39.5 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 2 
                if (combinacion.count(5) + combinacion.count(6) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (39.5 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (39.5 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 3 
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (39.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (39.5 + 3.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 1 + OTRO EN REGIÓN 4 
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (39.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (39.5 + 4.75) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 1
                if (combinacion.count(5) + combinacion.count(6) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (38.5 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (38.5 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 2
                if (combinacion.count(5) + combinacion.count(6) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (38.5 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (38.5 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 3
                if (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (38.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (38.5 + 3.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 2 + OTRO EN REGIÓN 4
                if (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (38.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (38.5 + 4.75) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 2
                if (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 3
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 3.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 4
                if (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 4.75) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 2.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 3.25) * 5
                # EN REGIÓN 1 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 4.75) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 1
                if (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 2.25) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 2.25) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 3.25) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0):
                    if letra == "X":
                        planes[combinacion] = (41.5 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (41.5 + 4.75) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 2.25) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 2.25) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 3.25) * 5
                # EN REGIÓN 2 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (48 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48 + 4.75) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (42.1 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (42.1 + 2.25) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(7) + combinacion.count(8) == 0):
                    if letra == "X":
                        planes[combinacion] = (42.1 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (42.1 + 2.25) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 3
                if (combinacion.count(5) + combinacion.count(6) == 5):
                    if letra == "X":
                        planes[combinacion] = (42.1 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (42.1 + 3.25) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 3 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (42.1 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (42.1 + 4.75) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.6 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48.6 + 2.25) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.6 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48.6 + 2.25) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.6 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48.6 + 3.25) * 5
                # EN REGIÓN 3 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (48.6 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (48.6 + 4.75) * 5
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 1
                if (combinacion.count(3) + combinacion.count(4) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (49.6 + 1.3) * 5
                    elif letra == "Y":
                        planes[combinacion] = (49.6 + 2.25) * 5
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 2
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(5) + combinacion.count(6) == 0):
                    if letra == "X":
                        planes[combinacion] = (49.6 + 0.7) * 5
                    elif letra == "Y":
                        planes[combinacion] = (49.6 + 2.25) * 5
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 3
                if (combinacion.count(1) + combinacion.count(2) == 0) and (combinacion.count(3) + combinacion.count(4) == 0):
                    if letra == "X":
                        planes[combinacion] = (49.6 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (49.6 + 3.25) * 5
                # EN REGIÓN 4 Y OTRA EN REGIÓN 4 + OTRO EN REGIÓN 4
                if (combinacion.count(7) + combinacion.count(8) == 5):
                    if letra == "X":
                        planes[combinacion] = (49.6 + 1.1) * 5
                    elif letra == "Y":
                        planes[combinacion] = (49.6 + 4.75) * 5
            
                   

    return planes



print(len(crear_plan(combinaciones_puertos)))

planes_empresa1 = crear_plan(combinaciones_puertos)
