import random

# Lista de países
countries = ['col', 'mex', 'bol', 'pe']

# Generar pais - población aleatoria
population_v2 = { country: random.randint(1, 100)  for country in countries}

print("Población:",population_v2)

# Nuevo diccionario recorriendo los items de población anterior, agregando una condicional
# en caso de que la población sea mayor a 50, entonces se agrega
result = { country: population for (country, population) in population_v2.items() if population > 50 }
print("Población filtrada:",result)

# Texto
text = 'Hola, soy Nicolas'

# crear un conjunto clave-valor con las vocales minus: vocales mayus
# Se itera sobre "text"
# Recordar que el diccionario tiene una única llave por lo que se reemplaza si ocurre más veces.
unique = { c: c.upper() for c in text if c in 'aeiou' }
print(unique)