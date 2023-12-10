# Funciones con return

def sum_with_range(min, max):
  """
  Calcula la suma de los números entre range(min,max) es decir [min,max-1]
  """
  print(min, max)
  sum = 0
  for x in range(min, max):
    sum += x
  return sum

# Llamando a la función, guardando el resultado en una variable
result = sum_with_range(1, 10)
print(result)

# Reutilizando la función
result_2 = sum_with_range(result, result + 10)
print(result_2)