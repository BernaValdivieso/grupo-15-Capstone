
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

cp = {'1':[1,10,16,25],'2':[2,6,20,23],'3':[3,17,22],'4':[4,8,12,15],'5':[5,9,11,18],'6':[7,14],'7':[19,21],'8':[13,24]}


planes1 = [str(i) for i in planes_empresa1.keys()]
planes2 = [str(i) for i in planes_empresa2.keys()]
planes3 = [str(i) for i in planes_empresa3.keys()]
planes4 = [str(i) for i in planes_empresa4.keys()]


###
"""
VARIABLES
"""

# variables

x1 = m.addVars(meses,'1',planes1, vtype=GRB.BINARY, name="x1")
x2 = m.addVars(meses,'2',planes2, vtype=GRB.BINARY, name="x2")
x3 = m.addVars(meses,'3',planes3, vtype=GRB.BINARY, name="x3")
x4 = m.addVars(meses,'4',planes4, vtype=GRB.BINARY, name="x4")
y = m.addVars(meses,puertos, vtype=GRB.INTEGER, lb = 0, name="y")            
b = m.addVars(meses,puertos, vtype=GRB.INTEGER, lb = 0, name="b")
q = m.addVars(meses,clientes, vtype=GRB.INTEGER, lb = 0, name="q")
s = m.addVars(meses, vtype=GRB.INTEGER, lb = 0, name="s")

"""
FUNCION OBJETIVO
"""

# funcion objetivo

m.setObjective(quicksum(C_spot*y[mes,puerto] for mes in meses for puerto in puertos) + quicksum(C_4_p[plan]*U1_4_p[plan]*x4[mes,'4',plan] for mes in meses for plan in planes4) + quicksum(C_3_p[plan]*U1_3_p[plan]*x3[mes,'3',plan] for mes in meses for plan in planes3) + quicksum(C_2_p[plan]*U1_2_p[plan]*x2[mes,'2',plan] for mes in meses for plan in planes2) + quicksum(C_1_p[plan]*U1_1_p[plan]*x1[mes,'1',plan] for mes in meses for plan in planes1), GRB.MINIMIZE)

# opción sin spot
#m.setObjective(quicksum(C_4_p[plan]*U1_4_p[plan]*x4[mes,'4',plan] for mes in meses for plan in planes4) + quicksum(C_3_p[plan]*U1_3_p[plan]*x3[mes,'3',plan] for mes in meses for plan in planes3) + quicksum(C_2_p[plan]*U1_2_p[plan]*x2[mes,'2',plan] for mes in meses for plan in planes2) + quicksum(C_1_p[plan]*U1_1_p[plan]*x1[mes,'1',plan] for mes in meses for plan in planes1), GRB.MINIMIZE)




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
        m.addConstr( b[mes,puerto] == quicksum(q[mes,str(cliente)] for cliente in cp[str(puerto)]))

      
# restriccion 4
for mes in meses:
    for puerto in puertos:
        #m.addConstr(b[mes,puerto] == quicksum(U2_4_p_d[str((str(plan),str(puerto)))]*x4[mes,'4',plan] for plan in planes4) + quicksum(U2_3_p_d[str((str(plan),str(puerto)))]*x3[mes,'3',plan] for plan in planes3) + quicksum(U2_2_p_d[str((str(plan),str(puerto)))]*x2[mes,'2',plan] for plan in planes2) + quicksum(U2_1_p_d[str((str(plan),str(puerto)))]*x1[mes,'1',plan] for plan in planes1) + y[mes,puerto])
        # sin spots
        m.addConstr(b[mes,puerto] == quicksum(U2_4_p_d[str((str(plan),str(puerto)))]*x4[mes,'4',plan] for plan in planes4) + quicksum(U2_3_p_d[str((str(plan),str(puerto)))]*x3[mes,'3',plan] for plan in planes3) + quicksum(U2_2_p_d[str((str(plan),str(puerto)))]*x2[mes,'2',plan] for plan in planes2) + quicksum(U2_1_p_d[str((str(plan),str(puerto)))]*x1[mes,'1',plan] for plan in planes1))
       
"""
RESTRICCIONES PARA CLIENTES
"""

#restriccion 5  
m.addConstrs(quicksum(q[mes,cliente]*EU for mes in meses) == R_M_c[int(cliente)] for cliente in clientes)

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
m.addConstr( quicksum(s[mes] for mes in meses) == ((I_0M + quicksum(P_m[int(mes)] for mes in meses) - quicksum(R_M_c[int(cliente)] for cliente in clientes) - SS))/EU)
 
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


def funcion_costo(empresa, plan):
    if empresa == 1:
        costo = int(planes_empresa1[plan]) * 10000
        return costo
    if empresa == 2:
        costo = int(planes_empresa2[plan]) * 10000
        return costo
    if empresa == 3:
        costo = int(planes_empresa3[plan]) * 10000
        return costo
    if empresa == 4:
        costo = int(planes_empresa4[plan]) * 10000
        return costo
    
    


x1 = list()
x2 = list()
x3 = list()
x4 = list()
y = list()
b = list()
q = list()
s = list()

dic = {'nombre': [],'mes': [],'contrato': [],'plan': [],'cliente': [],'puerto': [],'valor':[],'costo':[]}

