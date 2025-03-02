# Add bonus features:
#    1. rock-paper-scissors-spock-lizard
#    2. shorten player input

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

def display_winner(player, computer):
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
        prompt('You win!')
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
        prompt('Computer wins!')
    else:
        prompt("It's a tie!")

prompt("Let's play Rock-Paper-Scissors-Spock-Lizard!")

while True:

    prompt(f"Enter one of the following: ")
    for key, value in VALID_CHOICES.items():
        prompt(f"  '{key}' for {value}")
    player_choice = input()

    while player_choice not in VALID_CHOICES:
        prompt("That's not a valid choice.")
        player_choice = input()

    computer_choice = random.choice(list(VALID_CHOICES.keys()))

    display_winner(player_choice, computer_choice)

    while True:
        prompt("Do you want to play again (y/n)?")
        play_again = input().lower()

        if play_again.startswith('n') or play_again.startswith('y'):
            break
        else:
            prompt("That's not a valid choice. Enter 'y' or 'n'")

    if play_again[0] == 'n':
        break