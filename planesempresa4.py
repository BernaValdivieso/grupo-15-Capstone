# -*- coding: utf-8 -*-
"""
Created on Wed May 12 10:50:11 2021

@author: merca
"""

import time 

t1 = time.time()

# DISTINTAS COMBINACIONES DE PUERTOS QUE PUEDE HACER UN PLAN DE LA EMPRESA 4
    
combinaciones_1 = [(a,0,0,0) for a in range(1,9)]
combinaciones_2 = [(a,b,0,0) for a in range(1,9) for b in range(1,9)]
combinaciones_3 = [(a,b,c,0) for a in range(1,9) for b in range(1,9) for c in range(1,9)]
combinaciones_4 = [(a,b,c,d) for a in range(1,9) for b in range(1,9) for c in range(1,9) for d in range(1,9)]  

combinaciones_puertos = combinaciones_1+combinaciones_2+combinaciones_3+combinaciones_4

#FUNCION QUE EVITA REPITENCIAS DE COMBINACIONES
def sin_repetir(combinaciones_puertos):
    lista= list()
    lista2 = list()
    for combinacion in combinaciones_puertos:
        combinacion = sorted(combinacion)
        if not combinacion in lista:
            lista.append(combinacion)
    for item in lista:
        tupla = (item[0],item[1],item[2],item[3])
        lista2.append(tupla)
    return lista2

combinaciones_puertos = sin_repetir(combinaciones_puertos)

# FUNCION QUE CUENTA LA CANTIDAD DE PUERTOS VISITADOS
def puertos_visitados(combinacion):
    lista = []
    for puerto in combinacion:
        if not puerto in lista and puerto!=0:
            lista.append(puerto)
    return len(lista)
   
# FUNCION QUE CREA UN DICCIONARIO DE LOS DISTINTOS PLANES
# EL FORMATO ES (PUERTOS VISITADOS):COSTO
def crear_plan(combinaciones_puertos):
    
    planes = dict()
    
    for combinacion in combinaciones_puertos:
        
        # SE DEFINE LA CANTIDAD DE PUERTOS VISITADOS Y EL ADICIONAL 
        visitados = puertos_visitados(combinacion)
        adicional = 0
        if combinacion.count(7) + combinacion.count(8) > 0:
            adicional = 3.5
        
        # 1 UNIDADES
        if combinacion.count(0)==3:
            planes[combinacion]= 51.5 + adicional
            
        # 2 UNIDADES
        if combinacion.count(0)==2:
            if visitados==1:
                planes[combinacion]=(45 + adicional)*2
            if visitados==2:
                planes[combinacion]=(45 + 3.5 + adicional)*2
    
        # 3 UNIDADES
        if combinacion.count(0)==1:
            if visitados==1:
                planes[combinacion]=(44 + adicional)*3
            if visitados==2:
                planes[combinacion]=(44 + 3.5  + adicional)*3
            if visitados==3:
                planes[combinacion]=(44 + 4  + adicional)*3
        
        # 4 UNIDADES       
        if combinacion.count(0)==0:
            if visitados==1:
                planes[combinacion]=(43 + adicional)*4
            if visitados==2:
                planes[combinacion]=(43 + 3.5 + adicional)*4
            if visitados==3:
                planes[combinacion]=(43 + 4 + adicional)*4
            if visitados==4:
                planes[combinacion]=(43 + 4.5 + adicional)*4

    return planes
    
print(crear_plan(combinaciones_puertos))
print("")
print("Hay "+str(len(crear_plan(combinaciones_puertos)))+" planes")
t2 = time.time()
print("Tiempo en correr: "+str(t2-t1)+" segundos")
