# Add bonus features:
#    1. rock-paper-scissors-spock-lizard
#    2. shorten player input
#    3. best of 5

import random

VALID_CHOICES = {
    'r':  'rock', 
    'p':  'paper', 
    'sc': 'scissors', 
    'sp': 'spock', 
    'l':  'lizard',
}

def prompt(message):
    print(f'==> {message}')

def who_wins_game(player, computer):
    prompt(f'You chose {VALID_CHOICES[player]}. '
           f'The computer chose {VALID_CHOICES[computer]}.')
    if ((player == 'r' and computer == 'sc') or
       (player == 'p' and computer == 'r') or
       (player == 'sc' and computer == 'p') or
       (player == 'r' and computer == 'l') or
       (player == 'l' and computer == 'sp') or
       (player == 'sp' and computer == 'sc') or
       (player == 'sc' and computer == 'l') or
       (player == 'l' and computer == 'p') or
       (player == 'p' and computer == 'sp') or
       (player == 'sp' and computer == 'r')):
        return 'player'
    elif ((computer == 'r' and player == 'sc') or
       (computer == 'p' and player == 'r') or
       (computer == 'sc' and player == 'p') or
       (computer == 'r' and player == 'l') or
       (computer == 'l' and player == 'sp') or
       (computer == 'sp' and player == 'sc') or
       (computer == 'sc' and player == 'l') or
       (computer == 'l' and player == 'p') or
       (computer == 'p' and player == 'sp') or
       (computer == 'sp' and player == 'r')):
        return 'computer'
    else:
        return 'tie'

prompt("Let's play Rock-Paper-Scissors-Spock-Lizard!\n")

player_wins = 0
computer_wins = 0

while True:
    prompt("Enter one of the following: ")
    for key, value in VALID_CHOICES.items():
        print(f"     '{key}' to select {value}")
    player_choice = input()

    while player_choice not in VALID_CHOICES:
        prompt("That's not a valid choice.")
        player_choice = input()

    computer_choice = random.choice(list(VALID_CHOICES.keys()))

    game_winner = who_wins_game(player_choice, computer_choice)

    if game_winner == 'player':
        player_wins +=1
        prompt('You win!')
    elif game_winner == 'computer':
        computer_wins += 1
        prompt('Computer wins!')
    else:
        prompt("It's a tie!")

    prompt(f'SCORE: You - {player_wins}. Computer - {computer_wins}.')

    if player_wins == 3:
        prompt('You win the match!')
        break
    elif computer_wins == 3:
        prompt('Computer wins the match!')
        break