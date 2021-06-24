
import pandas as pd
from gurobipy import * 
import numpy as np 
from Parametros import *
from planes_empresa_1 import * 
from planes_empresa_2 import * 
from planes_empresa_3 import * 
from planes_empresa_4 import * 


# creamos el modelo
m = Model("planificacion")
m.reset()

# sets

meses = [str(i) for i in range(1,13)]
contratos = [str(i) for i in range(1,5)]
clientes = [str(i) for i in range(1,26)]
puertos = [str(i) for i in range(1,9)]
q1 = ['1','2','3']
q2 = ['4','5','6']
q3 = ['7','8','9']
q4 = ['10','11','12']


###

planes = []

planes1 = [str(i) for i in planes_empresa1.keys()]
planes2 = [str(i) for i in planes_empresa2.keys()]
planes3 = [str(i) for i in planes_empresa3.keys()]
planes4 = [str(i) for i in planes_empresa4.keys()]

i = 0
for plan in planes_empresa2.keys():
    i+=1
    if not str(plan) in planes:
        planes.append(str(plan))
        if i == 50:
            break
    
###
"""
VARIABLES
"""

# variables

x1 = m.addVars(meses,'1',planes1, vtype=GRB.BINARY, name="x1")
x2 = m.addVars(meses,'2',planes2, vtype=GRB.BINARY, name="x2")
x3 = m.addVars(meses,'3',planes3, vtype=GRB.BINARY, name="x3")
x4 = m.addVars(meses,'4',planes4, vtype=GRB.BINARY, name="x4")
y = m.addVars(meses,puertos, vtype=GRB.CONTINUOUS, lb = 0, name="y")            
b = m.addVars(meses,puertos, vtype=GRB.INTEGER, lb = 0, name="b")
q = m.addVars(meses,clientes, vtype=GRB.INTEGER, lb = 0, name="q")
s = m.addVars(meses, vtype=GRB.INTEGER, lb = 0, name="s")

"""
FUNCION OBJETIVO
"""

# funcion objetivo

m.setObjective(quicksum(C_spot*y[mes,puerto] for mes in meses for puerto in puertos) + quicksum(C_4_p[plan]*U1_4_p[plan]*x4[mes,'4',plan] for mes in meses for plan in planes4) + quicksum(C_3_p[plan]*U1_3_p[plan]*x3[mes,'3',plan] for mes in meses for plan in planes3) + quicksum(C_2_p[plan]*U1_2_p[plan]*x2[mes,'2',plan] for mes in meses for plan in planes2) + quicksum(C_1_p[plan]*U1_1_p[plan]*x1[mes,'1',plan] for mes in meses for plan in planes1), GRB.MINIMIZE)



"""
RESTRICCIONES PARA CONTRATOS
"""
# restricción 1
for mes in meses:
    m.addConstr(quicksum(x1[mes,'1',plan] for plan in planes1)<=1)
    m.addConstr(quicksum(x2[mes,'2',plan] for plan in planes2)<=1)
    m.addConstr(quicksum(x3[mes,'3',plan] for plan in planes3)<=1)
    m.addConstr(quicksum(x4[mes,'4',plan] for plan in planes4)<=1)

# restriccion 2
m.addConstr( CMIN_M_f[1] <= quicksum(EU*U1_1_p[str(plan)]*x1[mes,'1',plan] for mes in meses for plan in planes1))
m.addConstr( CMAX_M_F[1] >= quicksum(EU*U1_1_p[str(plan)]*x1[mes,'1',plan] for mes in meses for plan in planes1))

m.addConstr( CMIN_M_f[2] <= quicksum(EU*U1_2_p[str(plan)]*x2[mes,'2',plan] for mes in meses for plan in planes2))
m.addConstr( CMAX_M_F[2] >= quicksum(EU*U1_2_p[str(plan)]*x2[mes,'2',plan] for mes in meses for plan in planes2))

m.addConstr( CMIN_M_f[3] <= quicksum(EU*U1_3_p[str(plan)]*x3[mes,'3',plan] for mes in meses for plan in planes3))
m.addConstr( CMAX_M_F[3] >= quicksum(EU*U1_3_p[str(plan)]*x3[mes,'3',plan] for mes in meses for plan in planes3))

m.addConstr( CMIN_M_f[4] <= quicksum(EU*U1_4_p[str(plan)]*x4[mes,'4',plan] for mes in meses for plan in planes4))
m.addConstr( CMAX_M_F[4] >= quicksum(EU*U1_4_p[str(plan)]*x4[mes,'4',plan] for mes in meses for plan in planes4))

# restriccion 3
for mes in meses:
    for puerto in puertos:
        m.addConstr( b[mes,puerto] == quicksum(q[mes,cliente] for cliente in clientes))
        

