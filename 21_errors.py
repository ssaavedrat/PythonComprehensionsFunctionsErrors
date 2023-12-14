# Errores en Python

# SyntaxError
# print('Hola'))

# ZeroDivisionError
# print(0 / 0)

# NameError
# print(result)

# Cuando ocurre un error la ejecucuón del programa se termina
# print('No se ejecuta esto')

# Si la función suma cambia se produce un AssertionError
suma = lambda x,y: x + y
# Verificación con assert
assert suma(2,2) == 4

print('Hola')

# Generación de errores personalizados
age = 10
if age < 18:
  # Excepción personalizada
  raise Exception('No se permiten menores de edad')

# Este tipo de errores personalizado también interrumpe la ejecución del programa
print('Hola 2')