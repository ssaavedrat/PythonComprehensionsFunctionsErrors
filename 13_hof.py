# High Order Functions

# Función
def increment(x):
  return x + 1

# Función lambda
increment_v2 = lambda x: x +1

# Función toma como argumento otra función
def high_ord_func(x, func):
  # Llama a la función func con argumento x
  return x + func(x)

# HOF versión lambda
high_ord_func_v2 = lambda x, func: x + func(x)

# Llamada a la HOF
result = high_ord_func(2, increment)
# 2 + (2 + 1)
print("Resultado hof(2):",result)

# Llamando a la HOF versión lambda
result = high_ord_func_v2(2, increment_v2)
print("Resultado hof_v2(2):",result)

# Podemos cambiar la función de argumento de la hof
result = high_ord_func_v2(2, lambda x: x + 2)
print("Nueva función:",result) # 2 + (2 + 2)
# Nuevamente
result = high_ord_func_v2(2, lambda x: x * 5)
print("Nueva función 2:",result) # 2 + (2 * 5)