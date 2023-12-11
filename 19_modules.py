# Modulos de Python

# Módulo del sistema
import sys
# Ruta del sistema
print(sys.path, end= "\n\n")

# Regular Expresssions
import re
text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte 3'
# Encontrar numeros
result = re.findall('[0-9]+', text)
print(result, end= "\n\n")

# Tiempo
import time
# Hora actual para la computadora
timestamp = time.time()
print(timestamp, end= "\n\n")

# Formato más amigable
local = time.localtime()
# Ascii time
result = time.asctime(local)
print(result, end= "\n\n")

# Collections
import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
# Conteo de elementos
counter = collections.Counter(numbers)
print(counter, end= "\n\n")