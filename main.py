from datos import *
from gurobipy import *
from Parametros import *
from Variables import *

# Crear Modelo
m = Model("planificacion")
m.reset()

# Crear Variables
x = m.addVars(X_m_f_p, vtype=GRB.BINARY, name="x")
y = m.addVars(Y_m_d, name="y")
b = m.addVars(B_m_d, name="b")
q = m.addVars(Q_m_c, name="q")
s = m.addVars(S_m, name="s")

# Función Objetivo

# Restricciones COA
# Restricciones Clientes
# Restricciones Producción
