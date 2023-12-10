# Set de países
set_countries = {'col', 'mex', 'bol'}

# Tamaño de conjunto
size = len(set_countries)
print("El tamaño del conjunto es",size)

# Pertenencia
print("¿Colombia en set?",'col' in set_countries)
print("¿Perú en set?",'pe' in set_countries)

# Add
set_countries.add('pe')
print("Agregando Perú:",set_countries)
set_countries.add('pe')
print("Agregando Perú:",set_countries)

# Update
# Agrega los elementos listados
set_countries.update({'ar', 'ecua', 'pe'})
print("Set Actualizado:",set_countries)

# Remove
set_countries.remove('col')
print("Colombia eliminado:",set_countries)
# Remover otro país
set_countries.remove('ar')

# Si ejecutamos esto,
# set_countries.remove('arg')
# Fallará. 

# Discard no interrumpe la ejecución del programa
set_countries.discard('arg')


print("Argentina Eliminado:",set_countries)
set_countries.add('arg')
print(set_countries)

# Limpiar todo el set
set_countries.clear()
print(set_countries)
print(len(set_countries))