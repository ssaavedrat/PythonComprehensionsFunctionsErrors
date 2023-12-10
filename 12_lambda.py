# Funciones lambda o anónimas

# función increment
def increment(x):
  return x + 1

# funcion increment_v2
increment_v2 = lambda x: x + 1
print("Tipo de dato de increment_v2",type(increment_v2))

# Ambas funciones hacen lo mismo
result = increment(10)
print(11)
result = increment_v2(20)
print(result)

# Otra lambda function con dos argumentos
full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'

text = full_name('nicolas', 'perez casas')
print(text)