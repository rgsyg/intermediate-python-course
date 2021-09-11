import random

dice_rolls = int(input('How many dice would you like to roll? '))
dice_size = int(input('How many sides are the dice? '))

player_size = int(input('How many players? '))
player_name = []

for i in range(0, player_size):
    player_name += input(f'Player {i} name: ')

dice_sum = 0
player_counter = 0

for i in range(0, dice_rolls*player_size):
      print(f'{player_name[player_counter]} turn')
      roll = random.randint(1, dice_size)
      dice_sum += roll
      if roll == 1:
        print(f'You rolled a {roll}! Critical Fail')
      elif roll == dice_size:
        print(f'You rolled a {roll}! Critical Success')
      else:
        print(f'You rolled a {roll}'s)
      player_counter += 1
      if player_counter == player_size:
          player_counter = 0

print(f'You have rolled a total of {dice_sum}')
