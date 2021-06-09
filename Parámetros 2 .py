#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# C_spot
# costo de trasladar una tonelada en el spot

C_spot = 


# In[6]:


# U1_f_p 
# cargas a transportar para el plan p en el cotrato f

planes_contrato_1 = {'contrato': 1, 'planes': [(1,0),(2,1)]}
#planes_contrato_2 = {'contrato': 2, 'planes': }
#planes_contrato_3 = {'contrato': 3, 'planes': }
#planes_contrato_4 = {'contrato': 4, 'planes': }

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

U1_f_p = generador_de_u1(planes_contratos)
U1_f_p


# In[5]:


# U2_f_p_d
# cargas del puerto d para el plan p en contrato f 

planes_contrato_1 = {'contrato': 1, 'planes': [(1,0),(2,1)]}
#planes_contrato_2 = {'contrato': 2, 'planes': }
#planes_contrato_3 = {'contrato': 3, 'planes': }
#planes_contrato_4 = {'contrato': 4, 'planes': }

#planes_contratos = [planes_contrato_1, planes_contrato_2, planes_contrato_3, planes_contrato_4]
planes_contratos = [planes_contrato_1]
puertos = [i for i in range(1,9)]

def generador_de_u2(planes_contratos,puertos):
    combinaciones = []
    for contrato in planes_contratos:
        for plan in contrato['planes']:
            for puerto in puertos:
                cargas = plan.count(puerto)
                combinaciones.append(({'contrato':contrato['contrato'],'plan':plan,'puerto':puerto,'carga':cargas}))
    return combinaciones

U2_f_p_d = generador_de_u2(planes_contratos,puertos)
U2_f_p_d


# In[ ]:



# CMIN_M_f 
# Cantidad míınima de toneladas en el contrato f en M.

CMIN_M_f = [{'contrato':1,'minimo':270000},{'contrato':2:'minimo':220000},{'contrato':3:'minimo':180000},{'contrato':4:'minimo':170000}]

# CMAX_M_F
# Cantidad maxima de toneladas en el contrato  f en M
CMAX_M_F = [{'contrato':1,'maximo':300000},{'contrato':2:'maximo':280000},{'contrato':3:'maximo':220000},{'contrato':4:'maximo':210000}]

