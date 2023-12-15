# def get_population():
#   keys = ['col', 'bol']
#   values = [300,500]
#   return keys, values

def get_population(country_dict):
  # Diccionario de población por año
  population_dict = {
    '2022':int(country_dict['2022 Population']),
    '2020':int(country_dict['2020 Population']),
    '2015':int(country_dict['2015 Population']),
    '2010':int(country_dict['2010 Population']),
    '2000':int(country_dict['2000 Population']),
    '1990':int(country_dict['1990 Population']),
    '1980':int(country_dict['1980 Population']),
    '1970':int(country_dict['1970 Population'])
  }
  # Obtener una lista de las llaves
  keys = population_dict.keys()
  # Obtener una lista de los valores
  values = population_dict.values()
  return keys, values

A = "Hola"

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result

