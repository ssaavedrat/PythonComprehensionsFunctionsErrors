# Operaciones con conjuntos

# Definición de dos conjuntos, set_a y set_b, que contienen elementos de países
set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# Unión de los conjuntos set_a y set_b (todos los elementos sin duplicados)
set_c = set_a.union(set_b)
print(set_c)
# Alternativa usando el operador | para la unión
print(set_a | set_b)

# Intersección de los conjuntos set_a y set_b (elementos comunes)
set_c = set_a.intersection(set_b)
print(set_c)
# Alternativa usando el operador & para la intersección
print(set_a & set_b)

# Diferencia entre set_a y set_b (elementos en set_a pero no en set_b)
set_c = set_a.difference(set_b)
print(set_c)
# Alternativa usando el operador - para la diferencia
print(set_a - set_b)

# Diferencia simétrica entre set_a y set_b (elementos que están en uno de los conjuntos pero no en ambos)
set_c = set_a.symmetric_difference(set_b)
print(set_c)
# Alternativa usando el operador ^ para la diferencia simétrica
print(set_a^set_b)