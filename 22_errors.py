# Manejo de errores


try:
  print(0 / 0)
# Capturamos errores con except
except ZeroDivisionError as error:
  print(error)

try:
  # Si falla puede escribir un mensaje de error
  assert 1 != 1, 'Uno no es igual que uno'
except AssertionError as error:
  print(error)

try:
  age = 10
  if age < 18:
    raise Exception('No se permiten menores de edad')
except Exception as error: 
  print(error)

print('Hola')

# Podemos unificar el bloque try-except, pero solo detecta el primer error

try:
  print(1 / 0)
  assert 1 != 1, 'Uno no es igual que uno'
  age = 10
  if age < 18:
    raise Exception('No se permiten menores de edad')

except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)

print('Fin del programa')