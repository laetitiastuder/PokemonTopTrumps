import random
import requests

def random_pokemon():
  pokemon_number= random.randint(1,151)
  url='https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
  response=requests.get(url)
  pokemon = response.json()

  return {
    'name':pokemon['name'],
    'id':pokemon['id'],
    'height': pokemon['height'],
    'weight': pokemon['weight'],
  }

def run():
  player1_pokemon=random_pokemon()

  print('Your were given {}'.format(player1_pokemon['name']))
  stat_choice= input('Which stat do you want to use? (id, height,weight)')

  player2_pokemon= random_pokemon()
  print('The opponent chose {}'.format(player2_pokemon['name']))

  player1_stat= player1_pokemon[stat_choice]
  player2_stat= player2_pokemon[stat_choice]

  if player1_stat > player2_stat:
    print('You win!')
  elif player1_stat < player2_stat:
    print('You lose!')
  else:
    print ("It's a draw!")
run() 
