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

def who_wins(player, computer):
    if (
        (player == 'r' and computer == 'sc') or
        (player == 'p' and computer == 'r') or
        (player == 'sc' and computer == 'p') or
        (player == 'r' and computer == 'l') or
        (player == 'l' and computer == 'sp') or
        (player == 'sp' and computer == 'sc') or
        (player == 'sc' and computer == 'l') or
        (player == 'l' and computer == 'p') or
        (player == 'p' and computer == 'sp') or
        (player == 'sp' and computer == 'r')
       ):
        return 'player'
    elif player == computer:
        return 'tie'
    else:
        return 'computer'

def display_winner(winner):
    if winner == 'player':
        prompt('You win!')
    elif winner == 'computer':
        prompt('Computer wins!')
    else:
        prompt("It's a tie!")

prompt("Let's play Rock-Paper-Scissors-Spock-Lizard!\n")

player_score = 0
computer_score = 0

while True:
    prompt("Enter one of the following: ")
    for key, value in VALID_CHOICES.items():
        print(f"     '{key}' to select {value}")
    player_choice = input()

    while player_choice not in VALID_CHOICES:
        prompt("That's not a valid choice.")
        player_choice = input()

    computer_choice = random.choice(list(VALID_CHOICES.keys()))

    prompt(f'You chose {VALID_CHOICES[player_choice]}. '
           f'The computer chose {VALID_CHOICES[computer_choice]}.')

    game_winner = who_wins(player_choice, computer_choice)
    display_winner(game_winner)

    if game_winner == 'player':
        player_score +=1
    if game_winner == 'computer':
        computer_score += 1

    prompt(f'SCORE: You - {player_score}. Computer - {computer_score}.\n')

    if player_score == 3:
        prompt('You win the match!')
        break
    if computer_score == 3:
        prompt('Computer wins the match!')
        break