# restriccion 4
for mes in meses:
    for puerto in puertos:
        m.addConstr(b[mes,puerto] == quicksum(U2_4_p_d[str((str(plan),str(puerto)))]*x4[mes,'4',plan] for plan in planes4) + quicksum(U2_3_p_d[str((str(plan),str(puerto)))]*x3[mes,'3',plan] for plan in planes3) + quicksum(U2_2_p_d[str((str(plan),str(puerto)))]*x2[mes,'2',plan] for plan in planes2) + quicksum(U2_1_p_d[str((str(plan),str(puerto)))]*x1[mes,'1',plan] for plan in planes1) + y[mes,puerto])


"""
RESTRICCIONES PARA CLIENTES
"""

#restriccion 5  
"""
con el primero se debe comentar la restricción 4
"""
#m.addConstrs(quicksum(q[mes,cliente]*EU for mes in meses) == R_M_c[int(cliente)] for cliente in clientes)
m.addConstrs(quicksum(q[mes,cliente]*EU for mes in meses) >= R_M_c[int(cliente)] for cliente in clientes)

# restriccion 6
for mes in meses:
    for cliente in clientes:
         m.addConstr(EU*q[mes,cliente] <= MAX_m_c[int(cliente)])                      
          
# restriccion 7
for cliente in clientes:
    m.addConstr( MINQU_j_c[int(cliente)] <= quicksum(EU*q[mes,cliente] for mes in q1))
    m.addConstr( MAXQU_j_c[int(cliente)] >= quicksum(EU*q[mes,cliente] for mes in q1))
    m.addConstr( MINQU_j_c[int(cliente)] <= quicksum(EU*q[mes,cliente] for mes in q2))
    m.addConstr( MAXQU_j_c[int(cliente)] >= quicksum(EU*q[mes,cliente] for mes in q2))
    m.addConstr( MINQU_j_c[int(cliente)] <= quicksum(EU*q[mes,cliente] for mes in q3))
    m.addConstr( MAXQU_j_c[int(cliente)] >= quicksum(EU*q[mes,cliente] for mes in q3))
    m.addConstr( MINQU_j_c[int(cliente)] <= quicksum(EU*q[mes,cliente] for mes in q4))
    m.addConstr( MAXQU_j_c[int(cliente)] >= quicksum(EU*q[mes,cliente] for mes in q4))

"""
RESTRICCIONES DE PRODUCCION
"""

# restriccion 8
for mes1 in meses:
    anteriores = []
    for i in meses:
        anteriores.append(i)
        if i == mes1:
            break
    m.addConstr(SS <= I_0M + quicksum(P_m[int(mes)] for mes in anteriores) - quicksum( EU*q[mes,cliente] for mes in anteriores for cliente in clientes) - quicksum(EU*s[mes] for mes in anteriores))

# restriccion 9
m.addConstr( quicksum(s[mes] for mes in meses) == (I_0M + quicksum(P_m[int(mes)] for mes in anteriores) - quicksum(R_M_c[int(cliente)] for cliente in clientes) - SS)/EU)
 
# restriccion 10
for mes in meses:
    m.addConstr( MINEUIM_m[int(mes)] <= quicksum(q[mes,cliente] for cliente in clientes) + s[mes])
    m.addConstr( MAXEUI_m[int(mes)] >= quicksum(q[mes,cliente] for cliente in clientes) + s[mes])
                   
"""
OPTIMIZACION Y RESULTADOS
"""

m.update()
m.optimize()
obj = m.getObjective()
var = m.getVars()
m.printAttr('X')

x1 = list()
x2 = list()
x3 = list()
x4 = list()
y = list()
b = list()
q = list()
s = list()

dic = {'nombre': [],'mes': [],'contrato': [],'plan': [],'cliente': [],'puerto': [],'valor':[]}

for v in m.getVars():
    nombre = str(v.varName)
    valor = str(v.x)
    if 'x1' in nombre:
        x1.append([nombre,valor])
    if 'x2' in nombre:
        x2.append([nombre,valor])
    if 'x3' in nombre:
        x3.append([nombre,valor])
    if 'x4' in nombre:
        x4.append([nombre,valor])
    if 'y' in nombre:
        y.append([nombre,valor])
    if 'b' in nombre:
        b.append([nombre,valor])
    if 'q' in nombre:
        q.append([nombre,valor])
    if 's' in nombre:
        s.append([nombre,valor])
  
    
for i in x1:
    lista = []
    nombre = i[0][2:]
    parcial = []
    for c in nombre:
        if not c==',':
            parcial.append(c)
        if c==',' or ']':
            lista.append(parcial)
            parcial=[]
    print(lista)
    dic['nombre'].append(i[0])
    #dic['mes'].append()
    #dic['contrato'].append()
    #dic['plan'].append()
    #dic['cliente'].append()
    #dic['puerto'].append()
    dic['valor'].append(i[1])
    
    
    


