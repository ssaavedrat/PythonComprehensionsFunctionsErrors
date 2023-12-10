# Funciones con múltiples retornos

# Función de volumen, con parámetros con valores por defecto 1
def find_volume(length=1, width=1, depth=1):
  # Multiples retornos separados por coma
  return length * width * depth, width, 'hola'

# Variable simple
res = find_volume(depth=5)
# Tuple
print(res)

# Llamando a la función con un argumento específico
result, width, text = find_volume(width=10)

# Imprimiendo resultados
print(result)
print(width)
print(text)
