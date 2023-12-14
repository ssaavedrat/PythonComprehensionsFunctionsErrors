# Iterables
# Pueden ser manejados por un ciclo o 
# controlables manualmente

# Hemos hecho iteraciones con un ciclo for
for i in range(1, 11):
  print(i)

# Cuando range pasa por iter() se crea un objeto iterable
my_iter = iter(range(1, 4))
# range_iterator object
print(my_iter)

# Iterando "manualmente"
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# Esta linea generará la excepción StopIteration
print(next(my_iter))

# Lo beneficioso de usar iter() es que para grandes volumenes de datos se puede 
# evitar consumir memoria y tiempo de ejecución