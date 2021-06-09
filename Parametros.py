#!/usr/bin/env python
# coding: utf-8

# In[5]:


from numpy import *
from pandas import *

"""
PARAMETROS
"""

###################################################################################
### FUNCIONES Y CONJUNTOS NECESARIOS PARA LA DEFINICION DE LOS PARAMETROS
#################################################################################

planes_contrato_1 = {'contrato': 1, 'planes': [(1,0),(2,1)]}
#planes_contrato_2 = {'contrato': 2, 'planes': }
#planes_contrato_3 = {'contrato': 3, 'planes': }
#planes_contrato_4 = {'contrato': 4, 'planes': }

puertos = [i for i in range(1,9)]

#planes_contratos = [planes_contrato_1, planes_contrato_2, planes_contrato_3, planes_contrato_4]
planes_contratos = [planes_contrato_1]

def generador_de_u1(planes_contratos):
    combinaciones = []
    for contrato in planes_contratos:
        for plan in contrato['planes']:
            conteo_cargas = 0
            for n in plan:
                if not n == 0:
                    conteo_cargas+=1
            combinaciones.append({'contrato':contrato['contrato'],'plan':plan,'carga':conteo_cargas})
    return combinaciones

def generador_de_u2(planes_contratos,puertos):
    combinaciones = []
    for contrato in planes_contratos:
        for plan in contrato['planes']:
            for puerto in puertos:
                cargas = plan.count(puerto)
                combinaciones.append(({'contrato':contrato['contrato'],'plan':plan,'puerto':puerto,'carga':cargas}))
    return combinaciones


#############################################################
#############################################################

############################################################
############ PARAMETROS ENUMERADOS 
###########################################################


### 1 ###

### 2 ### 

# C_spot
# costo de trasladar una tonelada en el spot
C_spot = 65

### 3 ### 

# U1_f_p 
# cargas a transportar para el plan p en el cotrato f
U1_f_p = generador_de_u1(planes_contratos)

### 4 ### 

# U2_f_p_d
# cargas del puerto d para el plan p en contrato f 
U2_f_p_d = generador_de_u2(planes_contratos,puertos)

### 5 ### 

# EU
EU = 10000

### 6 ###

# CMIN_M_f 
# Cantidad míınima de toneladas en el contrato f en M.

CMIN_M_f = {1:270000 ,2:220000,3:180000,4:170000}

### 7 ###

# CMAX_M_F
# Cantidad maxima de toneladas en el contrato  f en M
CMAX_M_F = {1:300000,2:280000,3:220000,4:210000}

### 8 ### 

### 9 ### 

### 10 ### 

### 11 ### 

### 12 ### 

# Produccion esperada mensual 
P_m ={1: 110000,2: 90000,3: 110000,4: 100000,5: 90000, 6: 100000,7: 120000,8: 110000,9: 110000,10: 120000,11: 100000,12: 100000}

### 13 ### 

# Inventario inicial 
I_0M = 30000

### 14 ### 

#Inventario miniimo a retirar de bodega en m
MINEUIM_m = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}

### 15 ### 

#Inventario maximo a retirar de bodega en m
MAXEUI_m = {1:10000000,2:10000000,3:10000000,4:10000000,5:10000000,6:10000000,7:10000000,8:10000000,9:10000000,10:10000000,11:10000000,12:10000000}

### 16 ### 

# Inventario de seguridad, puede ser desde 0 hasta 50000
SS = 10000


# In[ ]:




