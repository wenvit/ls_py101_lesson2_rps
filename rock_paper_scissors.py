# Add bonus feature:  rock-paper-scissors-spock-lizard

import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']

def prompt(message):
    print(f'==> {message}')

def display_winner(player, computer):
    prompt(f'You chose {player_choice}. '
           f'The computer chose {computer_choice}.')
    if ((player == 'rock' and computer == 'scissors') or
       (player == 'paper' and computer == 'rock') or
       (player == 'scissors' and computer == 'paper') or
       (player == 'rock' and computer == 'lizard') or
       (player == 'lizard' and computer == 'spock') or
       (player == 'spock' and computer == 'scissors') or
       (player == 'scissors' and computer == 'lizard') or
       (player == 'lizard' and computer == 'paper') or
       (player == 'paper' and computer == 'spock') or
       (player == 'spock' and computer == 'rock')):
        prompt('You win!')
    elif ((computer == 'rock' and player == 'scissors') or
       (computer == 'paper' and player == 'rock') or
       (computer == 'scissors' and player == 'paper') or
       (computer == 'rock' and player == 'lizard') or
       (computer == 'lizard' and player == 'spock') or
       (computer == 'spock' and player == 'scissors') or
       (computer == 'scissors' and player == 'lizard') or
       (computer == 'lizard' and player == 'paper') or
       (computer == 'paper' and player == 'spock') or
       (computer == 'spock' and player == 'rock')):
        prompt('Computer wins!')
    else:
        prompt("It's a tie!")

prompt("Let's play Rock-Paper-Scissors-Spock-Lizard!")

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