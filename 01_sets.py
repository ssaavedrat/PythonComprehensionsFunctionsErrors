# Sets

# Son mutables
# No tienen un orden
# Sus elementos son únicos

# Definimos el set
set_countries = {'col', 'mex', 'bol'}
# Print puede invertir en distinto orden al definido
# Pues el orden no es importante en un set
print(set_countries)
print(type(set_countries))

# No pueden haber dos elementos iguales
set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)

# Los sets pueden almacenar múltiples tipos de datos
set_types = {1, 'hola', False, 12.12}
print(set_types)

# Crear un set a partir de un string
set_from_string = set('hoola')
print("Set from string",set_from_string)

# Crear un set a partir de una tupla
set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)

# Crear un set a partir de una lista
numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)
# Lista de Números únicos de "numbers"
unique_numbers = list(set_numbers)
print(unique_numbers)