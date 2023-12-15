# Es posible que sea necesario instalar la librería
# Utilizamos la sección pyplot de matplotlib
# Alias 'plt'
import matplotlib.pyplot as plt

def generate_bar_chart(labels,values):
  fig, ax = plt.subplots()
  ax.bar(labels,values)
  plt.show()

def generate_pie_chart(labels,values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  # organizar en centro
  ax.axis('equal')
  plt.show()
  
if __name__ == '__main__':
  labels = ['a','b','c']
  values = [10,200,50]
  # generate_bar_chart(labels,values)
  generate_pie_chart(labels,values)

