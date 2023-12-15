# Importando módulo personalizado
import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv("./app/world_population.csv")

  world_pop = {country_dict['Country/Territory']: country_dict['World Population Percentage'] for country_dict in data }

  charts.generate_pie_chart(world_pop.keys(), world_pop.values())
  
  

  # País a filtrar
  # country = 'Colombia'
  # country = input("Ingresa el país a filtrar:")

  # result = utils.population_by_country(data,country)
  # print("Resultado de population_by_country:",result)

  # # Caso país no encontrado
  # if len(result) == 0:
  #   print("No se encontró ningún país con ese nombre")
  #   return

  # country_dict = result[0]  
  # # Llamando funcion get_population del modulo utils
  # keys, values = utils.get_population(country_dict)
  # print("Resultado de get_population:",keys,values)

  # charts.generate_bar_chart(keys,values)
  
  # Obtener variable del módulo mod
  # print("utils.A:",utils.A)
  

  
  # Llamando a la función population_by_country del modulo utils

# Entry point para ejecutar el programa
if __name__ == '__main__':
  run()