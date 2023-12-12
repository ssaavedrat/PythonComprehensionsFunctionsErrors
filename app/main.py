# Importando módulo personalizado
import utils

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

def run():
  # Llamando funcion get_population del modulo utils
  keys, values = utils.get_population()
  
  print("Resultado de get_population:",keys,values)
  
  # Obtener variable del módulo mod
  print("utils.A:",utils.A)
  

  # País a filtrar
  country = 'Colombia'
  # country = input("Ingresa el país a filtrar:")
  
  # Llamando a la función population_by_country del modulo utils
  result = utils.population_by_country(data,country)
  print("Resultado de population_by_country:",result)

# Entry point para ejecutar el programa
if __name__ == '__main__':
  run()