# Filter con Dict.

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

print("Partidos\n",matches)
print("\nCantidad de Partidos\n",len(matches))

# Filtramos equipos que han ganado
new_list = list(filter(lambda item: item['home_team_result'] == 'Win', matches))

print("\nPartidos Ganados por Local\n",new_list)
print("\nNro. Partidos Ganados Local\n",len(new_list))

# En este caso no se modifica el arreglo original
print(matches)
print(len(matches))