import csv

# Función para leer un archivo csv
def read_csv(path):
  with open(path, 'r') as file:
    # reader es un iterable
    reader = csv.reader(file, delimiter=",")
    # podemos obtener su primera iteracion, es decir,
    # el header con next()
    header = next(reader)
    # print(header)
    # arreglo de datos
    data = []
    for row in reader:
      # Como recordatorio
      # list(zip([a,b,c],[1,2,3])) = [(a,1),(b,2),(c,3)]
      # Construímos un zip con header y row
      iterable = zip(header, row)
      # Generamos un diccionario con dict comprehension
      country_dict = { key:value for key,value in iterable}
      data.append(country_dict)

  # Regresamos su resultado
  return data
  
# Llamada a módulo
if __name__ == '__main__':
  data = read_csv("./app/world_population.csv")
  # Imprimiendo primer elemento del diccionario
  for key, value in data[3].items():
    print(f'{key}: {value}')