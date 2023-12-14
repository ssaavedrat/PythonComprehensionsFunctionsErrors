# Escribir archivos

# Permisos de escritura 'w'
# Permisos de lectura 'r' (por defecto)
# Permisos de escritura 'r+' (lectura y escritura) respetando el contenido
# Permisos de escritura 'w+' (lectura y escritura) borrando el contenido

with open('./text.txt', 'r+') as file:
  for line in file:
    print(line)
  # Escribimos nuevas lineas con caracter especial 
  # \n : salto de línea (newline) 
  file.write('nuevas cosas en este archivo\n')
  file.write('otra linea\n')
  file.write(' mas linea\n')