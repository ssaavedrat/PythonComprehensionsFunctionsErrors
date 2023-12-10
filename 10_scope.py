# Scope o Alcance
# Scope es el alcance de una variable en un bloque de código.
# Built-in > Global > Enclosing Scope > Local Scope

price = 100 # global

def increment():
  # Crea una variable local
  price = 200 # local
  # Usa la variable local
  # La variable result solo tiene un scope dentro de la función
  result = price + 10
  print(result)
  return result

print(price)
price_2 = increment()
print(price_2)