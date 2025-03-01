

import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f'==> {message}')

def display_winner(player, computer):
    prompt(f'You chose {player_choice}. '
           f'The computer chose {computer_choice}.')

    if ((player == 'rock' and computer == 'scissors') or
       (player == 'paper' and computer == 'rock') or
       (player == 'scissors' and computer == 'paper')):
        prompt('You win!')
    elif ((player == 'rock' and computer == 'paper') or
          (player == 'paper' and computer == 'scissors') or
          (player == 'scissors' and computer == 'rock')):
        prompt('Computer wins!')
    else:
        prompt("It's a tie!")

prompt("Let's play Rock-Paper-Scissors!")

while True:

    prompt(f"Choose one: {', '.join(VALID_CHOICES)}")
    player_choice = input()

    while player_choice not in VALID_CHOICES:
        prompt("That's not a valid choice.")
        player_choice = input()

    computer_choice = random.choice(VALID_CHOICES)

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