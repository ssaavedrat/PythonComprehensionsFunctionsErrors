# Importando módulo personalizado
import utils

# Llamando funcion get_population del modulo utils
keys, values = utils.get_population()

print(keys,values)

# Obtener variable del módulo mod
print(utils.A)

# Datos
data = [
  {
    'Country': 'Colombia',
    'Population': 500
  },
  {
    'Country': 'Bolivia',
    'Population': 300
  }
]

# País a filtrar
country = 'Colombia'
# country = input("Ingresa el país a filtrar:")

# Llamando a la función population_by_country del modulo utils
result = utils.population_by_country(data,country)
print(result)