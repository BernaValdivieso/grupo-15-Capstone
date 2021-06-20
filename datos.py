# Producción esperada mes : cantidad_esperada
produccion_esperada = {1: 110000,
                       2: 90000,
                       3: 110000,
                       4: 100000,
                       5: 90000,
                       6: 100000,
                       7: 120000,
                       8: 110000,
                       9: 110000,
                       10: 120000,
                       11: 100000,
                       12: 100000
                       }

# Inventario Inicial
inventario_inicial = 30000

# CLientes como clase
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


# Puertos; puerto: región
puertos_dict = {1: 1,
           2: 1,
           3: 2,
           4: 2,
           5: 3,
           6: 3,
           7: 4,
           8: 4
           }






 