for v in m.getVars():
    nombre = str(v.varName)
    valor = str(v.x)
    if 'x1' in nombre and valor == '1.0':
        x1.append([nombre,valor])
    if 'x2' in nombre and valor == '1.0':
        x2.append([nombre,valor])
    if 'x3' in nombre and valor == '1.0':
        x3.append([nombre,valor])
    if 'x4' in nombre and valor == '1.0':
        x4.append([nombre,valor])
    if 'y' in nombre and valor != ('0.0' or '-0.0'):
        y.append([nombre,valor])
    if 'b' in nombre and valor != '0.0':
        b.append([nombre,valor])
    if 'q' in nombre and valor != ('0.0' or '-0.0'):
        q.append([nombre,valor])
    if 's' in nombre and valor != '-0.0':
        s.append([nombre,valor])
  



for i in x1:   
    aux = i[0].replace("x1", "")
    aux = aux.replace("[", "")
    aux = aux.replace("]", "")
    aux = aux.replace("(", "")
    aux = aux.replace(")", "")
    aux = aux.split(",")
    temp = (int(aux[2]), int(aux[3]), int(aux[4]), int(aux[5]), int(aux[6]))
    dic['nombre'].append(i[0])
    dic['mes'].append(int(aux[0]))
    dic['contrato'].append(aux[1])
    dic['plan'].append(temp)
    dic['cliente'].append("_")
    dic['puerto'].append("_")
    dic['valor'].append(i[1])
    dic['costo'].append(funcion_costo(1,temp)) 

for i in x2:   
    aux = i[0].replace("x2", "")
    aux = aux.replace("[", "")
    aux = aux.replace("]", "")
    aux = aux.replace("(", "")
    aux = aux.replace(")", "")
    aux = aux.split(",")
    temp = (int(aux[2]), int(aux[3]), int(aux[4]), int(aux[5]), int(aux[6]))
    dic['nombre'].append(i[0])
    dic['mes'].append(int(aux[0]))
    dic['contrato'].append(aux[1])
    dic['plan'].append(temp)
    dic['cliente'].append("_")
    dic['puerto'].append("_")
    dic['valor'].append(i[1])
    dic['costo'].append(funcion_costo(2,temp)) 

for i in x3:   
    aux = i[0].replace("x3", "")
    aux = aux.replace("[", "")
    aux = aux.replace("]", "")
    aux = aux.replace("(", "")
    aux = aux.replace(")", "")
    aux = aux.split(",")
    temp = (int(aux[2]), int(aux[3]), int(aux[4]), int(aux[5]), int(aux[6]))
    dic['nombre'].append(i[0])
    dic['mes'].append(int(aux[0]))
    dic['contrato'].append(aux[1])
    dic['plan'].append(temp)
    dic['cliente'].append("_")
    dic['puerto'].append("_")
    dic['valor'].append(i[1])
    dic['costo'].append(funcion_costo(3,temp))  


for i in x4:   
    aux = i[0].replace("x4", "")
    aux = aux.replace("[", "")
    aux = aux.replace("]", "")
    aux = aux.replace("(", "")
    aux = aux.replace(")", "")
    aux = aux.split(",")
    temp = (int(aux[2]), int(aux[3]), int(aux[4]), int(aux[5]))
    dic['nombre'].append(i[0])
    dic['mes'].append(int(aux[0]))
    dic['contrato'].append(aux[1])
    dic['plan'].append(temp)
    dic['cliente'].append("_")
    dic['puerto'].append("_")
    dic['valor'].append(i[1]) 
    dic['costo'].append(funcion_costo(4,temp)) 

for i in y:   
    aux = i[0].replace("y", "")
    aux = aux.replace("[", "")
    aux = aux.replace("]", "")
    aux = aux.split(",")
    dic['nombre'].append(i[0])
    dic['mes'].append(int(aux[0]))
    dic['contrato'].append("_")
    dic['plan'].append("_")
    dic['cliente'].append("_")
    dic['puerto'].append(aux[1])
    dic['valor'].append(i[1])
    dic['costo'].append("_") 

for i in b:   
    aux = i[0].replace("b", "")
    aux = aux.replace("[", "")
    aux = aux.replace("]", "")
    aux = aux.split(",")
    dic['nombre'].append(i[0])
    dic['mes'].append(int(aux[0]))
    dic['contrato'].append("_")
    dic['plan'].append("_")
    dic['cliente'].append("_")
    dic['puerto'].append(aux[1])
    dic['valor'].append(i[1])
    dic['costo'].append("_")    

for i in q:   
    aux = i[0].replace("q", "")
    aux = aux.replace("[", "")
    aux = aux.replace("]", "")
    aux = aux.split(",")
    dic['nombre'].append(i[0])
    dic['mes'].append(int(aux[0]))
    dic['contrato'].append("_")
    dic['plan'].append("_")
    dic['cliente'].append(aux[1])
    dic['puerto'].append("_")
    dic['valor'].append(i[1])
    dic['costo'].append("_") 

for i in s:   
    aux = i[0].replace("s", "")
    aux = aux.replace("[", "")
    aux = aux.replace("]", "")
    dic['nombre'].append(i[0])
    dic['mes'].append(int(aux))
    dic['contrato'].append("_")
    dic['plan'].append("_")
    dic['cliente'].append("_")
    dic['puerto'].append("_")
    dic['valor'].append(i[1])
    dic['costo'].append("_") 

    

print("--------")
print(dic)
print("--------")

df=pd.DataFrame.from_dict(dic,orient='index').transpose()

print(df.head(20))

df.to_excel("output.xlsx")    


