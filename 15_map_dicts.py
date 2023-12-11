# MAP
# Uso de Map con diccionarios

# Lista de diccionarios
items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]


prices = list(map(lambda item: item['price'], items))
products = list(map(lambda prod:prod['product'], items))

print("items\n",items)
print("prices\n",prices)

# Nuevo atributo de impuestos
# Recibe un dict de argumento y agrega un nuevo par llave-valor
def add_taxes(item):
  item['taxes'] = item['price'] * .19
  return item

new_items = list(map(add_taxes, items))
print("new_items\n",new_items)

# ¡Se realizó un cambio en la lista original!
print("items\n",items)