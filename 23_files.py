file = open('./text.txt')

# Leer todo el archivo
# print(file.read())

# Leer una fila
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# Leer cada linea
for line in file:
  print(line)
file.close()

# Forma pythonista, abre el archivo y lo cierra automáticamente (liberando memoria) una 
# Vez termina la lectura
with open('./text.txt') as file:
  for line in file:
    print(line, end="")