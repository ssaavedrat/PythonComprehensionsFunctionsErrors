# Reduce
# Obtener un resultado de una lista o iterable

# Importamos la librería functools
import functools

# Lista de números
numbers = [1, 2, 3, 4]

# Función que suma dos números
def accum(counter, item):
  print('counter:',counter)
  print('item:',item)
  return counter + item

# Sumamos todos los números del array con functools.reduce
result = functools.reduce(accum, numbers)

r2 = functools.reduce(lambda x,y:x+y, numbers)

print(result)
print(r2)