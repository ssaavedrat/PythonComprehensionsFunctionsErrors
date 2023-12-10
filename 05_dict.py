# Dictionary Comprehension

"""
Caso general:

{key:value for var in iterable}

"""

# Diccionario con llave numero y valor numero por dos
dict = {}
for i in range(1, 5):
  dict[i] = i * 2

print("Ciclo for:",dict)

# Usando dict comprehension
dict_v2 = { i: i * 2 for i in range(1, 5)}
print("Dict comp.",dict_v2)

import random

# Lista de países
countries = ['col', 'mex', 'bol', 'pe']
# Diccionario de población por país
population = {}

# Ciclo for
for country in countries:
  population[country] = random.randint(1, 100)
print(population)

# Usando dict comprehension
population_v2 = { country: random.randint(1, 100)  for country in countries}
print(population_v2)

# nombres de usuarios
names = ['nico', 'zule', 'santi']
# edad de cada usuario
ages = [12, 56, 98]

# Queremos generar un diccionario con usuario y edad

# zip solo entrega un objeto iterable, es necesario cambiar su tipo a list para imprimirlo
print(list(zip(names, ages)))

# usando dict comprehension
new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)