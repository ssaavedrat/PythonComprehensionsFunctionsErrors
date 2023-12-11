# MAP
# Transformaciones a una lista de elementos

# lista de números
numbers = [1, 2, 3, 4]

# transformar elementos i * 2
numbers_v2 = []
for i in numbers:
  numbers_v2.append(i * 2)

# versión con lambda y map 
numbers_v3 = list(map(lambda i: i * 2, numbers))

# aunque posiblemente sea más limpio con list comprehension
# numbers_v4 = [i * 2 for i in numbers]

print("numbers:",numbers)
print("numbersv2:",numbers_v2)
print("numbersv3:",numbers_v3)

# Otro caso, dos listas de números
numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

print(numbers_1)
print(numbers_2)
# Sumar cada elemento
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
# Entregará un tamaño equivalente al de la lista más pequeña
print(result)