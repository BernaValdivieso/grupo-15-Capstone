
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

# FUNCION QUE RETORNA PUERTOS VISITADOS (NO LA CANTIDAD)
def puertos_visitados(combinacion):
    lista = []
    for puerto in combinacion:
        if not puerto in lista and puerto != 0:
            lista.append(puerto)
    return lista

def crear_plan(combinaciones_puertos):
    
    planes = dict()
    
    for combinacion in combinaciones_puertos:
        
        # SE DEFINE LA CANTIDAD DE PUERTOS VISITADOS Y EL ADICIONAL 
        visitados = puertos_visitados(combinacion) # FUNCION QUE RETORNA PUERTOS VISITADOS (NO LA CANTIDAD)
                
        # 1 PUERTO VISITADO = 1 UNIDAD A DESCARGAR
        if combinacion.count(0) == 4:
            if 3 in visitados or 4 in visitados:
                planes[combinacion] = (61.5 -1)
            elif 7 in visitados or 8 in visitados:
                planes[combinacion] = 61.5 + 3.5
            else:
                planes[combinacion] = 61.5
            
        # 2 PUERTOS VISITADO = 2 UNIDADES A DESCARGAR
        if combinacion.count(0) == 3:
            if len(visitados) == 1:
                if 3 in visitados or 4 in visitados:
                    planes[combinacion] = (58.5 -1)*2
                elif 7 in visitados or 8 in visitados:
                    planes[combinacion] = (58.5 + 3.5)*2
                else:
                    planes[combinacion] = (58.5)*2
                
            elif len(visitados) == 2:
                if 3 in visitados and 4 in visitados:
                    planes[combinacion] = (58.5 -1 + 1)*2
                elif 7 in visitados or 8 in visitados:
                    planes[combinacion] = (58.5 + 3.5 + 1)*2
                else:
                    planes[combinacion] = (58.5 + 1)*2

                
                
    
        # 3 PUERTOS VISITADO = 3 UNIDADES A DESCARGAR
        if combinacion.count(0) == 2:
            if len(visitados) == 1:
                if 3 in visitados or 4 in visitados:
                    planes[combinacion] = (53.5 -1)*3
                elif 7 in visitados or 8 in visitados:
                    planes[combinacion] = (53.5 + 3.5)*3
                else:
                    planes[combinacion] = (53.5)*3
                
            elif len(visitados) == 2:
                if 3 in visitados and 4 in visitados:
                    planes[combinacion] = (53.5 -1 + 1)*3
                elif 7 in visitados or 8 in visitados:
                    planes[combinacion] = (53.5 + 3.5 + 1)*3
                else:
                    planes[combinacion] = (53.5 + 1)*3
            else:
                if 7 in visitados or 8 in visitados:
                    planes[combinacion] = (53.5 + 3.5 + 1)*3
                else:
                    planes[combinacion] = (53.5 + 1)*3
        # 4 PUERTOS VISITADO  = 4 UNIDADES A DESCARGAR      
        if combinacion.count(0) == 1:
            if len(visitados) == 1:
                if 3 in visitados or 4 in visitados:
                    planes[combinacion] = (53 -1)*4
                elif 7 in visitados or 8 in visitados:
                    planes[combinacion] = (53 + 3.5)*4
                else:
                    planes[combinacion] = (53)*4
                
            elif len(visitados) == 2:
                if 3 in visitados and 4 in visitados:
                    planes[combinacion] = (53 -1 + 1)*4
                elif 7 in visitados or 8 in visitados:
                    planes[combinacion] = (53 + 3.5 + 1)*4
                else:
                    planes[combinacion] = (53 + 1)*4
            else:
                if 7 in visitados or 8 in visitados:
                    planes[combinacion] = (53 + 3.5 + 1)*4
                else:
                    planes[combinacion] = (53 + 1)*4

        # 5 PUERTOS VISITADO = 5 UNIDADES A DESCARGAR       
        if combinacion.count(0) == 0:
            if len(visitados) == 1:
                if 3 in visitados or 4 in visitados:
                    planes[combinacion] = (48.5 -1)*5
                elif 7 in visitados or 8 in visitados:
                    planes[combinacion] = (48.5 + 3.5)*5
                else:
                    planes[combinacion] = (48.5)*4
                
            elif len(visitados) == 2:
                if 3 in visitados and 4 in visitados:
                    planes[combinacion] = (48.5 -1 + 1)*5
                elif 7 in visitados or 8 in visitados:
                    planes[combinacion] = (48.5 + 3.5 + 1)*5
                else:
                    planes[combinacion] = (48.5 + 1)*5
            else:
                if 7 in visitados or 8 in visitados:
                    planes[combinacion] = (48.5 + 3.5 + 1)*5
                else:
                    planes[combinacion] = (48.5 + 1)*5

    return planes

print(crear_plan(combinaciones_puertos))

planes_empresa2 = crear_plan(combinaciones_puertos)