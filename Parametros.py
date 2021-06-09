#!/usr/bin/env python
# coding: utf-8

# In[5]:


from numpy import *
from pandas import *
from planes_empresa_2 import planes_empresa2
from planes_empresa_3 import planes_empresa3
from planes_empresa_4 import planes_empresa4
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

################################
# Clase Clientes
class Cliente:
  def __init__(self, _id, toneladas, max_m, min_qu, max_qu, puerto):
      self.id = _id
      self.toneladas = toneladas
      self.max_m  = max_m
      self.min_qu = min_qu
      self.max_qu = max_qu
      self.puerto = puerto
# Instancias de clientes
clientes = {1:  Cliente(1, 110000, 30000, 20000, 40000, 1),
            2:  Cliente(2, 70000, 30000, 10000, 40000, 2),
            3:  Cliente(3, 20000, 20000, 0, 20000, 3),
            4:  Cliente(4, 40000, 20000, 0, 30000, 4),
            5:  Cliente(5, 40000, 20000, 0, 40000, 5),
            6:  Cliente(6, 40000, 20000, 0, 40000, 2),
            7:  Cliente(7, 30000, 10000, 0, 10000, 6),
            8:  Cliente(8, 40000, 20000, 0, 10000, 4),
            9:  Cliente(9, 30000, 10000, 0, 20000, 5),
            10: Cliente(10, 40000, 20000, 0, 30000, 1),
            11: Cliente(11, 30000, 10000, 0, 20000, 5),
            12: Cliente(12, 40000, 10000, 0, 20000, 4),
            13: Cliente(13, 30000, 10000, 0, 20000, 8),
            14: Cliente(14, 20000, 20000, 0, 10000, 6),
            15: Cliente(15, 30000, 20000, 0, 20000, 4),
            16: Cliente(16, 40000, 20000, 0, 20000, 1),
            17: Cliente(17, 40000, 10000, 0, 20000, 3),
            18: Cliente(18, 40000, 20000, 0, 20000, 5),
            19: Cliente(19, 30000, 10000, 0, 20000, 7),
            20: Cliente(20, 50000, 40000, 10000, 20000, 2),
            21: Cliente(21, 40000, 10000, 10000, 20000, 7),
            22: Cliente(22, 40000, 20000, 0, 20000, 3),
            23: Cliente(23, 40000, 10000, 0, 20000, 2),
            24: Cliente(24, 30000, 10000, 0, 20000, 8),
            25: Cliente(25, 30000, 10000, 0, 20000, 1)
            }
#############################################################
#############################################################

############################################################
############ PARAMETROS ENUMERADOS 
###########################################################


### 1 ###
#costo de trasladar una tonelada en el COA f para el plan p
#FALTA AGREGAR EMPRESA1
C_f_p = {"empresa2": planes_empresa2, "empresa3": planes_empresa3, "empresa4": planes_empresa4}

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

### 8, 9, 10 y 11  ### 
# Toneladas requeridas por el cliente c en el período M (a lo largo de los 12 meses)
R_M_c= {}
# Maxima cantidad de toneladas que se pueden transportar a c en m
MAX_m_c = {}
# Mínima cantidad de toneladas para el cliente c en trimestre j
MINQU_j_c = {}
# Maxima cantidad de toneladas que se pueden transportar a c en m
MAXQU_j_c = {}

for cliente in clientes:
    R_M_c[cliente] = clientes[cliente].toneladas
    MAX_m_c[cliente] = clientes[cliente].max_m
    table_max =[]
    table_min =[]
    for trimestre in range(1,5):
        table_min.append([trimestre, clientes[cliente].min_qu])
        table_max.append([trimestre, clientes[cliente].max_qu])
    MINQU_j_c[cliente] = table_min
    MAXQU_j_c[cliente] = table_max

#print(MINQU_j_c)
#print(MAXQU_j_c)

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




