from datos import *
from gurobipy import *  
from Parametros import *
from Variables import *

# Conjuntos
meses = [i for i in range(1,13)]
contratos = [1, 2, 3, 4]
### planes
### puertos

# Crear Modelo
m = Model("planificacion")
m.reset()

# Crear Variables
x = m.addVars(X_m_f_p, vtype=GRB.BINARY, name="x")
y = m.addVars(Y_m_d, vtype=GRB.INTEGER, lb = 0, ub = 4,name="y")            
b = m.addVars(B_m_d, vtype=GRB.INTEGER, lb = 0, name="b")
q = m.addVars(Q_m_c, vtype=GRB.INTEGER, lb = 0, name="q")
s = m.addVars(S_m, vtype=GRB.INTEGER, lb = 0, name="s")

# Función Objetivo
m.setObjective(quicksum(x[m,f,p] for m, f, p in X_m_f_p), GRB.MINIMIZE)

# Restricciones COA
m.addConstrs(quicksum(x[m,f,p] for p in X_m_f_p) <= 1 for m, f in X_m_f_p)

# Restricciones Clientes
# Restricciones Producción
