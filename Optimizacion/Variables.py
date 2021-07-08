#!/usr/bin/env python
# coding: utf-8

# # Variables de decisión

# In[12]:
from planes_empresa_1 import planes_empresa1
from planes_empresa_2 import planes_empresa2
from planes_empresa_3 import planes_empresa3
from planes_empresa_4 import planes_empresa4

aux_list1 = []
for key in planes_empresa1.keys():
    aux_list1.append(key)

aux_list2 = []
for key in planes_empresa2.keys():
    aux_list2.append(key)

aux_list3 = []
for key in planes_empresa3.keys():
    aux_list3.append(key)

aux_list4 = []
for key in planes_empresa4.keys():
    aux_list4.append(key)
# X_m_f_p 
# si en el mes m en la región z el contrato f realiza el plan p

meses = [i for i in range(1,13)]
planes_contrato_1 = {'contrato': 1, 'planes': aux_list1}
planes_contrato_2 = {'contrato': 2, 'planes': aux_list2}
planes_contrato_3 = {'contrato': 3, 'planes': aux_list3}
planes_contrato_4 = {'contrato': 4, 'planes': aux_list4}

planes_contratos = [planes_contrato_1, planes_contrato_2, planes_contrato_3, planes_contrato_4]
planes = []
for plan in planes_contratos:
    for i in plan['planes']:
        if i not in planes:
            planes.append(i)

#planes_contratos = [planes_contrato_1]

def generador_de_x(meses,planes_contratos):
    combinaciones = []
    for contrato in planes_contratos:
        for mes in meses:
            for plan in contrato['planes']:
                #combinaciones.append({'mes':mes,'contrato':contrato['contrato'],'plan':plan})
                combinaciones.append((mes, contrato['contrato'], str(plan)))
    return combinaciones
            
X_m_f_p = generador_de_x(meses,planes_contratos)
#print(X_m_f_p)

# In[17]:


# Y_m_d 
# cargas a enviar por transporte SPOT en el mes m al puerto d 

meses = [i for i in range(1,13)]
puertos = [i for i in range(1,9)]
potenciales_cargas_spot = [i for i in range(1,6)] ### SE DEBE DEFINIR BIEN 

def generador_de_y(meses,puertos,potenciales_cargas_spot):
    combinaciones = []
    for mes in meses:
        for puerto in puertos:
            for carga in potenciales_cargas_spot:
                #combinaciones.append({'mes':mes,'puerto':puerto,'carga':carga})
                if (mes, puerto) not in combinaciones:
                    combinaciones.append((mes, puerto))
    return combinaciones

Y_m_d  = generador_de_y(meses,puertos,potenciales_cargas_spot)


# In[20]:


# B_m_d
# cargas a enviar en el mes m al puerto d

meses = [i for i in range(1,13)]
puertos = [i for i in range(1,9)]
cargas = [i for i in range(1,100)] ##### SE DEBE DEFINIR BIEN 

def generador_de_y(meses,puertos,cargas):
    combinaciones = []
    for mes in meses:
        for puerto in puertos:
            if (mes, puerto) not in combinaciones:
                combinaciones.append((mes, puerto))
    return combinaciones

B_m_d = generador_de_y(meses,puertos,cargas)


# In[26]:


# Q_m_c
# cargas transportadas en el mes m al cliente c

clientes = [i for i in range(1,4)]
cargas = [i for i in range(0,10)]
meses = [i for i in range(1,13)]

def generador_de_q(clientes,cargas,meses):
    combinaciones = []
    for mes in meses:
        for cliente in clientes:
            for carga in cargas:
                #combinaciones.append({'mes':mes,'cliente':cliente,'carga':carga})
                if (mes, cliente) not in combinaciones:
                    combinaciones.append((mes, cliente))
    return combinaciones

Q_m_c = generador_de_q(clientes,cargas,meses)


# In[22]:


# S_m
# potenciales cargas por ventas cortas en el mes m

minimo = 1 ############ SE DEBEN DEFINIR BIEN 
maximo = 13
S_m = [i for i in range(minimo,maximo)]
#print(S_m)

